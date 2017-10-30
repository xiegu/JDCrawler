#!/usr/bin/python
# encoding: utf-8

from db.sqlHelper import CatItemSqlHelper, HotSearchSqlHelper, HotSaleSqlHelper, ItemScoreSqlHelper, ItemCommentSqlHelper, ItemDetailSqlHelper
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def catItem_db_loader(queue2):
	sqlhelper = CatItemSqlHelper()
	sqlhelper.init_db()
	successNum = 0
	failNum = 0
	while not queue2.empty():
		try:
			item = queue2.get()
			if item:
				sqlhelper.insert(item)
				successNum += 1
			else:
				failNum += 1
		except Exception as e:
			raise e
	print 'Successfully inserted %d records, and %d records failed to load' %(successNum, failNum)


def hotSearch_db_loader(queue1):
	sqlhelper = HotSearchSqlHelper()
	sqlhelper.init_db()
	successNum = 0
	failNum = 0
	while not queue1.empty():
		try:
			keyword = queue1.get()
			if keyword:
				sqlhelper.insert(keyword)
				successNum += 1
			else:
				failNum += 1
		except Exception as e:
			raise e
	print 'Successfully inserted %d records, and %d records failed to load' %(successNum, failNum)

def hotSale_db_loader(queue1):
	sqlhelper = HotSaleSqlHelper()
	sqlhelper.init_db()
	successNum = 0
	failNum = 0
	while not queue1.empty():
		try:
			sale = queue1.get()
			if sale:
				sqlhelper.insert(sale)
				successNum += 1
			else:
				failNum += 1
		except Exception as e:
			raise e
	print 'Successfully inserted %d records, and %d records failed to load' %(successNum, failNum)

def itemScore_db_loader(queue2):
	sqlhelper = ItemScoreSqlHelper()
	sqlhelper.init_db()
	successNum = 0
	failNum = 0
	while not queue2.empty():
		try:
			score = queue2.get()
			if score:
				sqlhelper.insert(score)
				successNum += 1
			else:
				failNum += 1
		except Exception as e:
			raise e
	print 'Successfully inserted %d records, and %d records failed to load' %(successNum, failNum)

def itemComment_db_loader(queue2):
	sqlhelper = ItemCommentSqlHelper()
	sqlhelper.init_db()
	successNum = 0
	failNum = 0
	#print 'is %d' %queue2.qsize()
	#while not queue2.empty(): for commentcrawl1
	while True: # for commmentcrawl2
		try:
			comment = queue2.get()
			if comment:
				sqlhelper.insert(comment)
				successNum += 1
			else:
				failNum += 1
		except Exception as e:
			raise e
	print 'Successfully inserted %d records, and %d records failed to load' %(successNum, failNum)

def itemDetail_db_loader(queue2):
	sqlhelper = ItemDetailSqlHelper()
	sqlhelper.init_db()
	successNum = 0
	failNum = 0
	while not queue2.empty():
		try:
			detail = queue2.get()
			if detail:
				sqlhelper.insert(detail)
				successNum += 1
			else:
				failNum += 1
		except Exception as e:
			raise e
	print 'Successfully inserted %d records, and %d records failed to load' %(successNum, failNum)