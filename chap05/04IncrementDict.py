#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 按照递减的顺序显示词性
counts = nltk.defaultdict(int)

from nltk.corpus import brown

for (word, tag) in brown.tagged_words(categories = 'news'):
    counts[tag] += 1

print counts['N']
print list(counts)

from operator import itemgetter

print sorted(counts.items(), key=itemgetter(1), reverse=True)

# itemgetter的用法

pair = ('NP', 8336)
print pair[1]
print itemgetter(1)(pair)

# 遍历 通过最后两个字母，显示相关的词

print len('ii')

last_letters = nltk.defaultdict(list)
words = nltk.corpus.words.words('en')

for word in words:
    key = word[-2:]
    last_letters[key].append(word)


print last_letters['ly']
print last_letters['zy']

# 复杂的key和value

pos = nltk.defaultdict(lambda: nltk.defaultdict(int))
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
print brown_news_tagged
# for ((w1,t1),(w2,t2)) in nltk.ibigrams(brown_news_tagged):
#     pos[(t1,w2)][t2] += 1
# print pos[('DET','right')]

# 词典的基本用法

d = {}
d['a'] = 'a123'
d['b'] = 'b123'

print d.keys()
print list(d)
print sorted(d)
print 'c' in d
print d.values()
