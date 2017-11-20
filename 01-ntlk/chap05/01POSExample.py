#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 词性标注
text = nltk.word_tokenize("And now for something completely defferent")
print nltk.pos_tag(text)

text = nltk.word_tokenize("They refuese to permit us to obtain the refuse permit")
print nltk.pos_tag(text)

# 查找相同上下文w1w'w2的 w'
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')


