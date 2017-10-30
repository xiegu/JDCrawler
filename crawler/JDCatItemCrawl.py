#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

'''
@Descripition
JD items crawler - to crawl item id of each item listed in all the categories available now in the config.catList

JD sets up 3-level categories for each listing item: firstCategory, secondCategory, thirdCategory,
which are encoded with distinct number respectively.
'''

import time, sys, os, threading, Queue
import config
from config import get_item_url, get_price_url,THREAD_NUM
from crawler.htmlDownloader import HtmlDownloader
from crawler.htmlParser import HtmlParser
from util.myThread import MyThread

reload(sys)
sys.setdefaultencoding('utf8')


class JDCatItemCrawler(object):
	def __init__(self, queue1, queue2):
		self.queue1 = queue1
		self.queue2 = queue2

	def run(self):
		# while True: update every Monday in plan
		global PRICE
		PRICE = []
		print 'Start crawling search page number of each category' + ' ' + '>'*20
		pageNumList = self.pageCrawler(config.parserList[0])
		print 'Start crawling details of items in each category' + ' ' + '>'*20
		itemList = self.itemCrawler(config.parserList[1], pageNumList)
		#itemIdList = id_spliter([i[id] for i in itemList], THREAD_NUM)
		print 'Start crawling price of all items in each category' + ' ' + '>'*20
		itemIdList = [i['id'] for i in itemList]
		print 'totally %d items' %len(itemIdList)
		self.priceThread(itemIdList)
		# Modify these code
		priceIdList = [i['id'] for i in PRICE]
		for i in range(len(itemList)):
			j = priceIdList.index(itemIdList[i])
			#print '%s and %s' %(itemList[i]['id'], PRICE[j]['id'])
			itemList[i]['m'] = float(PRICE[j]['m'])
			itemList[i]['op'] = float(PRICE[j]['op'])
			itemList[i]['p'] = float(PRICE[j]['p'])
		for i in itemList:
			if i is not None:
				self.queue2.put(i)

	def priceThread(self, itemIdList):
		global PRICE
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
			self.priceCrawler(config.parserList[2], item)
			self.queue1.task_done()

	def pageCrawler(self, parser):
		html_parser = HtmlParser()
		pageNumList = []
		for c in config.catList:
			while True:
				content = HtmlDownloader.download(get_item_url(c['category'], 1))
				if not len(content) < 100:
					pageNum = html_parser.parse(content, parser)
					print pageNum
					break
				else:
					time.sleep(5)
					continue
			pageNumList.append({'category': c['category'], 'pageNum': pageNum})
		return pageNumList

	def itemCrawler(self, parser, pageNumList):
		html_parser = HtmlParser()
		itemList = []
		for c in config.catList:
			for p in pageNumList:
				if c['category'] == p['category']:
					pageNum = p['pageNum']
					break
				else:
					continue
			catItemList = []
			for p in range(pageNum):
				while True:
					content = HtmlDownloader.download(get_item_url(c['category'], p+1))
					if not len(content) < 100:
						item = html_parser.parse(content, parser)
						for i in range(len(item)):
							item[i]['category'] = c['category']
						break
					else:
						time.sleep(5)
						continue
				catItemList.extend(item)
			itemList.extend(catItemList)
			print 'Category %s done. \n' %c['category']
		return itemList

	def priceCrawler(self, parser, itemId):
		html_parser = HtmlParser()
		while True:
			content = HtmlDownloader.download(get_price_url(itemId))
			price = html_parser.parse(content, parser)
			if price is not None:
				#print '%s done' %itemId
				break
			else:
				time.sleep(5)
				continue			
		PRICE.extend(price)







