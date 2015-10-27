#!usr/bin/env python3
#-*- coding:utf-8 -*-

import asyncio,aiomysql

@asyncio.coroutine
def create_pool(pool,**kw):
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port','3306),
        user=kw['user'],
        passwd=kw['passwd'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )

@asyncio.coroutine
def select(sql,args,size=None):
    global __pool
    with (yield from __pool) as conn:
        cur=yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?','%s'),args or ())
        if size:
            rs=yield from cur.fetchmany(size)
        else:
            rs=yield from cur.fetchall()
        yield from cur.close()
    return rs

@classmethod
@asyncio.coroutine
def find(cls,pk):
    rs=yield from select('%s where `%s`=?' % (cls.__select__,cls.__primary_key__),[pk],1)
    if len(rs)==0:
        return None
    return cls(**rs[0])
