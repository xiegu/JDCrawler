#!/usr/bin/python
# encoding: utf-8

#@author Xiecheng Gu


import datetime
from sqlalchemy import Column, Integer, DateTime, Numeric, create_engine, VARCHAR, TEXT, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG

from db.IsqlHelper import ISqlHelper



BaseModel = declarative_base()

class ItemDetail(BaseModel):
	__tablename__ = 'JD_item_detail'
	row_num = Column(Integer, primary_key = True, autoincrement = True)
	id = Column(VARCHAR(20), nullable = False)
	brand = Column(TEXT, nullable = True)
	name = Column(TEXT, nullable = True)
	#category = Column(VARCHAR(20), nullable = False)
	update_time = Column(DateTime(), default = datetime.datetime.today)

class ItemComment(BaseModel):
	__tablename__ = 'JD_item_comment'
	row_num = Column(Integer, primary_key = True, autoincrement = True)
	id = Column(VARCHAR(20), nullable = False)
	reference_id = Column(VARCHAR(20), nullable = False)
	#category = Column(VARCHAR(20), nullable = False)
	content = Column(TEXT)
	creation_time = Column(DateTime(), nullable = False)
	image_count = Column(Integer, nullable = True)
	is_mobile = Column(Integer, nullable = True)
	nick_name = Column(VARCHAR(30), nullable = False)
	plus_available = Column(Integer, nullable = True)
	product_color = Column(TEXT, nullable = True)
	product_size = Column(TEXT, nullable = True)
	reference_name = Column(VARCHAR(300), nullable = True)
	reference_time = Column(DateTime(), nullable = True)
	score = Column(Integer, nullable = False)
	first_category = Column(Integer, nullable = False)
	second_category = Column(Integer, nullable = False)
	third_category = Column(Integer, nullable = False)
	useful_vote_count = Column(Integer, nullable = True)
	useless_vote_count = Column(Integer, nullable = True)
	user_client = Column(Integer, nullable = True)
	user_client_show = Column(VARCHAR(30), nullable = True)
	user_exp_value = Column(Integer, nullable = True)
	user_level_id = Column(Integer, nullable = True)
	user_level_name = Column(VARCHAR(20), nullable = True)
	update_time = Column(DateTime(), default = datetime.datetime.today)

class ItemScore(BaseModel):
	__tablename__ = 'JD_item_score_summary'
	row_num = Column(Integer, primary_key = True, autoincrement = True)
	sku_id = Column(VARCHAR(20), nullable = False)
	category = Column(VARCHAR(20), nullable = False)
	average_score = Column(Numeric(3,1))
	comment_count = Column(Integer)
	general_count = Column(Integer)
	general_rate = Column(Numeric(5,3))
	good_count = Column(Integer)
	good_rate = Column(Numeric(5,3))
	poor_count = Column(Integer)
	poor_rate = Column(Numeric(5,3))
	score1_count = Column(Integer)
	score2_count = Column(Integer)
	score3_count = Column(Integer)
	score4_count = Column(Integer)
	score5_count = Column(Integer)
	show_count = Column(Integer)
	update_time = Column(DateTime(), default = datetime.datetime.today)

class HotSale(BaseModel):
	__tablename__ = 'JD_hot_sale_info'
	row_num = Column(Integer, primary_key = True, autoincrement = True)
	id = Column(VARCHAR(20), nullable = False)
	name = Column(VARCHAR(300), nullable = False)
	category = Column(VARCHAR(20), nullable = False)
	update_time = Column(DateTime(), default = datetime.datetime.today)

class HotSearch(BaseModel):
	__tablename__ = 'JD_hot_search_info'
	row_num = Column(Integer, primary_key = True, autoincrement = True)
	catCode = Column(Integer, nullable = False)
	category = Column(VARCHAR(20), nullable = False)
	word = Column(VARCHAR(40), nullable = False)
	count = Column(Integer, nullable = False)
	update_time = Column(DateTime(), default = datetime.datetime.today) #local time

class CatItem(BaseModel):
	__tablename__ = 'JD_cat_item_info'
	row_num = Column(Integer, primary_key = True, autoincrement = True)
	id = Column(VARCHAR(20), nullable = False)
	category = Column(VARCHAR(20), nullable = False)
	name = Column(VARCHAR(300), nullable = False)
	link = Column(VARCHAR(60), nullable = False)
	m = Column(Numeric(8,1))
	op = Column(Numeric(8,1))
	p = Column(Numeric(8,1))
	update_time = Column(DateTime(), default = datetime.datetime.today) #local time


class ItemDetailSqlHelper(ISqlHelper):

	def __init__(self):
		# mysql
		self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'])
		DBSession = sessionmaker(bind = self.engine)
		self.session = DBSession()

	def init_db(self):
		BaseModel.metadata.create_all(self.engine)

	def drop_db(self):
		BaseModel.metadata.drop_all(self.engine)

	def insert(self, value):
		detail = ItemDetail(id = value['id'], brand = value.get('brand'), name = value.get('name'))
		self.session.add(detail)
		self.session.commit()

	def select(self):
		pass

	def close(self):
		pass

