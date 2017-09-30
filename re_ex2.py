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
#加上r之后会让转义字符的作用失效
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


#\d 表示数字 {n}表示数字重复次数
pattern = re.compile('0\d{2}-\d{7}')
s = 'phone number: 010-1234567, call !'
res = re.search(pattern, s)
print(res.group())

# .换行符以外的其他字符   \w字母数字下划线汉字 
# *任意数量  +表示一次或者多次
# * + 都是贪婪模式就是尽可能多的去匹配字符 
#在后面加上问号 变成非贪婪模式 *？就是尽可能少的去匹配字符
pattern1 = re.compile(r'\ba.+\b')
pattern2 = re.compile(r'\ba.*\b')
pattern3 = re.compile(r'\ba\w*\b')
pattern4 = re.compile(r'\ba\w+\b')
pattern5 = re.compile(r'\ba.+?\b')
s = 'phone number: 010-1234567, call a\n ans abcd!'
res1 = re.findall(pattern1, s)
print(res1) #['ans abcd'] 返回的是一个字符 贪婪模式
res2 = re.findall(pattern2, s)
print(res2) # ['a', 'ans abcd'] 
res3 = re.findall(pattern3, s)
print(res3) # ['a','ans','abcd']
res4 = re.findall(pattern4, s)
print(res4) #['ans','abcd']
res5 = re.findall(pattern4, s)
print(res5) #['ans', 'abcd'] 返回的是两个字符 懒惰模式


# ^ $ 匹配字符串的开头和结尾
pattern = re.compile(r'^\d{5,12}$') #匹配5-12位数字的字符串
s1 = 's123456789'
s2 = '1234455'
s3 = '12344445s'
res1 = re.match(pattern, s1)
print(res1) #None 因为以字母开头不满足要求
res2 = re.match(pattern, s2)
print(res2.group()) #1234455 满足要求
res3 = re.match(pattern, s3)
print(res3) #None 因为以字母结尾

 





