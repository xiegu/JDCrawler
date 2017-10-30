#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

import time, sys, Queue
from crawler.JDHotInfoCrawl import JDHotSearchCrawler
from db.dbLoader import hotSearch_db_loader



if __name__ == '__main__':
	a = time.ctime()
	print 'Start at:', a
	q1 = Queue.Queue()
	crawler = JDHotSearchCrawler(q1)
	crawler.run()
	hotSearch_db_loader(q1)
	b = time.ctime()
	print 'All done at:', b
	