#!usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con=lite.connect('system.db')

with con:
    
    cur=con.cursor()
    cur.execute("select users.name,jobs.profession from jobs inner join users on users.id=jobs.uid")
    rows=cur.fetchall()
    
    for row in rows:
        print(row)
