"""Project Euler Problem 16: Power digit sum

https://projecteuler.net/problem=16
(Copied verbatim from project_euler.ipynb, cell 16.)
"""

# Problem 16: Power digit sum
num = 2**1000
numstr_list = [int(x) for x in str(num)]
print(sum(numstr_list))
