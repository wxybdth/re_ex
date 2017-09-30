# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 14:31:42 2017

@author: wxybdth
regex 2
"""

import re
#一些基本的元字符
#\b 表示单词的开始或者结束 仅仅代表一个位置 不匹配空白字符
#特别注意：在匹配的模式前面加上r 因为模式里面\ 加上r表示原生字符
pattern1 = re.compile(r'\bhi\b')
pattren2 = re.compile(r'hi')
pattern3 = re.compile(r'\bhi')
pattren4 = re.compile(r'hi\b')

s = 'hi shit high nahi'
res1 = re.findall(pattern1, s)
print(res1)  #['hi'] 匹配单词hi
res2 = re.findall(pattren2, s) 
print(res2)  # ['hi', 'hi', 'hi', 'hi'] 匹配单词 hi shit high nahi 因为四个单词中都有hi 
res3 = re.findall(pattern3, s)
print(res3) # ['hi', 'hi'] 匹配单词 hi high
res4 = re.findall(pattren4, s)
print(res4) # ['hi', 'hi'] 匹配单词 hi nahi





