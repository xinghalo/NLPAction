#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

t = 'walk', 'fem', 3
print t
print t[0]
print t[1:]
print len(t)

raw = 'I turned off the spectroroute'
text = ['I', 'turned', 'off', 'the', 'spectroroute']
pair = (6, 'turned')
print raw[2], text[3], pair[1]
print raw[-3:], text[-3:], pair[-3:]
print len(raw), len(text), len(pair)

raw = 'Red lorry, yellow lorry, red lorry, yellow lorry.'
text = nltk.word_tokenize(raw)
fdist = nltk.FreqDist(text)
print list(fdist)
for key in fdist:
    print fdist[key],
print

words = ['I', 'turned', 'off', 'the', 'spectroroute']
words[2], words[3], words[4] = words[3], words[4], words[2]
print words

# 合并两个序列
tags = ['noun', 'verb', 'prep', 'det', 'noun']
print zip(words, tags)
print list(enumerate(words))

# 切分集合
text = nltk.corpus.nps_chat.words()
cut = int(0.9 * len(text))
trainning_data, test_data = text[:cut],text[cut:]
print text == trainning_data + test_data
print len(trainning_data) / len(test_data)

# 合并不同类型的序列
words = 'I turned off the spectroroute'.split()
wordlens = [(len(word),word) for word in words]
wordlens.sort()
print ' '.join(w for (_,w) in wordlens)

# todo 这个概念可以好好理解一下 —— 产生器表达式
text = '1 2 3 4 5 6 7'
print max([w.lower() for w in nltk.word_tokenize(text)])
print max(w.lower() for w in nltk.word_tokenize(text))