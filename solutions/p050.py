"""Project Euler Problem 50: Consecutive prime sum

https://projecteuler.net/problem=50
(Copied verbatim from project_euler.ipynb, cell 50.)
"""

# Problem 50: Consecutive prime sum
# Sieve of Sundaram to sieve the prime number: https://en.wikipedia.org/wiki/Sieve_of_Sundaram
# more detailed info about other language: https://www.geeksforgeeks.org/circular-primes-less-than-n/
import functools as ftool
from tqdm.notebook import tqdm_notebook
import numpy as np
def sieve_of_Sundaram(n):  #the prime number smaller than n
    k = (n-2)//2
    integers_list=[True]*(k+1)
    for i in range(1,k+1):
        j=i
        while i+j+2*i*j<=k:
            integers_list[i+j+2*i*j]=False
            j+=1
    #return integers_list # it can be muted
    prime = []
    if n>2:
        prime.append(2)
    for i in range(1,k+1):
        if integers_list[i]:
            prime.append(2*i+1)
    return prime
if __name__=="__main__":
    lim=int(10**6)
    prime_arr=np.array(sieve_of_Sundaram(lim))
    length=len(prime_arr)
    #print(sum(prime[3:24]))
    prime_dict={}
    for i in range(length):
        sumprime=0
        for j in range(i,length):
            sumprime+=prime_arr[j]
            if sumprime>=lim:
                sumprime-=prime_arr[j]
                j-=1
                break
            if (sumprime in prime_arr) and (j-i>1):
                if prime_dict.get(sumprime,(0,0,0,0,0))[-1]<=j-i+1:
                    prime_dict[sumprime]=(prime_arr[i],prime_arr[j],i,j,j-i+1)
    print("Sum of prime: (ini_val, final_val, ini_index, fin_index, length)")
    #print(prime_dict)
    key_sort=sorted(prime_dict.items(),key=lambda x:x[0],reverse=True)
    val_sort=sorted(prime_dict.items(),key=lambda x:x[1][-1],reverse=True)
    print(key_sort[0])
    print(val_sort[0])
######## it takes about 19.4 seconds ########
