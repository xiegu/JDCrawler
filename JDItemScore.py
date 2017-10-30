#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

import time, sys, Queue
from crawler.JDItemScoreCrawl import JDItemScoreCrawler
from db.dbLoader import itemScore_db_loader



if __name__ == '__main__':
	a = time.ctime()
	print 'Start at:', a
	q1 = Queue.Queue()
	q2 = Queue.Queue()
	crawler = JDItemScoreCrawler(q1,q2)
	crawler.run()
	itemScore_db_loader(q2)
	b = time.ctime()
	print 'All done at:', b