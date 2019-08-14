# coding=utf-8
import requests
import gevent
from gevent import monkey;monkey.patch_all()
from gevent.lock import Semaphore   #锁

#python自动化测试中如何使用协程
#案例1
def f1(a):
    for i in range(a):
        print 'f1 is ' + str(i)
        gevent.sleep(3)
def f2():
    for i in range(5):
        print 'f2 is ' + str(i)
        gevent.sleep(3)
g1=gevent.spawn(f1,a=10)
g2=gevent.spawn(f2)

gevent.joinall([g1,g2])





