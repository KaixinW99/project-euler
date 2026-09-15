"""Project Euler Problem 80: Square root digital expansion

https://projecteuler.net/problem=80
(Copied verbatim from project_euler.ipynb, cell 80.)
"""

# Problem 80: Square root digital expansion
""" Handle the sqrt with only integer!!!
    Square roots by substraction: https://studylib.net/doc/7921494/square-roots-by-subtraction---jarvis--frazer """
def sqrt_sub(n,digit):
    limit = int(10**(digit+1))
    a,b = int(5*n),5
    while b<limit:
        if a>=b:
            a-=b
            b+=10
        else:
            a=int(100*a)
            b=int(b//10*100)+5
    return int(b//100)

def sqrt_dig_sum(limit,digit):
    tot = 0
    for x in range(2,limit+1):
        if int(x**0.5)!=x**0.5:
            num=sqrt_sub(x,digit)
            tot+=sum([int(i) for i in list(str(num))])
    return tot
print(sqrt_dig_sum(100,100))
