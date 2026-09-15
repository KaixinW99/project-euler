"""Project Euler Problem 76: Counting summations

https://projecteuler.net/problem=76
(Copied verbatim from project_euler.ipynb, cell 76.)
"""

# Problem 76: Counting summations
""" That is the count partition (or number partition) we learnt in CS61A for Tree Recursion in UCBerkeley: https://inst.eecs.berkeley.edu/~cs61a/fa13/slides/08-Tree_1pps.pdf
    Main Algorithm: use at least one m (count_partition(n-m,m)); don't use any m (count_partition(n,m-1)) 
    BUT it takes FOREVER to run, so change to another idea """

"""
def count_partition(n,m): # it involves the number itself, so you may apply -1 to it.
    if n==0:
        return 1
    elif (n<0) or (m==0):
        return 0
    else:
        return count_partition(n-m,m)+count_partition(n,m-1)
if __name__=="__main__":
    print(count_partition(10,10))
"""

# you may also use PartitionsP[] in Mathematica to solve this number partition problem
# PartitionsP[]: https://reference.wolfram.com/language/ref/PartitionsP.html

# Dynamic programming: https://en.wikipedia.org/wiki/Dynamic_programming
# similar to problem 31
import numpy as np
target=100
ways=np.zeros(target+1,dtype=int)
ways[0]=1
for i in range(1,target): # we can use the number between 1 to target-1
    for j in range(i,target+1):
        ways[j]+=ways[j-i]
print(ways[target])
