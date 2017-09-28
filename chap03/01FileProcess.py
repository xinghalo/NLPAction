#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
raw = urlopen(url).read()

# 统计基本信息
print(type(raw))
print(len(raw))
print(raw[:75])

# 分词
tokens = nltk.word_tokenize(raw)[3:]
print(type(tokens))
print(len(tokens))
print(tokens[:10])

# 字符串转换成text
text = nltk.Text(tokens)
type(text)
print(text[1020:1060])

# 寻找字符的索引位置
print(raw.find("PART I"))
print(raw.rfind("End of Project Gutenberg's Crime"))