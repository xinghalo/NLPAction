#-*- coding: UTF-8 -*-
from __future__ import division

import nltk
import re, pprint
import os
from urllib import urlopen

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 赋值
foo = 'Monty'
bar = foo
foo = 'Python'
print bar

# 链表的赋值
foo = ['M','P']
bar = foo
foo[1] = 'N'
print bar

# 总结：变量的赋值是拷贝；结构化对象的赋值是指针

# 嵌套对象
empty = []
nested = [empty, empty, empty]
print nested

nested[1].append('Python')
print nested

nested2 = [[]]*3
nested2[1].append('P')
nested2[1] = ['N']
print nested2

# 等式

size = 5
python = ['Python']
snake_nest = [python]*size
print snake_nest[0] == snake_nest[1] == snake_nest[2] == snake_nest[3] == snake_nest[4]
print snake_nest[0] is snake_nest[1] is snake_nest[2] is snake_nest[3] is snake_nest[4]

import random
position = random.choice(range(size))
snake_nest[position] = ['python']
print snake_nest

print snake_nest[0] == snake_nest[1] == snake_nest[2] == snake_nest[3] == snake_nest[4]
print snake_nest[0] is snake_nest[1] is snake_nest[2] is snake_nest[3] is snake_nest[4]

# == 用来判断值
# is 用来判断对象

# 条件语句
mixed = ['cat', ['dog'], []]
for element in mixed:
    if element:
        print element
animals = ['cat','dog']
if 'cat' in animals:
    print 1
elif 'dog' in animals: # 如果匹配if 那么elif就不会执行
    print 2

sent = ['No', 'good', 'fish', 'goes', 'anywhere', 'without', 'a', 'porpoise', '.']
print all(len(w) > 4 for w in sent)
print any(len(w) > 4 for w in sent)