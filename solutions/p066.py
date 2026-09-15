"""Project Euler Problem 66: Diophantine equation

https://projecteuler.net/problem=66
(Copied verbatim from project_euler.ipynb, cell 66.)
"""

# Problem 66: Diophantine equation
'''
# for the nunmber less than 100, it takes about 42s. #
def diophantine(upperbound):
    minimal_sol=[]
    for D in range(2,upperbound+1):
        if D**0.5==int(D**0.5):
            continue
        y = 1
        while int((1+D*y**2)**0.5)!=(1+D*y**2)**0.5:
            y+=1
        minimal_sol.append(int((1+D*y**2)**0.5))
    return minimal_sol
diophantine(1000)
'''
# Pell's equation: https://en.wikipedia.org/wiki/Pell%27s_equation
# Pell’s Equation - Brahmagupta and Bhaskara II: https://cs.uwaterloo.ca/~cbruni/CO480Resources/lectures/CO480MayAug2017/lecture5.pdf
# More details from https://radiusofcircle.blogspot.com/2017/01/project-euler-problem-66-solution-with-python.html
def cf(n):
    """Bhaskara's Lemma to solve negative pell's equation (continued fraction)"""
    mn = 0.0
    dn = 1.0
    a0 = int(n**0.5)
    an = int(n**0.5)
    convergents = [a0]
    period = 0
    if a0 != n**0.5:
        while an != 2*a0:
            mn = int(dn*an - mn)
            dn = int((n - mn**2)/dn)
            an = int((a0 + mn)/dn)
            convergents.append(an)
    return convergents[:-1]

def cf_inv(cf):
    """
    function to calculate the simple fraction from the continued fraction.
    """
    numerator = 1
    denominator = cf.pop()
    while cf:
        denominator, numerator = denominator*cf.pop() + numerator, denominator
    return denominator, numerator

# variable to store the largest value 
# and the place it occurs
largest = 0, 0

# for loop less than 1000
for i in range(1, 1001):
    if i%(i)**0.5!= 0:
        continued_fraction = cf(i)
        if len(continued_fraction) % 2 != 0:
            u, v = cf_inv(continued_fraction)
            u, v = 2*u**2+1, 2*u*v
        else:
            u, v = cf_inv(continued_fraction)
        if u > largest[1]:
            largest = i, u
# print the largest value
print (largest[0])
