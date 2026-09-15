"""Project Euler Problem 47: Distinct primes factors

https://projecteuler.net/problem=47
(Copied verbatim from project_euler.ipynb, cell 47.)
"""

# Problem 47: Distinct primes factors
'''
# Sieve of Eratosthenes methods
# for more details, please check https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import numpy as np
from tqdm.notebook import tqdm_notebook
def Sieve_of_Eratosthenes(prime):
    prime[1]=0 # 1 is not taken into account
    l = len(prime)
    for i in range(2,l):
        for j in range(i*i,l,i): #like the 9*9 multiply table
            prime[j]=0

def distinctprime(upper,numfactor,seqlength):
    prime=np.array(range(int(upper)))
    Sieve_of_Eratosthenes(prime)
    prime=prime[prime!=0]
    def primefactor(num):
        pset=set()
        checkprime=prime[prime<=num/2]
        for p in checkprime:
            while num%p==0:
                num/=p
                pset.add(p)
            if len(pset)>numfactor:
                return False
            if num<p:
                break
        # if the num of prime factor is smaller than numfactor
        if len(pset)==numfactor:
            return True
        else:
            return False
    ### the smallest number should be 2*3*5*7*... etc ###
    start=1
    for i in range(numfactor):
        start*=prime[i]
    #####################################################
    for i in tqdm_notebook(range(start,upper)):
        counternum=0
        for j in range(i,i+seqlength):
            if not primefactor(j):
                break
            else:
                counternum+=1
        if counternum==seqlength:
            return i
if __name__=="__main__":
    print(distinctprime(int(10**6),4,4))
######## it takes about 79 seconds ########
'''

### some other idea on Internet: http://louistiao.me/posts/project-euler/problem-47-distinct-primes-factors/ ###
import itertools as itert
import functools as ftool
import math
import collections as coll
def nwise(iterable,n=2):         # n is the number of items in each frame
    """tee gives you the iterator"""
    iters=itert.tee(iterable,n)  # Return n independent iterators from a single iterable.
    for i, it in enumerate(iters):
        for _ in range(i):
            """decrease iterator by next()"""
            """if you use list(iterator), then all the elements are iterated"""
            next(it,None)       # Returns the next item from the iterator. e.g. next(iterator, what if iterator is exhausted, finished)
    return zip(*iters)          # the transpose of the iters only cares about the longest one. e.g. a=[[1,2,3,4],[2,3,4],[3,4]]; z=zip(*a) ---> output=list(z)=[(1,2,3),(2,3,4)]

### test for nwise() ###
#print(list(nwise(range(10),8)))
#print(list(nwise(range(10),3)))

### the details about prime_factors, you can check from: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
def prime_factors(n):
    prime_factor_list=[]
    while n%2==0:
        prime_factor_list.append(2)
        n/=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            prime_factor_list.append(i)
            n/=i
    if n>2:
        prime_factor_list.append(n)
    prime_factor_dict=coll.Counter(prime_factor_list)
    return prime_factor_dict

### test for prime_factor() ###
#print(prime_factors(315))
#print(list(map(prime_factors,range(2,16))))

def consecutive_distinct_factors(n,m):
    """The first consective n numbers to have m distinct prime factors"""
    for factors in nwise(map(prime_factors,itert.count(2)),n):          # factors are the list of Counter_dictionary
        if all(map(lambda x: len(x)==m,factors)):                       #length of dictionary shows the number of item in dictionary
            return factors

### test for consecutive_distinct_factors() ###
#print(consecutive_distinct_factors(2, 2))
#print(consecutive_distinct_factors(3, 3))
#print(consecutive_distinct_factors(4, 4))

# The last one in functools.reduce is the initializer, 
# If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. 
product = lambda xs: ftool.reduce(lambda x, y: x*y, xs, 1) 

### test for product ###
#print(product([]))
#print(product(range(1,6+1)))

multiple = lambda factors: product(map(pow,factors.keys(),factors.values()))

### test for mutiple ###
#print(list(map(multiple,consecutive_distinct_factors(2,2))))
#print(list(map(multiple,consecutive_distinct_factors(3,3))))
print(list(map(multiple,consecutive_distinct_factors(4,4))))
