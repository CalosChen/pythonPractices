#!/usr/bin/python3
#--encoding-utf-8--

import os, sys, re

print("Hello world!")
quit= False

print(len(sys.argv))
print(sys.argv[1])

def rename(dir,oldString,newString):
    for root, dirs, files in os.walk(dir):
        for fileName in files:
            fileStream=open(fileName)
            content=fileStream.read()
            reg=re.compile(oldString)
            content=reg.sub(newString,content)
            fileStream.write(content)
            fileStream.close()



            
            








