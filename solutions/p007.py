"""Project Euler Problem 7: 10001st prime

https://projecteuler.net/problem=7
(Copied verbatim from project_euler.ipynb, cell 7.)
"""

# Problem 7: 10001st prime 
def is_prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
def ind_prime(ind):
    s,n = 2,0
    while n<ind:
        if is_prime(s):
            n+=1
        s+=1
    return s-1
print(ind_prime(10001))

###### is there a new idea about it??? it takes 14.3s ######
