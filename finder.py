#!usr/bin/env python3
'search'
author = 'ZZD'

import os

def myfind(pattern,root='.'):
    for each in os.listdir(root):
        if os.path.isdir(os.path.join(root,each)):
            myfind(pattern,os.path.join(root,each))
        if pattern in str(each):
            print(os.path.join(root,each))
