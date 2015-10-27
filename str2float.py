#!usr/bin/env python3
from functools import reduce
from math import pow
def str2float(s):
    if  s.find('.')>-1:
        sign = s.index('.')
        s=s.replace('.','')
    else:
        s=0
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))/pow(10,sign)

print ('str2float(\'123.456\')=',str2float('123.456'))
