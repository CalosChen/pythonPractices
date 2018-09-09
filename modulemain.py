#!/usr/bin/python3

import module1
import sys,os,re,pymysql
module1.hello()

# greeting=input()
# name=sys.stdin.readline()
# print('%s%s'%(greeting,name,))
# sys.stdout.write(name)
arg1=sys.argv[1]
print(arg1)

db=pymysql.connect('localhost','root','cst','test')
cursor=db.cursor()
cursor.execute('select * from table1')
rs=cursor.fetchall()
for row in rs:
    print('%s %s'%(row[0],row[1],))
db.close()

aset=(1,2,3,6,5,)
adict={'a':5,'b':3}
alist=[1,2,4,5]
for el in aset:
    print(el)
for el in adict:
    print(adict[el])

try:
    print(1)
except:
    print(2)
finally:
    print('final')
i=5
while i>2:
    print(i)
    i=i-1
print('looped')

class Base:
    def __init__(self,id):
        self.id=id
    def show(self):
        print(self.id)
base=Base(2)
base.show()
