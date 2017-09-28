#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 函数当作参数
sent = ['take', 'care', 'of','sense']

def extract_property(prop):
    return [prop(word) for word in sent]
print extract_property(len)

def last_letter(word):
    return word[-1]
print extract_property(last_letter)

# lambda表达式
print extract_property(lambda w:w[-1])

print sorted(sent)
print sorted(sent,cmp)
print sorted(sent,lambda x,y: cmp(len(y),len(x)))

# 生成器
list1 = [x*x for x in range(3)]
print list1
list2 = (x*x for x in range(3))
print list2
# list2是内存地址，用的时候才会取，不用的话，就不会计算
for i in list2:
    print (i)

# 累计函数
print
list = [5,3,6,9,7,8,11]
def get_max(list):
    max = 0
    for x in list:
        if x > max:
            yield x
            max = x

for n in get_max(list):
    print n

# 高阶函数

# filter()
def is_content_word(word):
    return word.lower() not in ['a','of']
sent = ['Take','a','of','and']
print filter(is_content_word,sent)
print [w for w in sent if is_content_word(w)]

# map()
lengths = map(len, nltk.corpus.brown.sents(categories='news'))
print sum(lengths) / len(lengths)

lengths = [len(w) for w in nltk.corpus.brown.sents(categories='news')]
print sum(lengths) / len(lengths)

print map(lambda w:len(filter(lambda c:c.lower() in "aeiou",w)),sent)
print [len([c for c in w if c.lower() in "aeiou"]) for w in sent]

# 默认参数
def repeat(msg='<empty>', num=1):
    return msg*num

print repeat(num=3)
print repeat(msg='hello')

def generic(*args, **kwargs):
    print args
    print kwargs

generic(1,"African",1,2,3,monty="python",test=1,test2=3)