"""Project Euler Problem 44: Pentagon numbers

https://projecteuler.net/problem=44
(Copied verbatim from project_euler.ipynb, cell 44.)
"""

# Problem 44: Pentagon numbers
# solve the number inversely, n=(1+sqrt(1+24x))/6
import numpy as np
def isPentagon(x):
    n = np.sqrt(1+24*x)
    return n%6==5
def p(n):
    return 1/2*n*(3*n-1)
if __name__=="__main__":
    pentagonnum=[]
    for i in range(1,5000):
        for j in range(1,i):
            pi,pj=p(i),p(j)
            if isPentagon(pi+pj) and isPentagon(pi-pj):
                pentagonnum.append(pi-pj)
    print(int(min(pentagonnum)))
######## it takes about 25.1s ########
