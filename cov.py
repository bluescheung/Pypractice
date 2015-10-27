#!usr/bin/env python3

out=open('read.txt','w')
f=open('readme.txt','r')
out.write(f.read().encode('utf-8'))
