"""Project Euler Problem 24: Lexicographic permutations

https://projecteuler.net/problem=24
(Copied verbatim from project_euler.ipynb, cell 24.)
"""

# Problem 24: Lexicographic permutations
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
num = 10
ind = int(1e6)   ### start from 1 to num! ###
def lexicographic(num,ind):
    l=list(range(num+1))
    f=[]
    def n_and_ind(n,ind,num):
        if ind-n*factorial(num)>0:
            return n,ind-n*factorial(num)
        else:
            return n_and_ind(n-1,ind,num)
    for x in range(num-1,-1,-1):
        pos,ind=n_and_ind(x,ind,x)
        f.append(str(l[pos]))
        l.remove(l[pos])
    return int(''.join(f))
print(lexicographic(num,ind))
