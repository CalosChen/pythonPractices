#!/usr/bin/python3

import module1
import sys,os,re,pymysql
module1.hello()

greeting=input()
name=sys.stdin.readline()
print('%s%s'%(greeting,name,))
sys.stdout.write(name)
arg1=sys.argv[1]
print(arg1)

db=pymysql.connect('localhost','root','cst','test')
cursor=db.cursor()
cursor.execute('select * from table1')
rs=cursor.fetchall()
for row in rs:
    print('%s %s'%(row[0],row[1],))
db.close()