"""Project Euler Problem 41: Pandigital prime

https://projecteuler.net/problem=41
(Copied verbatim from project_euler.ipynb, cell 41.)
"""

# Problem 41: Pandigital prime
import sympy as sym
import itertools as itert
import functools as ftool
### check whether n number can be divided by 3 ###
### that is 1, 4, 7 digits ###
PanPrime=[]
for p in itert.permutations(range(7,0,-1)):
    s = ftool.reduce(lambda a, b: 10*a+b, p)
    if sym.isprime(s):
        PanPrime.append(s)
print(max(PanPrime))
