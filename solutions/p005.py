"""Project Euler Problem 5: Smallest multiple

https://projecteuler.net/problem=5
(Copied verbatim from project_euler.ipynb, cell 5.)
"""

# Problem 5: Smallest multiple
from math import log
from functools import reduce
from numpy import prod
from operator import mul
def is_prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
uplimit = 20
plist=[x**(int(log(uplimit,x))) for x in range(2,uplimit+1) if is_prime(x)]
print(reduce(lambda x,y: x*y,plist))
#print(reduce(mul,plist))
#print(prod(plist))
