### 15读取文件

这个代码主要是读取文件

运行`python 15.py a.txt`

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:21:44 2021

@author: hiszm
"""

from sys import argv

script,filename = argv

txt = open (filename)

print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")
# 这里 ">" 输入提示符号 ；提示你可以在这里输入 你需要输入 a.txt 即可
file_again = input ("> ")

txt_again = open (file_again)

print (txt_again.read())
```

![image-20210412133358424](https://gitee.com/hiszm/img2021/raw/master//April/20210412133405.png)

`a.txt `里面内容

```
------------------------------------------
a.txt
https://github.com/hiszm/python-train
------------------------------------------
```



### 16读写文件

这个代码主要是写文件

运行`python 16.py a.txt`

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:21:44 2021

@author: hiszm
"""

from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input ("?")

print ("Opening the file...")
target = open (filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input ("line 1: ")
line2 = input ("line 2: ")
line3 = input ("line 3: ")

print ("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()
```





![image-20210412134042562](https://gitee.com/hiszm/img2021/raw/master//April/20210412134042.png)

###  17更多文件操作

运行`python 16.py a.txt b.txt`

这个主要是复制文件`a.txt`的内容复制到`b.txt`,开始a里面是有内容的，b是没有内容的



![image-20210412134655385](https://gitee.com/hiszm/img2021/raw/master//April/20210412134655.png)

```python
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

# We could do these two on one line too, how?
raw_input = open (from_file)
indata = raw_input.read()

print ("The input file is %d bytes long" % len(indata))

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input ()

output = open(to_file, 'w')
output.write(indata)

print ("Alright, all done.")

output.close()
raw_input.close()


```

![image-20210412134527311](https://gitee.com/hiszm/img2021/raw/master//April/20210412134527.png)



### 习题 18: 命名、变量、代码、函数

主要介绍函数相关的结构

运行`python 18.py`

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:45:33 2021

@author: hiszm
"""

# This one is like your scripts with argv
def print_two (*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
    
# Ok, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
    
# This just takes one argument
def print_one (arg1):
    print ("arg1: %r" % arg1)
    
# This one takes no arguments
def print_none():
    print ("I got nothin'.")
    
print_two ("Zed","Shaw")
print_two_again ("Zed","Shaw")
print_one ("First!")
print_none()
```

![image-20210412134928095](https://gitee.com/hiszm/img2021/raw/master//April/20210412134928.png)

### 习题 19: 函数和变量

运行`python 19.py`

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:45:33 2021

@author: hiszm
"""

def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")
    

print ("We can just give the function numbers directly:")
cheese_and_crackers (20, 30)

print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crakers = 50

cheese_and_crackers (amount_of_cheese, amount_of_crakers)

print ("We can even do math inside too:")
cheese_and_crackers (10 + 20, 5 + 6)


print ("And we can combine the two, variables and math:")
cheese_and_crackers (amount_of_cheese + 100,
amount_of_crakers + 1000)
```

![image-20210412135233789](https://gitee.com/hiszm/img2021/raw/master//April/20210412135233.png)

### 习题 20: 函数和文件

代码主要用于按行读取文件里面的内容

运行`python 20.py a.txt`

```python
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
```

![image-20210412135442947](https://gitee.com/hiszm/img2021/raw/master//April/20210412135442.png)



> 思考：
>
> 这里只读取了三行
>
> 文件有4行,如何读取第四行`--------------------------------------`



### 习题 21: 函数可以返回东西

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:45:33 2021

@author: hiszm
"""

def add (a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

def subtract (a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return a - b
    
def multiply (a, b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b
    
def divide (a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b
    
print ("Let's do some math with just functions!")

age = add (30, 5)
height = subtract (78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)

print ("Age: %d, Height: %d, Weght: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add (age, subtract(height, multiply(weight, divide(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")
```

![image-20210412140011606](https://gitee.com/hiszm/img2021/raw/master//April/20210412140011.png)

### 习题 22: 到现在你学到了哪些东西？

一些基础知识的回顾



图片加载不出来请点击这里（https://segmentfault.com/a/1190000017338712 出处）

https://gitee.com/hiszm/img2021/raw/master//April/20210412141201.png

![image-20210412141200377](https://gitee.com/hiszm/img2021/raw/master//April/20210412141201.png)



![img](https://gitee.com/hiszm/img2021/raw/master//April/20210412140057.png)





### 习题 23: 读代码

https://github.com/hiszm/python-train

### 习题 24: 更多练习

`python 24.py a.txt`

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:45:33 2021

@author: hiszm
"""
print ("Let's practice everything.")
print ("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passsion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print ("--------------")
print (poem)
print ("--------------")


five = 10 - 2 + 3 - 6
print ("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_poit = 10000
beans, jars, crates = secret_formula(start_poit)

print ("With a starting point of: %d" % start_poit)
print ("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))


start_poit = start_poit / 10

print ("We can also do that this way:")
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_poit))
```

![image-20210412140409221](https://gitee.com/hiszm/img2021/raw/master//April/20210412140409.png)

### 习题 25: 更多更多的练习

`python 25.py a.txt`

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:21:44 2021

@author: hiszm
"""

import sys

sys.path.append('C:\\Users\\hiszm')  
                
import hiszm

sentence = "All good things come to those who wait."

words = hiszm.break_words(sentence)

print("--------------------")


print(words)


print("--------------------")

hiszm.print_first_word(words)


print("--------------------")
hiszm.print_last_word(words)

print("--------------------")




```

```
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print (word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
```

