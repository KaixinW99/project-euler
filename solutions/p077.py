"""Project Euler Problem 77: Prime summations

https://projecteuler.net/problem=77
(Copied verbatim from project_euler.ipynb, cell 77.)
"""

# Problem 77: Prime summations
import sympy as sym
import numpy as np
target = 100 # I guess that is limit
primes = list(sym.sieve.primerange(0, target)) #It generates all prime numbers in the range [a, b)
ways=np.zeros(target+1,dtype=int)
ways[0]=1
for i in range(len(primes)):
    for j in range(primes[i],target+1):
        ways[j]+=ways[j-primes[i]]
print(np.where(ways>5000)[0][0]) # np.where will return an array, so we need to slice twice
