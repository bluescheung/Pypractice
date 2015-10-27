#!usr/bin/env python3

import hashlib

db={}

def login(username,password):
    if db[username]==hashlib.md5().update((password+username+'the-Salt').encode('utf-8')).hexdigest():
        print('%s login!' % username)

def register(username,password):
    if username not in db:
        db[username]=hashlib.md5().update((password+username+'the-Salt').encode('utf-8')).hexdigest()
    else:
        login(username,password)

if __name__=='__main__':
    while True:
        username=input('input username:')
        password=input('input password:')
        register(username,password)
