"""Project Euler Problem 1: Multiples of 3 or 5

https://projecteuler.net/problem=1
(Copied verbatim from project_euler.ipynb, cell 1.)
"""

# Problem 1: Multiples of 3 or 5
"""
def multiplier(n,uplimit):
    return [x for x in range(1,uplimit) if x%n==0]
print(sum(multiplier(3,1000))+sum(multiplier(5,1000))-sum(multiplier(15,1000)))
"""
#! a much faster one
def multiplier(f,uplimit):
    i = (uplimit-1)//f
    return i*(i+1)*f//2
n = 1000
print(multiplier(3,n)+multiplier(5,n)-multiplier(15,n))
