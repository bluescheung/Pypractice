#!usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con=lite.connect('system.db')

with con:

    cur=con.cursor()
    cur.execute("create table users(id int,name text)")
    cur.execute("insert into users values(1,'Michelle')")
    cur.execute("insert into users values(2,'Howard')")
    cur.execute("insert into users values(3,'Greg')")

    cur.execute("create table jobs(id int,uid int,profession text)")
    cur.execute("insert into jobs values(1,1,'Scientist')")
    cur.execute("insert into jobs values(2,2,'Marketeer')")
    cur.execute("insert into jobs values(3,3,'Developer')")
