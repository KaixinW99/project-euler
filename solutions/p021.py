"""Project Euler Problem 21: Amicable numbers

https://projecteuler.net/problem=21
(Copied verbatim from project_euler.ipynb, cell 21.)
"""

# Problem 21: Amicable numbers
# Perfect number and divisor-sum, related to problem 23 and problem 95
from math import sqrt
def divisor_sum(n):
    sum_of_divisor=1 ### 1 is always the divisor of all number
    if int(sqrt(n))==sqrt(n):
        sum_of_divisor+=sqrt(n)
    for d in range(2,int(sqrt(n))+1):
        if n%d==0 and d!=n/d:
            sum_of_divisor+=d+n/d
    return sum_of_divisor
amicable_list = []
for x in range(3,10000):   ### 2 is not the amicable number
    if divisor_sum(divisor_sum(x))==x and divisor_sum(x)!=x:
        amicable_list.append(x)
#print(amicable_list)
print(sum(amicable_list))
