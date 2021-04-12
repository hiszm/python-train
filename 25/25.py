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



