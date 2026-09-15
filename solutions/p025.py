"""Project Euler Problem 25: 1000-digit Fibonacci number

https://projecteuler.net/problem=25
(Copied verbatim from project_euler.ipynb, cell 25.)
"""

# Problem 25: 1000-digit Fibonacci number
def fib_dig(n):
    a,b,i=1,1,2
    while b<10**(n-1):
        a,b=b,a+b
        i+=1
    return i
print(fib_dig(1000))
