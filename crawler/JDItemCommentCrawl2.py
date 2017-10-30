#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

'''
@Descripition
JD item comment crawler - to crawl item comment information in JD

JD sets up 3-level categories for each listing item: firstCategory, secondCategory, thirdCategory,
which are encoded with distinct number respectively.
'''

import random, time, sys, os, threading, Queue
import config
from config import get_itemComment_url, THREAD_NUM, PROXIESURL
from crawler.htmlDownloader import HtmlDownloader
from crawler.htmlParser import HtmlParser
from util.myThread import MyThread
from util.myProxies import get_proxies
from db.sqlHelper import CatItemSqlHelper

reload(sys)
sys.setdefaultencoding('utf8')

def startItemCommentCrawl(queue1, queue2):
	crawl = JDItemCommentCrawler(queue1, queue2)
	crawl.run()

class JDItemCommentCrawler(object):
	def __init__(self, queue1, queue2):
		self.queue1 = queue1
		self.queue2 = queue2

	def run(self):
		# while True: update every Monday in plan
		print 'Start crawling item comment in JD' + ' ' + '>'*20
		query = CatItemSqlHelper().select()
		itemIdList = [i[0] for i in query]
		itemIdList = random.sample(itemIdList, len(itemIdList))
		print 'totally %d items' %len(itemIdList)
		self.commentThread(itemIdList)

	def commentThread(self, itemIdList):
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
		#self.queue1.join()

	def worker(self):
		while not self.queue1.empty():
			item = self.queue1.get()
			self.commentCrawler(config.parserList[6], item)
			#self.queue1.task_done()

	def commentCrawler(self, parser, itemId, pageNum = 70):
		html_parser = HtmlParser()
		itemList = []
		proxies = get_proxies(PROXIESURL, free = True)
		for p in range(pageNum):
			while True:
				if p < 50:
					content = HtmlDownloader.download(get_itemComment_url(itemId, p))
				else:
					content = HtmlDownloader.download_proxy(get_itemComment_url(itemId, p), proxies)
				comment = html_parser.parse(content, parser)
				if comment is not None:
					break
				else:
					time.sleep(10)
					continue
			if(len(comment) == 0):
				break
			else:
				for i in range(len(comment)):
					comment[i]['id'] = itemId
					self.queue2.put(comment[i])
				itemList.extend(comment)
		print '%s done' %itemId
		#print '%d' %self.queue2.qsize()
		print 'Comment length %d' %len(itemList)