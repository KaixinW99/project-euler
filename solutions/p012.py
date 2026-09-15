"""Project Euler Problem 12: Highly divisible triangular number

https://projecteuler.net/problem=12
(Copied verbatim from project_euler.ipynb, cell 12.)
"""

# Problem 12: Highly divisible triangular number
# squence of triangle numbers = sum of natural numbers = n*(n+1)/2
from math import sqrt
def divisor_counter(n):
    num_of_divisor=2
    for d in range(2,int(sqrt(n))+1):
        if n%d==0 and d!=n/d:
            num_of_divisor+=2
    if int(sqrt(n))==sqrt(n):
        num_of_divisor+=1
    return num_of_divisor
n = 20  # 20*21/2=210
while True:
    if divisor_counter(n*(n+1)/2)>500:
        print(int(n*(n+1)/2))
        break
    n+=1
