#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

'''
@Descripition
JD hot info crawler - to crawl hot sales item and hot search keywords in JD
JD sets up 3-level categories for each listing item: firstCategory, secondCategory, thirdCategory,
which are encoded with distinct number respectively.
'''

import sys
import config
from config import get_topSale_url, get_topSearch_url
from crawler.htmlDownloader import HtmlDownloader
from crawler.htmlParser import HtmlParser

reload(sys)
sys.setdefaultencoding('utf8')


class JDHotSearchCrawler(object):
	def __init__(self, queue1):
		self.queue1 = queue1

	def run(self):
		# while True: update every Monday in plan
		print 'Start crawling hot search words in category' + ' ' + '>'*20
		search = self.hotSearchCrawler(config.parserList[3])
		for i in search:
			if i is not None:
				self.queue1.put(i)

	def hotSearchCrawler(self, parser):
		html_parser = HtmlParser()
		wordList = []
		for c in config.searchList:
			while True:
				content = HtmlDownloader.download(get_topSearch_url(c['code']))
				if content is not None:
					keyword = html_parser.parse(content, parser)
					for i in range(len(keyword)):
						keyword[i]['catCode'] = c.get('code')
						keyword[i]['category'] = c.get('category')
					break
				else:
					time.sleep(5)
					continue
			wordList.extend(keyword)
		return wordList

class JDHotSaleCrawler(object):
	def __init__(self, queue1):
		self.queue1 = queue1

	def run(self):
		# while True: update every Monday in plan
		print 'Start crawling hot sale item in category' + ' ' + '>'*20
		sale = self.hotSaleCrawler(config.parserList[4])
		for i in sale:
			if i is not None:
				self.queue1.put(i)

	def hotSaleCrawler(self, parser):
		html_parser = HtmlParser()
		saleList = []
		for c in config.catList:
			while True:
				content = HtmlDownloader.download(get_topSale_url(c['code'][2]))
				if content is not None:
					sale = html_parser.parse(content, parser)
					for i in range(len(sale)):
						sale[i]['category'] = c.get('category')
					break
				else:
					time.sleep(5)
					continue
			saleList.extend(sale)
		return saleList
