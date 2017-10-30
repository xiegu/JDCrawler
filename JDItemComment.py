#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

import time, sys, Queue
from crawler.JDItemCommentCrawl import JDItemCommentCrawler
from db.dbLoader import itemComment_db_loader



if __name__ == '__main__':
	a = time.ctime()
	print 'Start at:', a
	q1 = Queue.Queue()
	q2 = Queue.Queue()
	crawler = JDItemCommentCrawler(q1,q2)
	crawler.run()
	itemComment_db_loader(q2)
	b = time.ctime()
	print 'All done at:', b