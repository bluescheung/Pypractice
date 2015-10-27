#!usr/bin/env python3

import asyncio,aiomysql

@asyncio.coroutine
def execute(sql,args,autocommit=Ture):
    with (yield from __pool) as conn:
        if not autocommit:
            yield from conn.begin()
        try:
            cur=yield from conn.cursor()
            yield from cur.execute(sql.replace('?',%s'),args)
            affected=cur.rowcount
            yield from cur.close()
            if not autocommit:
                yield from conn.commit()
        except BaseException as e:
            if not autocommit:
                yield from conn.rollback()
            raise
        return affected

@asyncio.coroutine
def save(self):
    args=list(map(self.getValueOrDefault,self.__fields__))
    args.append(self.getValueOrDefault(self.__primary_key__))
    rows=yield from execute(self.__insert__,args)
    if rows!=1:
        print('...')

@asyncio.coroutine
def update(self):
    args=list(map(self.getValue,self.__fields__))
    args.append(self.getValue(self.__primary_key__))
    rows=yield from execute(self.__update__,args)
    if rows!=1:
        print('....')

@asyncio.coroutine
def remove(self):
    args=[self.getValue(self.__primary_key__)]
    rows=yield from execute(self.__delete__,args)
    if rows!=1:
        print('...')
