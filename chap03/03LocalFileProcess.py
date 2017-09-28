#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 读取本地文件
f = open('document.txt')
raw = f.read()
print(raw)

import os
print(os.listdir('.'))

# 读取本地文件，但是没好使
f = open('document.txt','rU')
for line in f:
    print(line)

# 读取nltk语料库中的文本
path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
print(path)
raw = open(path,'rU').read()
print(raw[:100])