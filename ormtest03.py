#!usr/bin/env python3

import asyncio,aiomysql

class ModelMetaclass(type):
    def __new__(clas,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
    tableName=attrs.get('__table__',None) or name
    mappings=dict()
    fields[]
    primaryKey=None
    for k,v int attrs.item():
        if isinstance(v,Field):
            mapping[k]=v
        if v.primary_key:
            if primaryKey:
                raise StandardError('Duplicate')
            primaryKey=k
        else:
            fields.append(k)
    for k in mappings.keys():
        attrs.pop(k)
    escaped_fields=list(map(lambda:f:'`%s`' % f,fields))
    attrs['__mappings__']=mappings
    attrs['__table__']=tableName
    attrs['__primary_key__']=primaryKey
    attrs['__fields__']=fields
    attrs['__select__']='select `%s`,%s from `%s`' % (primaryKey,','.join(escaped_fields),tableName)
    attrs['__insert__']='insert into `%s` (%s,`%s`) values (%s)' % (tableName,','.join(escaped_fields),primaryKey,create_args_string(len(escaped_fields)))
    attrs['__update__']='update `%s` set %s where `%s`=?' % (tableName,','.join(map(lambda f:'`%s`=?' % (mappings.get(f).name or f),fields)),primaryKey)
    attrs['__delete__']='delete from `%s` where `%s`=?' % (tableName,primaryKey)
    return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value
    def getValue(self,key):
        return getattr(self,key,None)
    def getValueOrDefault(self,key):
        value=getattr(self,key,None)
        if value is None:
            field=self.__mappings__[key]
            if field.default is not None:
                value=field.default() if callable(field.default) else field.default
            setattr(self,key,value)
    return value
    
