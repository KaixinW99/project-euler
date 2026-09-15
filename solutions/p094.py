"""Project Euler Problem 94: Almost equilateral triangles

https://projecteuler.net/problem=94
(Copied verbatim from project_euler.ipynb, cell 94.)
"""

# Problem 94: Almost equilateral triangles
# ! Heron's formula: trianlge area = sqrt(s(s-a)(s-b)(s-c)) w.r.t s=(a+b+c)/2
# ! Opt 1: a=b=odd, c=even 
# ! Opt 2: c=2d, a and d are coprime; if a = 0 mod k and d = 0 mod k, c = 2d = 0 mod k, and a = c (+/-) 1 = (+/-) 1 mod k instead of 0 mod k
""" Euclid's formula to generate all primitive Pythagorean triplets: https://en.wikipedia.org/wiki/Pythagorean_triple"""
""" Primitive Pythagorean triplets: a= m^2 - n^2 ; b= 2mn ; c= m^2 + n^2 with m > n > 0; m,n coprime; m+n odd """
import math
import itertools as itert
perimeters = 0
LIMIT = 10**9
# ! a = (m^2+n^2). p = 3a (+/-) 1 =  3(m^2+n^2) (+/-) 1 <= LIMIT
# ! to get all possible solution, 3(m^2+n^2) - 1 <= LIMIT
# ! as m>n, m^2 <= (LIMT+1)/6
for m in itert.count(2):
    if m*m > (LIMIT+1)/6:
        break
    for n in range(m-1,0,-2): # m,n are coprime 
        if math.gcd(m,n)==1:
            a = m*m-n*n
            b = 2*m*n
            c = m*m+n*n
            if a*2 == c-1:
                p = c*3-1
                if p<= LIMIT:
                    perimeters+=p
            if a*2 == c+1:
                p = c*3+1
                if p<= LIMIT:
                    perimeters+=p
            if b*2 == c-1:
                p = c*3-1
                if p<= LIMIT:
                    perimeters+=p
            if b*2 == c+1:
                p = c*3+1
                if p<= LIMIT:
                    perimeters+=p
print(perimeters)
# ! it takes about 20s
