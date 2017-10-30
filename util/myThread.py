import threading

class MyThread(threading.Thread):
	def __init__(self, func):
		super(MyThread, self).__init__()
		self.func = func

	def run(self):
		self.func()


def id_spliter(itemId, n):
	l = len(itemId)
	lrange = range(l)
	itemList = []
	for i in range(n):
		itindex = [j for j in lrange if j%n ==i]
		itemList.append([itemId[i] for i in itindex])
		return itemList