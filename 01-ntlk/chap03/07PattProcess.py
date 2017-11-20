#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
print wordlist

# 使用基本的元字符
print [w for w in wordlist if re.search('ed$',w)]
print [w for w in wordlist if re.search('^..j..t..$',w)]

# 正则表达式规则
'''
. 通配所有
^ 开头
$ 结尾
[] 匹配集合中的一个
* 零个或者多个
+ 1个或者多个
？零个或者多个
{a,b} 重复a-b次
'''

word = 'supercalifragilisticexpialidocious'
print re.findall(r'[aeiou]',word)

print len(re.findall(r'[aeiou]',word))

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj
                   for vs in re.findall(r'[aeiou]{2,}',word))
print fd.items()

# 字符块的更多操作
regexp = r'^[AEIOUaeiou]+[AEIOUaeiou]+$[^AEIOUaeiou]'
def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)

english_udhr = nltk.corpus.udhr.words('English-Latin1')
print nltk.tokenwrap(compress(w) for w in english_udhr[:75])

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
csv = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]',w)]
cfd = nltk.ConditionalFreqDist(csv)
print cfd.tabulate()

cv_word_pairs = [(cv, w) for w in rotokas_words
                 for cv in re.findall(r'[ptksvr][aeiou]',w)]
cv_index = nltk.Index(cv_word_pairs)
print cv_index['su']
print cv_index['po']

