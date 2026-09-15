"""Project Euler Problem 49: Prime permutations

https://projecteuler.net/problem=49
(Copied verbatim from project_euler.ipynb, cell 49.)
"""

# Problem 49: Prime permutations
# Sieve of Eratosthenes methods
# for more details, please check https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import itertools as itert
import functools as ftool
import numpy as np
def Sieve_of_Eratosthenes_digit(lower,upper):
    prime=np.array(range(upper))
    prime[1]=0 # 1 is not taken into account
    l = len(prime)
    for i in range(2,l):
        for j in range(i*i,l,i): #like the 9*9 multiply table
            prime[j]=0
    prime=prime[(prime!=0) & (prime>=lower)]
    return prime

primelist=Sieve_of_Eratosthenes_digit(int(10**3),int(10**4))
#print(primelist)
for fir in primelist:
    def comp_digit(num):
        component,digit=[],0
        while num!=0:
            component.append(num%10)
            num//=10
            digit+=1
        return component,digit
    fir_component, digit = comp_digit(fir)
    for thr_component in set(itert.permutations(fir_component[::-1])):
        thr = ftool.reduce(lambda a, b: 10*a+b, thr_component)
        if (thr>fir) and (thr in primelist):
            sec = int((thr+fir)/2)
            if sec in primelist:
                if sec-fir==3330:
                    #print(fir,sec,thr)
                    ### method 1 ###
                    print(int(fir*10**(2*digit)+sec*10**digit+thr))
                    ### method 2 ###
                    print(fir,end='')
                    print(sec,end='')
                    print(thr)
