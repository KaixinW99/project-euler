"""Project Euler Problem 42: Coded triangle numbers

https://projecteuler.net/problem=42
(Copied verbatim from project_euler.ipynb, cell 42.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 42: Coded triangle numbers
### use ord() to check the unicode of letter, start from "a", ranked 97; "A", ranked 65###
#print(ord('A'))
#print(ord('a'))
import numpy as np
f=open('p042_words.txt','r')
strlist=f.readline().strip('" "').split('","')
f.close()
### solve the n=1/2*(sqrt(8*t+1)-1) ###
tot,totlist=0,[]
for word in strlist:
    s=0
    for letter in list(word.lower()):
        s+=ord(letter)-96
        #print(s)
    num = 1/2*((8*s+1)**0.5-1)
    if num==int(num):
        tot+=1
        totlist.append(word)
print(tot)
