#!usr/bin/env python3
from functools import reduce
def normalize(name):
    if not str.isalpha(name):
        pass
    else:
        return  name.capitalize()

L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
L3=['123','22','abc']
L4=list(map(normalize,L3))
print(L2)
print(L4)

def prod(L):
    def product(x,y):
        return x*y
    return reduce(product,L)

P=prod([1,2,3,4,5,6])
print (P)
