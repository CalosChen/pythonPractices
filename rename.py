#!/usr/bin/python3
#--encoding-utf-8--

import env, os, sys, re

print("Hello world!")
quit= False

def rename(dir,oldString,newString):
    for root, dirs, files in os.walk(dir):
        for fileName in files:
            fileStream=open(fileName)
            content=fileStream.read()
            reg=re.compile(oldString)
            content=reg.sub(newString,content)
            fileStream.write(content)
            fileStream.close()


            
            








