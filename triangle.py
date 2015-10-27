#!usr/bin/env python3
def triangles():
    a=[1]
    yield a
    while True:
        a.insert(0,0)
        a.append(0)
        l=len(a)
        L=[]
        for i in range(l):
            if i<l-1:
                L.append(a[i]+a[i+1])
        yield L
        a=L
n=0
for t in triangles():
    print (t)
    n=n+1
    if n==10:
        break
