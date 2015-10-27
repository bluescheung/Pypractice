#!usr/bin/env python3
import os

def dir():
    L= [ x for x in os.listdir('.') if os.path.isdir(x)]
    for i in L:
        print i

dir()
