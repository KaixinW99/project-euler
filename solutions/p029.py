"""Project Euler Problem 29: Distinct powers

https://projecteuler.net/problem=29
(Copied verbatim from project_euler.ipynb, cell 29.)
"""

# Problem 29: Distinct powers
setofpower={a**b for a in range(2,101) for b in range(2,101)}
print(len(setofpower))
