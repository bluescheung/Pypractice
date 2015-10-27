#!usr/bin/env python3

import struct

def Judge(name):
    with open(name,'rb') as f:
        h=f.read(30)
    L=[]
    for i in struct.unpack('<ccIIIIIIHH',name):
        L.append(i)
    if L[0]==b'B' and L[1]==b'M' or L[1]==b'A':
        print(L[6]+'x'+L[7]+'@'+L[9])
    else:
        print('this is not a bmp pic') 
