#!/usr/bin/python3
#-*- coding:utf-8 -*-

from multiprocessing import Process,Pool
import time
import os
def task(name):
    print(name)
    time.sleep(2)

if __name__=="__main__":
    pool=Pool(3)
    pool.map(task,[1,2,3])
    pool.close()
    pool.join()