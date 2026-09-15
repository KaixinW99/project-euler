"""Project Euler Problem 45: Triangular, pentagonal, and hexagonal

https://projecteuler.net/problem=45
(Copied verbatim from project_euler.ipynb, cell 45.)
"""

# Problem 45: Triangular, pentagonal, and hexagonal
import numpy as np
def isPentagon(x):
    n = np.sqrt(1+24*x)
    return n%6==5
def isTriangle(x):
    n = np.sqrt(1+8*x)
    return n%2==1
def hexafunc(n):
    return n*(2*n-1)
if __name__=="__main__":
    n=144
    while True:
        num=hexafunc(n)
        if isPentagon(num) and isTriangle(num):
            print(num)
            break
        else:
            n+=1
