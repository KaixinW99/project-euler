"""Project Euler Problem 57: Square root convergents

https://projecteuler.net/problem=57
(Copied verbatim from project_euler.ipynb, cell 57.)
"""

# Problem 57: Square root convergents
# Method one: burte force with python library "fractions": https://docs.python.org/3/library/fractions.html
# the recursive definition: a{k+1}=1+1/(1+a{k}) with a{k}=n{k}/d{k} -> a{k+1}=(2*d{k}+n{k})/(d{k}+n{k})
from math import gcd
def sqrtConvergent(upper):
    c=0
    n=d=1
    for _ in range(int(upper+1)):
        n,d=2*d+n,d+n
        #gcdnd=gcd(int(n),int(d))
        #n,d=int(n/gcdnd),int(d/gcdnd)
        if len(str(n))>len(str(d)):
            c+=1
    return c
if __name__=="__main__":
    print(sqrtConvergent(1000))
