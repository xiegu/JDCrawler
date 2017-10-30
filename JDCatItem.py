#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

import time, sys, Queue
from crawler.JDCatItemCrawl import JDCatItemCrawler
from db.dbLoader import catItem_db_loader



if __name__ == '__main__':
	a = time.ctime()
	print 'Start at:', a
	q1 = Queue.Queue()
	q2 = Queue.Queue()
	crawler = JDCatItemCrawler(q1,q2)
	crawler.run()
	catItem_db_loader(q2)
	b = time.ctime()
	print 'All done at:', b
	