#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_text(str):
    text = re.sub('\s+',' ',str)
    text = re.sub(r'<.*?>',' ',text)
    return text

print get_text('<a>hahaha</a>')

# 输入输出，应该尽量避免修改参数

# 参数传递
def modify1(word):
    word = 'after'
s = 'before'
modify1(s)
print s

def modify2(list):
    list[1] = '2'
l = ['a','b','c']
modify2(l)
print  l

# 变量的作用域
# LGB规则：local 本地 --> global 全局 --> biuld-in 内置
# 防御性编程
def tag(word):
    assert isinstance(word, basestring), "参数不对"
    return word
tag('Stirng')
# tag(2)

# 功能分解

# 文档 http://www.python.org/dev/peps/pep-0257/的 docstring

def test(line):
    """
    descp
    :param line: input
    :return: none
    """
    print line

test("hello")