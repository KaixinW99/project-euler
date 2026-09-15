"""Project Euler Problem 14: Longest Collatz sequence

https://projecteuler.net/problem=14
(Copied verbatim from project_euler.ipynb, cell 14.)
"""

# Problem 14: Longest Collatz sequence
import sys
sys.setrecursionlimit(int(1e8))
def collatz(n):
    if n==1:
        return 1
    elif n%2==0:
        return collatz(n/2)+1
    else:
        return collatz(3*n+1)+1

collatz_len=[]
for i in range(1,int(1e6)):
    collatz_len.append(collatz(i))
ind = collatz_len.index(max(collatz_len))+1
print(ind)

### is there another quick method? it takes 32.6s to run ###
