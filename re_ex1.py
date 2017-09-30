# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:57:58 2017
regex expression 1 
@author: 王鑫沂
"""
import re
#pattern 要匹配的字符串模式，字符串可以选择忽略大小写，匹配多行等等等其他选项需要用re.compile编译成pattern型，
pattern = re.compile('hello',re.I)
#需要匹配的字符串
s = 'HElloworldhello'

#不同的匹配方法 
#re.match 从字符串的起始位置来对pattern进行匹配，只匹配第一个符合的结果 匹配结果作为一个match对象返回
res1 = re.match(pattern,s)
print(res1.group()) #HEllo

#re.findall 从字符串的起始位置对pattern进行匹配，匹配所有正确的结果 匹配结果以列表的形式返回
res2 = re.findall(pattern,s)
print(res2)  # ['HEllo', 'hello']

#res.sub arg1 匹配的模式 arg2 替换的模式 arg3 待匹配的字符串
res3 = re.sub(pattern,'good',s)
print(res3) # goodworldgood

#re.split 将字符串以pattern为间隔分开 返回分开后的列表
res4 = re.split(pattern,s)
print(res4) #['', 'world', '']
pattern2 = re.compile('(hello)',re.I)
res5 = re.compile(pattern2,s)
print(res5) #['', 'HEllo', 'world', 'hello', ''] 如果在pattern外打个括号 就不会将pattern所在的词保留



