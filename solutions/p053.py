"""Project Euler Problem 53: Combinatoric selections

https://projecteuler.net/problem=53
(Copied verbatim from project_euler.ipynb, cell 53.)
"""

# Problem 53: Combinatoric selections
from sympy import factorial
def combination(n,r):
    return factorial(n)/factorial(r)/factorial(n-r)
if __name__=="__main__":
    cou=0
    for n in range(1,101):
        for r in range(0,n):
            if combination(n,r)>10**6:
                cou+=1
    print(cou)
