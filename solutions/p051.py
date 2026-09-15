"""Project Euler Problem 51: Prime digit replacements

https://projecteuler.net/problem=51
(Copied verbatim from project_euler.ipynb, cell 51.)
"""

# Problem 51: Prime digit replacements
### Modular arithmetic: https://en.wikipedia.org/wiki/Modular_arithmetic ###

# We can check the (mod 3), the sum of all digit === number (mod 3)
# the number with one replacement (*)  ,in 10 digits, it always provides 3 number divisible by 3.
# the number with one replacement (**) ,in 10 digits, it always provides 3 number divisible by 3.
# the number with one replacement (***),you can have all not divisible by 3.
import collections as coll
def sieve_of_Eratosthenes(n):
    """Sieve of Sundaram: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""
    prime=list(range(n))
    prime[1]=0
    for i in range(2,n):
        for j in range(i*i,n,i): #like the 9*9 multiply table
            prime[j]=0
    return [int(x) for x in prime if x!=0]

def rep_dig(n):
    """It could be two or more sets of replicate digit in one number, e.g. 112233"""
    n = str(n)
    rep=[str(x) for x in range(10)]
    sol = []
    for digit,degeneracy in coll.Counter(n).items():
        if degeneracy!=1:
            temp=[int(n.replace(str(digit),x)) for x in rep]
            ### prevent the case from having the heading 0, e.g. 002345 ###
            if len(str(temp[0]))<len(str(temp[1])):
                temp.pop(0)
            sol.append(temp)
    return sol

def check(num_in_family,primes_list):
    for num in primes_list:
        tot_rep_list=rep_dig(num)
        for rep_list in tot_rep_list:
            sol=[num for num in rep_list if num in primes_list]
            if len(sol)==num_in_family:
                return sol

primes=sieve_of_Eratosthenes(int(1000000))
prime_rep=[x for x in primes if max(coll.Counter(str(x)).values())>=3] ### it can be 121313 (3 (1)) 222323 (4 (2)) ...
primefamily=check(8,prime_rep)
print(primefamily[0])
