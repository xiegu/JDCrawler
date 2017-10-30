#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

'''
@Descripition
JD item score crawler - to crawl item score information in JD

JD sets up 3-level categories for each listing item: firstCategory, secondCategory, thirdCategory,
which are encoded with distinct number respectively.
'''

import time, sys, os, threading, Queue
import config
from config import get_itemScore_url, THREAD_NUM
from crawler.htmlDownloader import HtmlDownloader
from crawler.htmlParser import HtmlParser
from util.myThread import MyThread
from db.sqlHelper import CatItemSqlHelper

reload(sys)
sys.setdefaultencoding('utf8')


class JDItemScoreCrawler(object):
	def __init__(self, queue1, queue2):
		self.queue1 = queue1
		self.queue2 = queue2

	def run(self):
		# while True: update every Monday in plan
		global SCORE
		SCORE = []
		print 'Start crawling item score in JD' + ' ' + '>'*20
		query = CatItemSqlHelper().select()
		itemIdList = [i[0] for i in query]
		print 'totally %d items' %len(itemIdList)
		self.scoreThread(itemIdList)
		print 'totally %d items in SCORE' %len(SCORE)
		scoreIdList = [str(s['SkuId']) for s in SCORE]
		for i in range(len(SCORE)):
			j = itemIdList.index(scoreIdList[i])
			SCORE[i]['category'] = query[j][1]
		for i in SCORE:
			if i is not None:
				self.queue2.put(i)

	def scoreThread(self, itemIdList):
		global SCORE
		print '%d threads are working' %THREAD_NUM
		threads = []
		for i in itemIdList:
			self.queue1.put(i)
		for t in range(THREAD_NUM):
			thread = MyThread(self.worker)
			threads.append(thread)
		for t in threads:
			t.start()
		for t in threads:
			t.join()
		self.queue1.join()

	def worker(self):
		while not self.queue1.empty():
			item = self.queue1.get()
			self.scoreCrawler(config.parserList[5], item)
			self.queue1.task_done()

	def scoreCrawler(self, parser, itemId):
		html_parser = HtmlParser()
		while True:
			content = HtmlDownloader.download(get_itemScore_url(itemId))
			score = html_parser.parse(content, parser)
			if score is not None:
				break
			else:
				time.sleep(5)
				continue
		SCORE.extend(score)