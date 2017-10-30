#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu

'''
@Descripition
JD item comment crawler 2 - to crawl item comment information in JD

Update information:
- Multi-processing
- Real time write into MySQL

JD sets up 3-level categories for each listing item: firstCategory, secondCategory, thirdCategory,
which are encoded with distinct number respectively.
'''

import time, sys
from multiprocessing import Process,Queue
from crawler.JDItemCommentCrawl2 import startItemCommentCrawl
from db.dbLoader import itemComment_db_loader



if __name__ == '__main__':
	a = time.ctime()
	print 'Start at:', a
	q1 = Queue()
	q2 = Queue()
	p1 = Process(target = startItemCommentCrawl, args = (q1, q2))
	p2 = Process(target = itemComment_db_loader, args = (q2,))
	p1.start()
	p2.start()
	p1.join()
	#p2.join()
	time.sleep(100)
	p2.terminate()
	b = time.ctime()
	print 'All done at:', b