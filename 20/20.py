# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:45:33 2021

@author: hiszm
"""

from sys import argv
# 从sys库中调用argv函数

script, input_file = argv
# 把argv解包，将参数依次赋予左边的变量名

def print_all(f):
# 定义函数，形参f
    print (f.read())
    # 以只读方式读取f中的内容并打印
    
def rewind(f):
# 定义函数，形参f
    f.seek(0)
    # 移动文件读取指针至f中内容的开头位置
    
def print_a_line(line_count, f):
# 定义函数，形参line_count和f
    print (line_count, f.readline())
    # 读取f内容的一整行，打印line_count中的内容和f中指定行的内容

current_file = open (input_file)
# 打开文件读取内容

print ("First let's print the whole file:\n")
# 打印并换行 首先让我们来打印这个文件里的内容

print_all (current_file)
# 打印current_file中的内容

print ("Now let's rewind, kind of like a tape.")
# 打印 现在让我们倒回去，有点像倒带

rewind (current_file)
# 将文件读取指针移至开头位置

print ("Let's print three lines:")
# 打印 让我们打印三行

current_line = 1
# 设置读取的行数为第一行
print_a_line (current_line, current_file)
# 打印文件内容的第一行

current_line = current_line + 1
# 行数增加1，即读取第二行
print_a_line (current_line, current_file)
# 打印文件内容的第二行

current_line = current_line + 1
# 行数再增加1，即读取第三行
print_a_line (current_line, current_file)
# 打印文件内容的第三行