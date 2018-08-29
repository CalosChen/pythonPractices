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