"""Project Euler Problem 69: Totient maximum

https://projecteuler.net/problem=69
(Copied verbatim from project_euler.ipynb, cell 69.)
"""

# Problem 69: Totient maximum
""" Euler's totient function: "https://en.wikipedia.org/wiki/Euler's_totient_function" 
    phi(n)=n*prod(1-1/p) where the product is over all positive prime divisors p of n 
    phi(n)=p1^(k1-1)*(p1-1) * p2^(k2-1)*(p2-1) * ... * pr^(kr-1)*(pr-1) """
""" Actually, we need to the product of prime, and find the largest one smaller 1000000
    We can multiply other number to the product to let it get closer to 1000000 """
import sympy as sym
import functools as functl
def Totient_maximum(n): # n is the upper limit, n must be larger than 3 !!!
    """ Here we use prime generator from sympy: https://www.geeksforgeeks.org/prime-functions-python-sympy/
        or you can use the one I write based on Sieve of Eratosthenes by searching it in this notebook """
    prime_prod = lambda upper: functl.reduce(lambda x,y: x*y, sym.sieve.primerange(0, upper)) #It generates all prime numbers in the range [a, b)
    upper=3
    while prime_prod(upper)*2<=n:
        upper+=1
    return prime_prod(upper)

if __name__=="__main__":
    print(Totient_maximum(1000000))
