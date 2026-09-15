"""Project Euler Problem 82: Path sum: three ways

https://projecteuler.net/problem=82
(Copied verbatim from project_euler.ipynb, cell 82.)
"""

# Problem 82: Path sum: three ways
# Dynamic programming: https://en.wikipedia.org/wiki/Dynamic_programming
import numpy as np
f = np.genfromtxt("p082_matrix.txt",dtype=int,delimiter=",")
rowlen,collen=len(f),len(f[0])
sol = f[:,rowlen-1] #initialization
for i in range(rowlen-2,-1,-1):
    # traverse down
    sol[0]+=f[0,i]
    for j in range(1,rowlen):
        sol[j]=min(sol[j-1]+f[j,i],sol[j]+f[j,i])
    # traverse up
    for j in range(rowlen-2,-1,-1):
        sol[j]=min(sol[j],sol[j+1]+f[j,i])
print(min(sol))
