"""Project Euler Problem 15: Lattice paths

https://projecteuler.net/problem=15
(Copied verbatim from project_euler.ipynb, cell 15.)
"""

# Problem 15: Lattice paths
import sys
sys.setrecursionlimit(int(1e8))
# That is the count partition (or number partition) we learnt in CS61A for Tree Recursion in UCBerkeley: https://inst.eecs.berkeley.edu/~cs61a/fa13/slides/08-Tree_1pps.pdf
'''
def lattice(length,width):
    if length==0 or width==0:
        return 1
    else:
        return lattice(length-1,width)+lattice(length,width-1)
'''
# it takes forever.
# Lets think it in combination number.
# You only have two ways to go and the total steps are fixed
# so that is (total steps)C(left steps)
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
print(int(factorial(40)/factorial(20)**2))
