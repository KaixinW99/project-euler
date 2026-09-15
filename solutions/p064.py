"""Project Euler Problem 64: Odd period square roots

https://projecteuler.net/problem=64
(Copied verbatim from project_euler.ipynb, cell 64.)
"""

# Problem 64: Odd period square roots
# Detailed information about Contiuned Fraction: https://www.mathblog.dk/project-euler-continued-fractions-odd-period/
def Odd_period_square_roots(upperbound):
    result=0
    for i in range(2,upperbound+1):
        a0 = int(i**0.5)
        if a0**2==i: 
            continue
        period=0
        n,d,a=0,1,a0
        while a!=2*a0:
            """ The iterative part of algorithm: https://www.fq.math.ca/Papers1/42-2/quartrippon02_2004.pdf 
                Wikipedia about countiuned Fraction: https://en.wikipedia.org/wiki/Continued_fraction
                                                    https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
                n === numerator & d === denominator
                numerator = denominator * a - numerator
                denominator = floor((number-numerator^2)/denominator)
                a = floor((root+numerator)/denominator)
            """
            n=d*a-n
            d=(i-n**2)/d
            a=int((a0+n)/d)
            period+=1
        if period & 1==1: result+=1
    return result
print(Odd_period_square_roots(10000))
