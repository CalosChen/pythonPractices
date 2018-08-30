#!/usr/bin/python3
import re
 
slogan="I like to be good"
matches=re.match(r'(.*) (.*).*',slogan,re.M|re.I)
if matches:
    print(matches.group())
    print(matches.group(1))
    pass
else:
    print("No match!")
    pass

alist=[1,2,3,4]
adict={"a":1,"b":2,"c":3}
aset=set()
aset={1,3,4}
aturple=(1,2,3)

print(aset)