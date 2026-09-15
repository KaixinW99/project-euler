"""Project Euler Problem 23: Non-abundant sums

https://projecteuler.net/problem=23
(Copied verbatim from project_euler.ipynb, cell 23.)
"""

# Problem 23: Non-abundant sums
# Perfect number and divisor-sum, related to problem 21 and problem 95
from math import sqrt
def divisor_sum(n):
    sum_of_divisor=1 ### 1 is always the divisor of all number
    if int(sqrt(n))==sqrt(n):
        sum_of_divisor+=sqrt(n)
    for d in range(2,int(sqrt(n))+1):
        if n%d==0 and d!=n/d:
            sum_of_divisor+=d+n/d
    return sum_of_divisor

abundant_num=[]
for x in range(12,28124):
    if divisor_sum(x)>x:
        abundant_num.append(x)
#print(abundant_num)
abundant_sum=set()
for i in range(len(abundant_num)):
    for j in range(i,len(abundant_num)):
        abundant_sum.add(abundant_num[i]+abundant_num[j])
nonabundant_sum_all=0
for x in range(28124):
    if not (x in abundant_sum):
        nonabundant_sum_all+=x
print(nonabundant_sum_all)
