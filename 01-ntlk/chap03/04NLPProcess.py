#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 读取原始文本
raw = open('document.txt').read()
print(type(raw))

# 分词
tokens = nltk.word_tokenize(raw)
print(type(tokens))

# 小写转换
words = [w.lower() for w in tokens]
print(type(words))

# 词典排序
vocab = sorted(set(words))
print(type(vocab))