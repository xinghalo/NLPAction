#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# old style
tokens = nltk.corpus.brown.words(categories='news')
count = 0
total = 0
for token in tokens:
    count += 1
    total += len(token)
print total / count

# new style
total = sum(len(t) for t in tokens)
print total / len(tokens)

# 范围变量
sent = ['the','dog','gave','john','the','newspaper']
n = 3
print [sent[i:i+n] for i in range(len(sent)-n+1)]

m,n = 3,7
array = [[set() for i in range(n)] for j in range(m)]
array[2][5].add('Alice')
pprint.pprint(array)

array = [[set()] * n ] * m
array[2][5].add(7)
pprint.pprint(array)