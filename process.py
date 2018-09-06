#!/usr/bin/python3
#-*- coding:utf-8 -*-

from multiprocessing import Process
import os
import time
print(__name__)
print(__file__)
print(time.time())
print(time.strftime("%Y:%m:%d",time.localtime()))

def task(name):
    print(name)

if __name__=="__main__":
    for i in range(2):
        p=Process(target=task,args=(str(i),))
        p.start()
    p.join()
# def run_proc(name):
#   print('Child process {0} {1} Running '.format(name, os.getpid()))
# if __name__ == '__main__':
#   print('Parent process {0} is Running'.format(os.getpid()))
#   for i in range(5):
#     p = Process(target=run_proc, args=(str(i),))
#     print('process start')
#     p.start()
#   p.join()
#   print('Process close')
