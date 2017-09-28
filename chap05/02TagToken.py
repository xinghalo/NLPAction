#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 已标注的标示方法
tagged_token = nltk.tag.str2tuple('fly/NN')
print tagged_token
print tagged_token[0]

# 读取标注的语料库 用tagset = 'universal' 代替Simplify_tags=True
print nltk.corpus.brown.tagged_words()
print nltk.corpus.brown.tagged_words(tagset='universal')

# 词性标注集
''' 
这个貌似过期了，跟我使用的nltk版本不太一样

ADJ     形容词
ADV     动词
CNJ     连词
DET     限定词
EX      存在量词
FW      外来词
MOD     情态动词

N       名词
NP      专有名词
NUM     数词
PRO     代词
P       介词
TO      词to
UH      感叹词
V       动词
VD      过去式
VG      现在分词
VN      过去分词
WH      Wh限定词
'''

# 新闻类， 词性分布
from nltk.corpus import brown
brown_new_tagged = brown.tagged_words(categories='news',tagset = 'universal')
tag_fd = nltk.FreqDist(tag for (word,tag) in brown_new_tagged)
print tag_fd.keys()

# 名词
word_tag_pairs = nltk.bigrams(brown_new_tagged)
print list(nltk.FreqDist(a[1] for (a,b) in word_tag_pairs if b[1] == 'NOUN'))

# 动词
wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
word_tag_fd = nltk.FreqDist(wsj)
print [word+"/"+tag for (word,tag) in word_tag_fd if tag.startswith('V')]

# 查找词的词性
cfd1 = nltk.ConditionalFreqDist(wsj)
print cfd1['yield'].keys()
print cfd1['cut'].keys()

# 根据词性，查找对应的词
cfd2 = nltk.ConditionalFreqDist((tag,word) for (word,tag) in wsj)
print cfd2['VERB'].keys()

# 形容词和副词
# 形容词用来修饰名词，如 the large pizza
# 副词用来修饰动词或者形容词，如the stock fell quickly; mary's teacher was really nice
# 冠词，the a
# 情态动词，should may
# 人称代词，she they

# 查看各种词性下的top词
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag,word) for (word,tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag,cfd[tag].keys()[:5]) for tag in cfd.conditions())

tagdict = findtags('N', nltk.corpus.brown.tagged_words(categories='news',tagset='universal'))
for tag in sorted(tagdict):
    print tag, tagdict[tag]

# 探索标注好的语料库
brown_learned_text = brown.words(categories='learned')
print sorted(set(b for (a,b) in nltk.bigrams(brown_learned_text) if a =='often'))

brown_lrnd_tagged = brown.tagged_words(categories='learned',tagset='universal')
tags = [b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()

# 基于POS寻找三词短语
from nltk.corpus import brown
def process(sentence):
    for (w1, t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
        if(t1.startswith('V') and t2=='TO' and t3.startswith('V')):
            print w1, w2, w3

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

# 查看标注不清的词
data = nltk.ConditionalFreqDist((word.lower(),tag) for (word,tag) in brown_new_tagged)
for word in data.conditions():
    if len(data[word]) > 3:
        tags = data[word].keys()
        print word, ' '.join(tags)