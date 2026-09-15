"""Project Euler Problem 10: Summation of primes

https://projecteuler.net/problem=10
(Copied verbatim from project_euler.ipynb, cell 10.)
"""

# Problem 10: Summation of primes
### it takes too much time ###
'''
def is_prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
x,totsum, upper = 2, 0, 2e6
while x<upper:
    if is_prime(x):
        totsum+=x
    x+=1
print(totsum)
'''

# Sieve of Eratosthenes methods
# for more details, please check https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sumprime(n):
    composite=list(range(n))
    composite[1]=0 # 1 is not taken into account
    for i in range(2,n):
        for j in range(i*i,n,i): #like the 9*9 multiply table
            composite[j]=0
    return sum(composite)
print(sumprime(int(2e6)))
###### is there a new idea about it??? it takes 1.3s ######
