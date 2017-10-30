#!/usr/bin/python
# encoding: utf-8
from multiprocessing import Process, Queue
import os, time, random
 
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())
 
def read(q):
    while True:
            value = q.get(True)
            print 'Get %s from queue.' % value
            time.sleep(random.randint(2,3))
 
if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #pr.daemon = True
    # 启动子进程pw，写入:
    pw.start()    
    # 等待pw结束:
    
    # 启动子进程pr，读取:
    pr.start()
    pw.join()
    print '所有数据都写入'
    time.sleep(10)
    print 'sleep 10 secs'
    pr.terminate()
    print 'all done'
