#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 拼接
silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught','us','.']
print ' '.join(silly)
print ';'.join(silly)
print ''.join(silly)

# 字符串 和 格式化
word = 'cat'
sentence = """hello
world"""

print word
print sentence

# 格式化输出
fdist = nltk.FreqDist(['dog','cat','dog','cat'])
for word in fdist:
    print word, '->', fdist[word], ';',

# format
print '%s -> %d;' % ('cat', 3)
print '%s -> ' % 'cat'
print ' -> %d' % 3
print 'I wnat a %s right now' % 'coffe'
print "%s wants a %s %s" % ("lee", "coffe", "now")

# 基于模版的输出
template = 'Lee wants a %s right now'
menu = ['sandwich', 'coffe']
for snack in menu:
    print template % snack

# 排列
print '%6s' % 'dog'
print '%-6s' % 'dog'
print '%6s' % 'abcdefjjjj'
width = 6
print '%-*s' % (width,'dog')
count, total = 3205, 9375
print "accuracy for %d words:%2.4f%%" % (total, 100*count/total)
print "%"
print "%%"
print "%d%%" % 4


# 格式化输出 词频
def tabulate(cfdist, words, categories):
    print '%-16s' % 'Category',
    for word in words:
        print '%6s' % word,
    print
    for category in categories:
        print '%-16s' % category,
        for word in words:
            print '%6d' % cfdist[category][word],
        print
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories = genre))
genres = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
tabulate(cfd,modals,genres)

# 将结果写入文件
output_file = open('output.txt','w')
words = set(nltk.corpus.genesis.words('english-kjv.txt'))
for word in sorted(words):
    output_file.write(word + "\n")

print len(words)
print str(len(words))
output_file.write(str(len(words))+'\n')
output_file.close()

# 换行
from textwrap import fill
format = '%s (%d),'
saying = ['After','all','is','said','and','done',',','more','like','is','said','than']
pieces = [format % (word, len(word)) for word in saying]
output = ' '.join(pieces)
wrapped = fill(output)
# 格式化输出
print wrapped
# 原样输出
print saying