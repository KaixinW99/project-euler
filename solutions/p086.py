"""Project Euler Problem 86: Cuboid route

https://projecteuler.net/problem=86
(Copied verbatim from project_euler.ipynb, cell 86.)
"""

# Problem 86: Cuboid route
""" Euclid's formula to generate all primitive Pythagorean triplets: https://en.wikipedia.org/wiki/Pythagorean_triple"""
""" Primitive Pythagorean triplets: a= m^2 - n^2 ; b= 2mn ; c= m^2 + n^2 with m > n > 0; m,n coprime; m+n odd """
import math
import itertools as itert
def combinations(a: int,b_c: int) -> int:
    if 2*a < b_c:
        #* the longest side must be a -> if 2a < b+c then either b or c would be longer than a
        return 0
    if a >= b_c:
        #* a >= b+c, any combination (b,c) produces a valid cuboid
        return b_c//2
    #* a < b+c, a>=b>=c so a>=b>=(b+c)/2
    return a - (b_c-1)//2

def countSingle(a: int) -> int:
    #* count how many paths exist with length a
    sum_all: int = 0
    for b_c in range(1, 2*a+1):
        diag_squa = a*a+b_c*b_c
        root = math.sqrt(diag_squa)
        if root*root==diag_squa:
            sum_all+=combinations(a,b_c)
    return sum_all

def countALL(LIMIT: int) -> list:
    #* count combinations per path length
    solu = [0] * (LIMIT+1)
    for m in range(1, int(math.sqrt(2*LIMIT))+1):
        for n in range((m%2)+1,m,2):
            if math.gcd(m,n)!=1:
                continue
            x = m*m - n*n
            y = 2*m*n

            for k in itert.count(1):
                if k*x>LIMIT:
                    break
                solu[k*x] += combinations(k*x,k*y)
            for k in itert.count(1):
                if k*y>LIMIT:
                    break
                solu[k*y] += combinations(k*y,k*x)
    return solu

sum_all = 0
total = []
solutions = countALL(10000)
for i in solutions:
    sum_all+=i
    total.append(sum_all)
    if sum_all > 1_000_000:
        print(len(total)-1)
        break
