#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 计算每个句子平均的词数
print len(nltk.corpus.brown.words())/len(nltk.corpus.brown.sents())

# 基于Punkt句子分割器分割
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = sent_tokenizer.tokenize(text)

pprint.pprint(sents[171:181])

# 测试
text = 'hello, U.S.A. heheda! hello, world.'
sents = sent_tokenizer.tokenize(text)
pprint.pprint(sents)

# 分词
def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words

text = 'doyouseethekittyseethedoggydoyoulikethekittylikethedoggy'
seg1 = '00000000000000010000000000100000000000000001000000000001'
seg2 = '01001001001000010010010000101001000100100001000100100001'
print segment(text, seg1)
print segment(text, seg2)

# 基于词典的分词，给每个词打分，寻找分值最少的分词结果
def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size+lexicon_size
seg3 = '0000100100000011001000000110000100010000001100010000001'
print segment(text, seg3)

print evaluate(text, seg1)
print evaluate(text, seg2)
print evaluate(text, seg3)

# todo 模拟退火算法：
# 一开始仅搜索短语分词；随机扰动0和1；每次迭代，扰动边界减少

from random import randint

def flip(segs, pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs,randint(0,len(segs)-1))
    return segs

def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text,segs)
        for i in range(iterations):
            guess = flip_n(segs, int(round(temperature)))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print evaluate(text, segs), segment(text,segs)
    print
    return segs

print anneal(text, seg1, 5000, 1.2)