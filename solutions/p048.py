"""Project Euler Problem 48: Self powers

https://projecteuler.net/problem=48
(Copied verbatim from project_euler.ipynb, cell 48.)
"""

# Problem 48: Self powers
sum_selfpower=0
for i in range(1,1001):
    sum_selfpower+=i**i
print(sum_selfpower%(10**10))
# what if we use cpp to calculate it out?
