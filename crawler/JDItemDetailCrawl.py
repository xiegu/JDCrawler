#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

'''
@Descripition
JD item detail crawler - to crawl item detail information in JD

JD sets up 3-level categories for each listing item: firstCategory, secondCategory, thirdCategory,
which are encoded with distinct number respectively.
'''

import time, sys, os, threading, Queue
import config
from config import get_itemDetail_url, THREAD_NUM
from crawler.htmlDownloader import HtmlDownloader
from crawler.htmlParser import HtmlParser
from util.myThread import MyThread
from db.sqlHelper import CatItemSqlHelper

reload(sys)
sys.setdefaultencoding('utf8')


class JDItemDetailCrawler(object):
	def __init__(self, queue1, queue2):
		self.queue1 = queue1
		self.queue2 = queue2

	def run(self):
		# while True: update every Monday in plan
		global DETAIL
		DETAIL = []
		print 'Start crawling item detail in JD' + ' ' + '>'*20
		query = CatItemSqlHelper().select()
		itemIdList = [i[0] for i in query]
		print 'totally %d items' %len(itemIdList)
		self.detailThread(itemIdList)
		print 'totally %d items in DETAIL' %len(DETAIL)
		# detailIdList = [str(d['id']) for d in DETAIL]
		# for i in range(len(DETAIL)):
		# 	j = itemIdList.index(detailIdList[i])
		# 	DETAIL[i]['category'] = query[j][1]
		for i in DETAIL:
			if i is not None:
				self.queue2.put(i)

	def detailThread(self, itemIdList):
		global DETAIL
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
			self.detailCrawler(config.parserList[7], item)
			print 'item %s done' %item
			self.queue1.task_done()

	def detailCrawler(self, parser, itemId):
		html_parser = HtmlParser()
		while True:
			content = HtmlDownloader.download(get_itemDetail_url(itemId))
			detail = html_parser.parse(content, parser)
			if detail is not None:
				break
			else:
				time.sleep(5)
				continue
		DETAIL.extend(detail)