#!/usr/bin/python3

import module1
import sys,os,re
module1.hello()

greeting=input()
name=sys.stdin.readline()
print('%s%s'%(greeting,name,))
sys.stdout.write(name)
arg1=sys.argv[1]
print(arg1)