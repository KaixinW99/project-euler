"""Project Euler Problem 40: Champernowne's constant

https://projecteuler.net/problem=40
(Copied verbatim from project_euler.ipynb, cell 40.)
"""

# Problem 40: Champernowne's constant
from numpy import prod
def champernowne(n):
    r,s=0,9
    k=1
    while s<n:
        r=s
        k+=1
        s+=k*9*10**(k-1)
    h = n-r-1
    t = 10**(k-1)+h//k
    p = h%k
    return int(str(t)[p])

if __name__=="__main__":
    #print(champernowne(21))
    diglist=[champernowne(10**x) for x in range(7)]
    print(prod(diglist))
