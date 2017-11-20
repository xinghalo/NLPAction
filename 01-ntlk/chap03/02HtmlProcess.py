#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
print(html[:60])
'''
raw = nltk.clean_html(html)
tokens = nltk.word_tokenize(raw)
print(tokens)

tokens = tokens[96:399]
text = nltk.Text(tokens)
print(text.concordance('gene'))
'''
