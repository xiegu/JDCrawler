#!/usr/bin/python
# encoding: utf-8
import config, json, re
from bs4 import BeautifulSoup as bs

class HtmlParser(object):
	def parse(self, content, parser):
		if parser['func'] == 'fetchPageNum':
			return self.pageNumParser(content, parser)
		elif parser['func'] == 'fetchItem':
			return self.itemParser(content, parser)
		elif parser['func'] == 'fetchPrice':
			return self.priceParser(content, parser)
		elif parser['func'] == 'fetchHotSearch':
			return self.hotSearchParser(content, parser)
		elif parser['func'] == 'fetchHotSale':
			return self.hotSaleParser(content, parser)
		elif parser['func'] == 'fetchScore':
			return self.itemScoreParser(content, parser)
		elif parser['func'] == 'fetchComment':
			return self.itemCommentParser(content, parser)
		elif parser['func'] == 'fetchDetail':
			return self.itemDetailParser(content, parser)
		else:
			return None

	def pageNumParser(self, content, parser):
		htmlContent = bs(content)
		pageNum = htmlContent.find(parser['position']['pos'], parser['position']['class'])
		pageNum = int(pageNum.em.b.get_text())
		return pageNum

	def itemParser(self, content, parser):
		htmlContent = bs(content)
		items = htmlContent.find_all(parser['position']['pos'], parser['position']['class'])
		itemList = []
		for i in items:
			#category = c['category']
			id = i.find('div', re.compile('j-sku-item'))['data-sku']
			link = 'https:' + i.find_all('a')[0]['href']
			name = i.find('div', 'p-name').a.em.get_text().strip()
			itemList.append({'id': id, 'link': link, 'name': name})
		return itemList

	def priceParser(self, content, parser):
		try:
			price = json.loads(content)
			return price
		except ValueError:
			return None

	def hotSearchParser(self, content, parser):
		try:
			htmlContent = json.loads(content)
			search = htmlContent.get(parser['position'])
			return search
		except ValueError:
			return None

	def hotSaleParser(self, content, parser):
		try:
			htmlContent = json.loads(content)
			sale = htmlContent.get(parser['position'])
			return sale
		except ValueError:
			return None

	def itemScoreParser(self, content, parser):
		try:
			htmlContent = json.loads(content)
			score = htmlContent.get(parser['position'])
			return score
		except ValueError:
			return None

	def itemCommentParser(self, content, parser):
		try:
			htmlContent = json.loads(content)
			comment = htmlContent.get(parser['position'])
			return comment
		except ValueError:
			return None

	def itemDetailParser(self, content, parser):
		try:
			htmlContent = bs(content)
			brand = htmlContent.find_all(parser['position']['pos'], id=parser['position']['id'])[0].find('li')['title']
			name = htmlContent.find_all(parser['position2']['pos'], parser['position2']['class'])[0].find_all('li')[0]['title']
			id = htmlContent.find_all(parser['position2']['pos'], parser['position2']['class'])[0].find_all('li')[1]['title']
			detail = list()
			detail.append({'id': id, 'brand': brand, 'name': name})
			return detail
		except IndexError:
			#name = htmlContent.find_all(parser['position3']['pos'], parser['position3']['class'])[0].find_all('li')[0]['title'].split(' ')[0]
			id = 'NA'
			name = 'NA'
			brand = 'NA'
			detail = list()
			detail.append({'id': id, 'brand': brand, 'name': name})
			return detail
		except ValueError:
			return None
			
