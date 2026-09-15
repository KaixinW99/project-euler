"""Project Euler Problem 81: Path sum: two ways

https://projecteuler.net/problem=81
(Copied verbatim from project_euler.ipynb, cell 81.)
"""

# Problem 81: Path sum: two ways
# Dynamic programming: https://en.wikipedia.org/wiki/Dynamic_programming
"""[[4445 2697 5115 ... 2758 3748 5870]
    [1096   20 1318 ... 4187 9353 9377]
    [9607 7385  521 ... 9515 6385 9230]
    ...
    [2265 8192 1763 ... 7456 5128 5294]
    [2132 8992 8160 ... 5634 1113 5789]
    [5304 5499  564 ... 2751 3406 7981]]
    """
import numpy as np
f = np.genfromtxt("p081_matrix.txt",dtype=int,delimiter=",")
rowlen,collen=len(f),len(f[0])
for i in range(rowlen-2,-1,-1):
    """ There is only one choice for last row and last column """
    f[rowlen-1,i]+=f[rowlen-1,i+1]
    f[i,rowlen-1]+=f[i+1,rowlen-1]
for i in range(rowlen-2,-1,-1):
    for j in range(rowlen-2,-1,-1):
        """ All other positions with two choices """
        f[i,j]+=min(f[i+1,j],f[i,j+1])
print(f[0,0])
