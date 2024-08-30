#!/usr/bin/python3
#Arguments of command line
#1 - name
#2 - date and time

import datetime
import os
import getpass
import math
import sys

path="/"
#path="/bin/" 

if not os.path.exists(path):
    path='/'

fnames=os.listdir(path)
count=len(fnames)
fsizes=[math.ceil((os.path.getsize(path+fnames[i]))/1024) for i in range(0,count)]
ffull=[(x,y) for x in fnames for y in fsizes]
ffull=[]
for i in range(0,count):
    ffull.append((fnames[i],fsizes[i]))
sorted_ffull=sorted(ffull,key=lambda item:item[1],reverse=True)

if  len(sys.argv)<2:
    print("Hello, "+getpass.getuser()+"!")
else:
    print("Hello, "+sys.argv[1])
if len(sys.argv)<3:
    print("Current time:",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
else:
    print("Current time:",sys.argv[2])
print("Total number of files:",count)
print("Top 10 largest files (inKB):")
for i in range(0,10):
    print(path+sorted_ffull[i][0]+":",sorted_ffull[i][1],"KB")


