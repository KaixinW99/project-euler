"""Project Euler Problem 100: Arranged probability

https://projecteuler.net/problem=100
(Copied verbatim from project_euler.ipynb, cell 100.)
"""

# Problem 100: Arranged probability

# Suppose the box has b blue discs and r red discs
#* The probability of taking 2 blue disc is [b/(b+r)]*[(b-1)/(b+r-1)]
#* solve [b(b-1)]/[(b+r)(b+r-1)] = 1/2
# -> b^2 -(2r+1)b +(r-r^2) = 0 -> b = [(2r+1) +/- sqrt(8r^2+1)] /2
#* b = r + [sqrt(8r^2+1)+1]/2 with respect to b>r (so it can reach 1/2)

#* b is integer, so sqrt(8r^2 + 1) is odd and 8r^2 + 1 should be perfext square
#* 8y^2 + 1 = x^2 for x > 0 
#* Pell equation: x^2 - 8y^2 = 1, similar to problem 66
#! Pell's equation: https://en.wikipedia.org/wiki/Pell%27s_equation
#! Pell’s Equation - Brahmagupta and Bhaskara II: https://cs.uwaterloo.ca/~cbruni/CO480Resources/lectures/CO480MayAug2017/lecture5.pdf

# Suppose fundamental solution is (x0, y0) with another one (x1, y1)
#! all other solutions be derived from it (proven on the top reference).
#* x0^2 - 8y0^2 = 1 -> (x0 - y0*sqrt(8))(x0 + y0*sqrt(8)) = 1 so as (x1,y1)
#* [(x0 - y0*sqrt(8))(x0 + y0*sqrt(8))][(x1 - y1*sqrt(8))(x1 + y1*sqrt(8))] = 1*1
# [(x0 - y0*sqrt(8))(x1 - y1*sqrt(8))][(x0 + y0*sqrt(8))(x1 + y1*sqrt(8))] = 1
# [x0x1 - x0y1*sqrt(8) - x1y0*sqrt(8) + 8y0y1][x0x1 + x0y1*sqrt(8) + x1y0*sqrt(8) + 8y0y1] = 1
# [(x0y1+8y0y1) - (x0y1*sqrt(8) + x1y0*sqrt(8))][(x0y1+8y0y1) + (x0y1*sqrt(8) + x1y0*sqrt(8))] = 1
#* (x0y1+8y0y1)^2 - 8(x0y1 + x1y0)^2 = 1
#* Therefore, ((x0y1+8y0y1),(x0y1 + x1y0)) is also the solution
#* By inspection, fundamental solution is (3,1)

# fundamental solution
x0, y0 = 3,1

# current solution
x, y = x0, y0

LIMIT = 10**12
while True:
    sqrt_check = (8*(y**2)+1)**0.5
    if sqrt_check%2==1: # odd
        blue = (sqrt_check+1)//2 + y
        if blue + y > LIMIT: # total number
            print(int(blue))
            break
    # next larger solution
    x, y = x*x0 + y*y0*8, x*y0 + y*x0
