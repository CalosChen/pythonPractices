#!/usr/bin/python

import time
import _thread

def task(name):
    print(name)


try:
    _thread.start_new_thread(task,("help",))
except:
    print("wrong")

while 1:
    pass
        