#!usr/bin/env python3

f=open('variables.txt','r')
new=open('main.txt','w')
for k in f:
    if('main' in k):
        new.write(k)
f.close()
new.close()
