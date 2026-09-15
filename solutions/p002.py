"""Project Euler Problem 2: Even Fibonacci numbers

https://projecteuler.net/problem=2
(Copied verbatim from project_euler.ipynb, cell 2.)
"""

# Problem 2: Even Fibonacci numbers
a,b,eventot=1,1,0
while a+b<=4e6:
    a,b=a+b,a+2*b
    eventot+=a
    a,b=b,a+b
    #print(a,b)
print(eventot)
