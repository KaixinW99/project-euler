"""Project Euler Problem 58: Spiral primes

https://projecteuler.net/problem=58
(Copied verbatim from project_euler.ipynb, cell 58.)
"""

# Problem 58: Spiral primes
# check the problem 28: number spiral
import sympy as sym
import itertools as itert
# chck the itertools here: https://docs.python.org/3/library/itertools.html#itertools.count
def spiral_prime(n):
    totalnum=1
    primenum=0
    position=1
    if n==1:
        return totalnum
    for i in range(3,n+1,2): # the matrix
        for j in range(4): # the number in the diagonal
            position+=i-1
            totalnum+=1
            #print(position,totalnum)
            if sym.isprime(position):
                primenum+=1
    return primenum/totalnum
### it takes forever in the loop ###

# the diagonal can be separated into four equation with recursion in math
# a{n} = (9,25,49,81,121,...)= 4n^2+4n+1 = (2n+1)^2        = m^2      -> it is not the prime
# b{n} = (5,17,37,65,101,...)= 4n^2+1    = (m-1)^2+1       = m(m-2)+2
# c{n} = (3,13,31,57,91,...) = 4n^2-2n+1 = (m-1)^2-(m-1)+1 = m(m-3)+3
# d{n} = (7,21,43,73,111,...)= 4n^2+2n+1 = (m-1)^2+(m-1)+1 = m(m-1)+1
# p/c < 0.1 ---> p/(4n+1) < 0.1 ---> 10p < 4n+1 and return 2n+1 ---> 10p < 2m-1 and return m 
# n -> [1,inf,1] ---> m -> 2n+1 -> [3,inf,2]
def spiral_prime_check(percent):
    p=0
    for m in itert.count(3,2):
        p+=sym.isprime(m*(m-1)+1)
        p+=sym.isprime(m*(m-2)+2)
        p+=sym.isprime(m*(m-3)+3)
        if 100*percent*p<2*m-1:
            return m
if __name__=="__main__":
    lim=spiral_prime_check(0.1)
    print("the spiral prime limit from prime check of 0.1 is %i"%lim)
    print("the first one falls below 0.1 (side length = %i) is %.6f and the last one (side length = %i) is %.6f"%(lim,spiral_prime(lim),lim-2,spiral_prime(lim-2)))
