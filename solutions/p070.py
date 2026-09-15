"""Project Euler Problem 70: Totient permutation

https://projecteuler.net/problem=70
(Copied verbatim from project_euler.ipynb, cell 70.)
"""

# Problem 70: Totient permutation
""" Euler's totient function: "https://en.wikipedia.org/wiki/Euler's_totient_function" 
    phi(n)=n*prod(1-1/p) where the product is over all positive prime divisors p of n 
    phi(n)=p1^(k1-1)*(p1-1) * p2^(k2-1)*(p2-1) * ... * pr^(kr-1)*(pr-1) """

""" n/phi(n) = 1/prod(1-1/p) For the smallest n/phi(n), the denominator should be maximized.
    n can be a prime, but phi(n)=n-1 which cannot be permutated. 
    n can be multiplication of two distinct prime factor, which is close to sqrt(10000000)=3162, so we can choose 2000 to 5000 
    phi(n) = p1*p2*(1-1/p1)*(1-1/p2) = (p1-1)(p2-1) """
import sympy as sym
def is_perm(a,b):
    asort=sorted(str(a))
    bsort=sorted(str(b))
    if asort==bsort:
        return True
def Totient_permutation(prime_list,limit):
    best = 1
    phibest = 1
    bestRatio = float("inf")
    length=len(prime_list)
    for i in range(length):
        for j in range(i+1,length):
            n = prime_list[i]*prime_list[j]
            if n>limit: break
            phi = (prime_list[i]-1)*(prime_list[j]-1)
            ratio = n/phi
            if is_perm(n,phi) and bestRatio > ratio:
                best = n
                phibest = phi
                bestRatio = ratio
    return best

if __name__=="__main__":
    lower, upper=2000, 5000
    """ Here we use prime generator from sympy: https://www.geeksforgeeks.org/prime-functions-python-sympy/
        or you can use the one I write based on Sieve of Eratosthenes by searching it in this notebook """
    prime_list=list(sym.sieve.primerange(lower, upper)) #It generates all prime numbers in the range [a, b)
    print(Totient_permutation(prime_list,10000000))
