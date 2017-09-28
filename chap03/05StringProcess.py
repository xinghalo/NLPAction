#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 单行输出
monty = 'Month Python'
print(monty)

circus = "Month Python's Flying Circus"
print(circus)

circus = 'Month Python\'s Flying Circus'
print(circus)

# 多行输出
couplet = "Shall I compare thee to a Summer's day?"\
    "Thou are more lovely..."
print(couplet)

couplet = ("Shall I compare thee to a Summer's day?",
    "Thou are more lovely...")
print(couplet)

couplet = """
Shall I compare thee to a Summer's day?
Thou are more lovely...
"""
print(couplet)

couplet = '''
Shall I compare thee to a Summer's day?
Thou are more lovely...
'''
print(couplet)

# 字符串的拼接和乘法
a = [1,2,3,4,5,6,7,6,5,4,3,2,1]
b = [' '*2*(7-i)+'very' for i in a]
for line in b:
    print(line)

# 输出信息
print monty

# 拼接输出
grail = 'Holy Grail'
print monty + grail

print monty, grail

print monty, "and the", grail

# 访问单个字符串
print monty[0]
print monty[3]
# print monty[5]
# print monty[20]

print monty[-1]
# print monty[-20]

sent = 'colorless green ideas sleep furiously'
for char in sent:
    print char,

from nltk.corpus import gutenberg
raw = gutenberg.raw('melville-moby_dick.txt')
# print raw[:100]
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
print fdist.keys()

# 字符串切片
phrase = 'And now for something complete different'
if 'thing' in phrase:
    print 'found thing'

print monty.find('Python')

# 字符串方法
print 'hello'.find('e')
print 'hello'.rfind('e')
print 'hello'.index('e')
print 'hello'.rindex('e')
print 'hello'.join('world')
print 'hello, world'.split(',')
print 'hello, \nwor\nld\n'.splitlines()
print 'hello, \nwor\nld\n'.splitlines(True) # 是否保留换行符
print 'Hello'.lower()
print 'Hello'.upper()
# print 'Hello'.titlecase()
print 'Hello    '.strip()
print 'Hello'.replace('l','a')

# 链表与字符串的差异
query = 'Who knows?'
beatles = ['John', 'Paul', 'George', 'Ringo']
print query[2]
print beatles[2]
print query[:2]
print beatles[:2]
print query + " I don't"
print beatles + ['Brian']
beatles[0] = "John Lennon"
print beatles
del beatles[-1]
print beatles

# query[0]='F'
# print query