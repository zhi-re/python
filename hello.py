#!/usr/bin/python
# coding=utf-8

print ("你好，世界");print ("hello");

if False:
    print("true") # 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量
else:
    print("false")
    print("false3")

# 使用斜杠（ \）将一行的语句分为多行显示
one = 1;
two = 2;
three = 3;
total = one + \
        two + \
        three
print(total)
# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)

# Python 引号
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
print(word)
print(sentence)
print(paragraph)

'''
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
"""

# raw_input("按下 enter 键退出，其他任意键显示...\n")

import sys;x = 'cq';sys.stdout.write(x + '\n');sys.stdout.write(x+'\n');

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y

"""多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。"""

a = 30;
if a<20 : 
   print a; 
elif a==20 :  
    print a+a; 
else :  
    print a+a+a; 
