#!/usr/bin/python3

import os
import re
import sys

fileName = "./lstext.txt"
oldString = "now"
newString = "yes"
fileStream = open(fileName, 'r')
content = fileStream.read()
print(content)
fileStream.close()
newContent = content.replace(oldString, newString)
print("---")
fileStream = open(fileName, 'w')
print(newContent)
fileStream.write(newContent)
fileStream.close()


def replaceString(dir, oldString, newString):
    if dir == ".":
        dir = os.getcwd()
        pass
    for root, dirs, files in os.walk(dir):
        for fileName in files:
            file = open(fileName, 'r')
            content = file.read()
            file.close()
            content = content.replace(oldString, newString)
            file = open(fileName, 'w')
            file.write(content)
            file.close()
            pass
        for dirName in dirs:
            replaceString(dirName, oldString, newString)

            pass
        pass
    pass
