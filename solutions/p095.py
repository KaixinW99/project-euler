"""Project Euler Problem 95: Amicable chains

https://projecteuler.net/problem=95
(Copied verbatim from project_euler.ipynb, cell 95.)
"""

# Problem 95: Amicable chains
# Perfect number and divisor-sum, related to problem 21 and problem 23
"""
from math import sqrt
from collections import defaultdict
from tqdm import tqdm_notebook
def sum_proper_divisor(n):
    if n == 1: return 0
    def prime_factor(n):
        pf_dict = defaultdict(int)
        for i in range(2,n):
            while n%i==0:
                n//=i
                pf_dict[i]+=1
        return pf_dict
    all_factor_dict = prime_factor(n)
    if all_factor_dict=={}: return 1
    sum_divisor = 1
    for f, e in all_factor_dict.items():
        each_f = 0
        for i in range(e+1):
            each_f+=f**i
        sum_divisor*=each_f
    return sum_divisor-n

if __name__ =="__main__":
    sum_proper_divisor_dict = defaultdict(int)
    uplimit = int(1000000) 
    for x in tqdm_notebook(range(1,uplimit+1)):
        while True:
            next_num = sum_proper_divisor(x)
            if next_num == 1:
                sum_proper_divisor_dict[x]=0
            if next_num>uplimit:
                sum_proper_divisor_dict[x]=0
                #sum_proper_divisor_dict[next_num]=0
                break
            if next_num<x:
                sum_proper_divisor_dict[x]+=sum_proper_divisor_dict[next_num]
                break
            if next_num==x:
                sum_proper_divisor_dict[x]+=1
                break
            sum_proper_divisor_dict[x]+=1
            x=next_num
    #print(sum_proper_divisor_dict)
"""
"""The former one takes 3h"""
from collections import defaultdict
LIMIT = int(10**6)
d_sum = [0] * (LIMIT+1)
d_chain = defaultdict(int)

#! This is the coding method to handle the sum of all proper divisor
#! In mathematics, you can find all of the prime factors and their possible times.
#! 24 = 2**3 * 3 -> the sum of all divisors is (2**0 + 2**1 + 2**2 + 2**3) * (3*0 + 3**1)
#! 28 = 2**2 * 7 -> (2**0 + 2**1 + 2**2) * (7**0 + 7**1) = 7 * 8 = 56 -> 56-28 = 28
for i in range(1,LIMIT+1):          # all the possible factors to number
    for j in range(i*2,LIMIT+1,i):  # start from the one larger than factors, step is the factor itself
        d_sum[j]+=i

for i in range(LIMIT+1):
    cur = i
    visited = {i}
    while True:
        nex = d_sum[cur]
        d_chain[i] += 1
        if nex == i:
            break
        elif (nex > LIMIT) or (nex in visited):
            d_chain[i] = 0
            break
        else:
            visited.add(nex)
            cur = nex
print(max(d_chain.items(),key=lambda x: x[1]))
