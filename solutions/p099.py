"""Project Euler Problem 99: Largest exponential

https://projecteuler.net/problem=99
(Copied verbatim from project_euler.ipynb, cell 99.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 99: Largest exponential
from math import log
f = open("p099_base_exp.txt","r")
exp_l = [tuple(map(eval,line.split(","))) for line in f.readlines()]
largest = 0
largest_i = 0
for i,it in enumerate(exp_l):
    num = it[1]*log(it[0])
    if num > largest:
        largest = num
        largest_i = i+1
print(largest_i)
