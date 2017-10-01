# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 07:23:10 2017

@author: wxybdth
regex 3
"""
import re
#字符 . * + 等字符在正则表达式中有特殊含义
#如果想要匹配他们本身就需要加转义字符\
s1 = 'Jay*chou+Bruno*Mars'
s2 = '+++++++++'
pattern1 = re.compile('\*')
pattern2 = re.compile('\++')
# pattern2 = re.compile('*') error
res1 = re.findall(pattern1, s1)
print(res1) #['*', '*']
res2 = re.findall(pattern2,s2)
print(res2) #['+++++++++']

#\的用法
#首先 在Python中字符\表示的是转义字符 两个\\其实表示的是一个字符‘\’的意思
#其次 正则表达式中也是用\表示转义字符 所以\\也是表示一个字符'\'的意思
s1 = 'abc\\ncd\\th' 
pattern1 = re.compile('\\\\')
res1 = re.findall(pattern1,s1)
print(res1)

#r可以令转义字符失效变成普通字符
s1 = 'abc\ncd\t'
s2 = r'abc\ncd\t'
s3 = 'abc\mcd\o'
pattern2 = re.compile(r'\\')
res1 = re.findall(pattern2, s1)
print(res1)  #[]
res2 = re.findall(pattern2, s2)
print(res2) #['\\', '\\']
res3 = re.findall(pattern2, s3)
print(res3) #因为\m 和 \o都没有 所以\仍然是一个普通字符 ['\\', '\\']


pattern4 = re.compile(r'\\\\')
s ="abc\\cd\\hh"
res4 = re.findall(pattern4, s)
print(res4) #[]

s5 = '\\d+'
pattern5 = re.compile("\\\\d\\+")
res5 = re.findall(pattern5, s5)
print(res5) #['\\d+']









