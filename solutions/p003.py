"""Project Euler Problem 3: Largest prime factor

https://projecteuler.net/problem=3
(Copied verbatim from project_euler.ipynb, cell 3.)
"""

# Problem 3: Largest prime factor
a,b=2,600851475143
while a<b/a:
    if b%a!=0:
        a+=1
    else:
        b/=a
print((b==int(b))*int(b))
