"""Project Euler Problem 33: Digit cancelling fractions

https://projecteuler.net/problem=33
(Copied verbatim from project_euler.ipynb, cell 33.)
"""

# Problem 33: Digit cancelling fractions
# just do some simple calculations
from math import gcd
def rec_gcd(a,b):
    if b==0:
        return a
    else:
        return rec_gcd(b,a%b)
def CancelFrac():
    np, dp = 1,1
    for c in range(1,10):
        for d in range(1,c):
            for n in range(1,d):
                if 9*n*(c-d)==c*(d-n):
                    np*=n
                    dp*=d
    return dp/gcd(np,dp)  #dp/rec_gec(np,dp)
if __name__=="__main__":
    print(CancelFrac())