class ItemCommentSqlHelper(ISqlHelper):

	def __init__(self):
		# mysql
		self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'])
		DBSession = sessionmaker(bind = self.engine)
		self.session = DBSession()

	def init_db(self):
		BaseModel.metadata.create_all(self.engine)
	
	def drop_db(self):
		BaseModel.metadata.drop_all(self.engine)

	def insert(self, value):
		score = ItemComment(id = value['id'], reference_id = str(value['referenceId']), content = value['content'], #category = value['category'],
							creation_time = value['creationTime'], image_count = value.get('imageCount'), is_mobile = value.get('isMobile'),
							nick_name = value['nickname'], plus_available = value.get('plusAvailable'), product_color = value.get('productColor'),
							product_size = value.get('productSize'), reference_name = value.get('referenceName'), reference_time = value.get('referenceTime'),
							score = value['score'], first_category = value['firstCategory'], second_category = value['secondCategory'],
							third_category = value['thirdCategory'], useful_vote_count = value.get('usefulVoteCount'), useless_vote_count = value.get('uselessVoteCount'),
							user_client = value.get('userClient'), user_client_show = value.get('userClientShow'), user_exp_value = value.get('userExpValue'),
							user_level_id = value.get('userLevelId'), user_level_name = value.get('userLevelName'))
		self.session.add(score)
		self.session.commit()

	def select(self):
		pass

	def close(self):
		pass

class ItemScoreSqlHelper(ISqlHelper):

	def __init__(self):
		# mysql
		self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'])
		DBSession = sessionmaker(bind = self.engine)
		self.session = DBSession()

	def init_db(self):
		BaseModel.metadata.create_all(self.engine)
	
	def drop_db(self):
		BaseModel.metadata.drop_all(self.engine)

	def insert(self, value):
		score = ItemScore(sku_id = str(value['SkuId']), category = value['category'], average_score = value['AverageScore'],
							comment_count = value['CommentCount'], general_count = value['GeneralCount'],
							general_rate = value['GeneralRate'], good_count = value['GoodCount'], good_rate = value['GoodRate'],
							poor_count = value['PoorCount'], poor_rate = value['PoorRate'], score1_count = value['Score1Count'],
							score2_count = value['Score2Count'], score3_count = value['Score3Count'], score4_count = value['Score4Count'],
							score5_count = value['Score5Count'], show_count = value['ShowCount'])
		self.session.add(score)
		self.session.commit()

	def select(self):
		pass

	def close(self):
		pass

class HotSaleSqlHelper(ISqlHelper):
	#params = {'word': HotSearch.word, 'count': HotSearch.count}

	def __init__(self):
		# mysql
		self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'])
		DBSession = sessionmaker(bind = self.engine)
		self.session = DBSession()

	def init_db(self):
		BaseModel.metadata.create_all(self.engine)
	
	def drop_db(self):
		BaseModel.metadata.drop_all(self.engine)

	def insert(self, value):
		sale= HotSale(id = value['wareId'], name = value['wareName'], category = value['category'])
		self.session.add(sale)
		self.session.commit()

	def select(self):
		pass

	def close(self):
		pass

class HotSearchSqlHelper(ISqlHelper):
	#params = {'word': HotSearch.word, 'count': HotSearch.count}

	def __init__(self):
		# mysql
		self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'])
		DBSession = sessionmaker(bind = self.engine)
		self.session = DBSession()

	def init_db(self):
		BaseModel.metadata.create_all(self.engine)
	
	def drop_db(self):
		BaseModel.metadata.drop_all(self.engine)

	def insert(self, value):
		keyword = HotSearch(catCode = value['catCode'], category = value['category'], word = value['keyString'], count = int(value['keyCount']))
		self.session.add(keyword)
		self.session.commit()

	def select(self):
		pass

	def close(self):
		pass


class CatItemSqlHelper(ISqlHelper):
	params = {'id': CatItem.id, 'category': CatItem.category, 'name': CatItem.name, 'link': CatItem.link, 
				'm': CatItem.m, 'op': CatItem.op, 'p': CatItem.p}

	def __init__(self):
		# mysql
		self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'])
		DBSession = sessionmaker(bind = self.engine)
		self.session = DBSession()

	def init_db(self):
		BaseModel.metadata.create_all(self.engine)

	def drop_db(self):
		BaseModel.metadata.drop_all(self.engine)

	def insert(self, value):
		item = CatItem(id = value['id'], category = value['category'], name = value['name'],
						link = value['link'], m = value['m'], op = value['op'],
						p = value['p'])
		self.session.add(item)
		self.session.commit()

	def delete(self, conditions = None):
		if conditions:
			condition_list = []
			for key in list(conditions.keys()):
				if self.params.get(key, None):
					condition_list.append(self.params.get(key) == conditions.get(key))
			conditions = condition_list
			query = self.session(CatItem)
			for condition in conditions:
				query = query.filter(condition)
			deleteNum = query.delete()
			self.session.commit()
		else:
			deleteNum = 0
		return 'deleteNum %d' %deleteNum

	def update(self, conditions = None, value = None):
		if conditions and value:
			condition_list = []
			for key in list(conditions,keys()):
				if self.params.get(key, None):
					condition_list.append(self.params.get(key) == conditions.get(key))
			conditions = condition_list
			query = self.session.query(CatItem)
			for condition in conditions:
				query = query.filter(condition)
			updatevalue = {}
			for key in list(value.keys()):
				if self.params.get(key, None):
					updatevalue[self.params.get(key, None)] = value.get(key)
			updateNum = query.update(updatevalue)
			self.session.commit()
		else:
			updateNum = 0
			return 'updateNum %d' %updateNum

	def select(self, count = None):
		query = self.session.query(CatItem.id, CatItem.category)
		if count:
			return query.limit(count).all()
		else:
			return query.all()


	def close(self):
		pass

if __name__ == '__main__':
	sqlhelper = SqlHelper()
	sqlhelper.init_db()
	item = {'id': 112339645, 'category': 'air', 'name': 'airconditioner',
					'link': 'www.google.com', 'm': 1233, 'op': 1234, 
					'p': 3333}
	sqlhelper.insert(item)
	print 'done'



		