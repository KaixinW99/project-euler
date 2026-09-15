"""Project Euler Problem 31: Coin sums

https://projecteuler.net/problem=31
(Copied verbatim from project_euler.ipynb, cell 31.)
"""

# Problem 31: Coin sums
# That is the count partition (or number partition) we learnt in CS61A for Tree Recursion in UCBerkeley: https://inst.eecs.berkeley.edu/~cs61a/fa13/slides/08-Tree_1pps.pdf
# For more details about clever ones: https://www.geeksforgeeks.org/coin-change-dp-7/
"""
def count(S,m,n):
    if n==0:
        return 1
    if n<0:
        return 0
    if m<=0:
        return 0
    return count(S,m-1,n)+count(S,m,n-S[m-1]) # Main Algorithm: use at least one this kind of currency; don't use any this kind of currency
if __name__=="__main__":
    curr = [1,2,5,10,20,50,100,200]
    m = len(curr)
    n = 200
    print(count(curr,m,n))
"""

# Dynamic Programming: https://en.wikipedia.org/wiki/Dynamic_programming
import numpy as np
target=200
coin_size=[1,2,5,10,20,50,100,200]
ways=np.zeros(target+1,dtype=int)
ways[0]=1
for i in range(len(coin_size)):
    for j in range(coin_size[i],target+1):
        ways[j]+=ways[j-coin_size[i]]
print(ways[target])
