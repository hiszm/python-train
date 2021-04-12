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
file_again = input ("> ")

txt_again = open (file_again)

print (txt_again.read())