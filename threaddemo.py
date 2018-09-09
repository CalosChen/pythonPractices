#!/usr/bin/python

#!import: in this folder, there must be no file that matches the name of the builtin modules like threading, process,request, etc.
import time
import _thread

def task(name):
    print(name)


try:
    # _thread.start_new_thread(task,("no",))
except:
    print("wrong")

while 1:
    pass
        