#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

raw = """When I'm a Duchess, she said to herself, (not in a very hopeful
    though),' I won't
"""
print re.split(r' ', raw)
print re.split(r'[ \t\n]+', raw)
print re.split(r'\s+', raw)
print re.split(r'\W+', raw)
print re.findall(r"\w+(?:[-']\w+)*|'[-.(]+|\S\w*", raw)

# todo 这个表达式不太理解
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x)
      ([A-Z]\.)+          # 关键词缩写 U.S.A
    | \w+(-\w+)*        # 
    | \$?\d+(\.\d+)?%?  # 百分比，金额
    | \.\.\.            #
    | [][.,;'"?():-_`]  # 分隔符
'''
print nltk.regexp_tokenize(text, pattern)