"""Project Euler Problem 60: Prime pair sets

https://projecteuler.net/problem=60
(Copied verbatim from project_euler.ipynb, cell 60.)
"""

# Problem 60: Prime pair sets
### Sieve of Eratosthenes on Geeks for Geeks: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
### This one is a little bit faster because we check from 2 to int(sqrt(n)+1)
### This one also involves the upper limit.
def Sieve_of_Eratosthenes(n):
    """ Sieve of Sundaram: https://www.geeksforgeeks.org/sieve-of-eratosthenes/ """
    prime=list(range(n+1))
    prime[1]=0
    for i in range(2,int(n**0.5+1)):
        for j in range(i*i,n+1,i): #like the 9*9 multiply table
            prime[j]=0
    return [int(x) for x in prime if x!=0]

### Miller–Rabin primality test: https://en.wikipedia.org/wiki/Miller–Rabin_primality_test
### algorithm: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
from math import comb
import random
def is_prime(n, k = 3):
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2 == 0
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1 # shift right by 1 bits
      # A for loop with a random sample of numbers
      for a in random.sample(range(2, n-2), k):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop

def check(x,y):
    a = int(str(x)+str(y))
    b = int(str(y)+str(x))
    if is_prime(a) and is_prime(b):
        return True
    else:
        return False
    
def prime_pairs(primes):
    # a is the first number
    for a in primes:
        # b is the second number
        for b in primes:
            # check if b is less than a
            if b < a:
                continue
            # check if a and b satisfy the condition
            if check(a,b):
                # c is the third number
                for c in primes:
                    # check if c is less than b
                    if c < b:
                        continue
                    # check if a,c and b,c satisfy the condition
                    if check(a,c) and check(b,c):
                        # d is the fourth number
                        for d in primes:
                            # check if d is less than c
                            if d < c:
                                continue
                            # check if (a,d), (b,d) and (c,d) satisfy the condition
                            if check(a,d) and check(b,d) and check(c,d):
                                # e is the fifth prime
                                for e in primes:
                                    # check if e is less than d
                                    if e < d:
                                        continue
                                    # check if (a,e), (b,e), (c,e) and (d,e) satisfy the condition
                                    if check(a,e) and check(b,e) and check(c,e) and check(d,e):
                                        return a+b+c+d+e

primes=Sieve_of_Eratosthenes(10000)
print(prime_pairs(primes))
