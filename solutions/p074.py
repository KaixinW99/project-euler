"""Project Euler Problem 74: Digit factorial chains

https://projecteuler.net/problem=74
(Copied verbatim from project_euler.ipynb, cell 74.)
"""

# Problem 74: Digit factorial chains
import sympy as sym
import numpy as np
f = [sym.factorial(n) for n in range(10)]
def FacSum(n):
    temp = n
    facsum = 0
    while temp>0:
        facsum+=f[temp%10]
        temp//=10
    return facsum
limit = int(1e6)
seqlength = np.zeros(int(1e7),dtype=int)
""" as there are only three such loops that exists:
    169 -> 363601 -> 1454 -> 169 
    871 -> 45361 -> 871
    872 -> 45362 -> 872 
    145 -> 145 and 40585 -> 40585 From Problem 34
    1 -> 1
    2 -> 2"""
seqlength[169] = 3
seqlength[363601] = 3
seqlength[1454] = 3
seqlength[871] = 2
seqlength[45361] = 2
seqlength[872] = 2
seqlength[45362] = 2
seqlength[145] = 1
seqlength[40585] = 1
seqlength[1]=1
seqlength[2]=1
for i in range(3,limit+1):
    n = i
    cout = 0
    while seqlength[n]==0:
        cout += 1
        n = FacSum(n)
    seqlength[i] = cout + seqlength[n]
result = np.count_nonzero(seqlength==60)
print(result)
# it takes about 21s
