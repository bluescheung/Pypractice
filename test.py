#!/usr/bin/python

import re
"""
pat = re.compile(r'\S*\s+\S*\s+(\d+)\s+\S*')

sum = 0
for line in open('pagehead'):
  sum = sum + 

print sum
"""



pat = re.compile(r'\S*\s+\S*\s+(\d+)\s+\S*')
print sum([int(pat.match(line).groups()[0]) for line in open('pagehead')])
