#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 查找词干

# 删除后缀
def stem(word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s','ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

# 匹配所有带后缀的单词
print re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$','processes')

def stem2(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$'
    match = re.findall(regexp, word)
    if len(match) == 0:
        return word
    stem, suffix = match[0]
    return stem

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
 is no basis for a system of government. Supreme executive power derives from
 a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = nltk.word_tokenize(raw)
print [stem2(t) for t in tokens]