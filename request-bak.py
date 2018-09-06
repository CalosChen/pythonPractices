#!/usr/bin/python3
# -*- coding:utf-8 -*-

# assue that we want to download a page, then, we can get data from the certain page with request from urllib module, then read and decode the data
from urllib import request, parse

url="http://caloch.cn"
with request.urlopen(url) as stream:
    data=stream.read()
    print(data)
    html=data.decode("utf-8")
    print(html)