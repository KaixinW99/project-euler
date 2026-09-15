"""Project Euler Problem 27: Quadratic primes

https://projecteuler.net/problem=27
(Copied verbatim from project_euler.ipynb, cell 27.)
"""

# Problem 27: Quadratic primes
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n/2)+1):
        if n%i==0:
            return False
    return True

alist,blist,nlist=[],[],[]
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0
        while is_prime(n**2+a*n+b):
            n+=1
        nlist.append(n)
        blist.append(b)
        alist.append(a)
i = nlist.index(max(nlist))
print(alist[i]*blist[i])
