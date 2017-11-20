#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from nltk.corpus import gutenberg, nps_chat

moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
print moby.findall(r"<a> (<.*>) <man>")

# print gutenberg.words('melville-moby_dick.txt')[:1000]
# r = r'<a> (.*) <man>'
# raw = 'a good man'
# print re.findall(r,raw)

from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies','learned']))
print hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>")