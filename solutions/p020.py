"""Project Euler Problem 20: Factorial digit sum

https://projecteuler.net/problem=20
(Copied verbatim from project_euler.ipynb, cell 20.)
"""

# Problem 20: Factorial digit sum
import sys
sys.setrecursionlimit(int(1e3))
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
sum_dig=sum([int(x) for x in str(factorial(100))])
print(sum_dig)
