#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 词形归并
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
 is no basis for a system of government. Supreme executive power derives from 
 a mandate from the masses, not from some farcical aquatic ceremony.
"""
tokens = nltk.word_tokenize(raw)
print tokens

# stemmer 去梗机 —— 词干提取
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

# 可以看到Porter的效果更好一点
print [porter.stem(t) for t in tokens]
print [lancaster.stem(t) for t in tokens]

# 词形归并
wnl = nltk.WordNetLemmatizer()
print [wnl.lemmatize(t) for t in tokens]