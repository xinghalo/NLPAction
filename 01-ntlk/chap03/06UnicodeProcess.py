#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 读取文件
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
import codecs
f = codecs.open(path,encoding='latin2')
print f

for line in f:
    line = line.strip()
    print line.encode('unicode_escape')



