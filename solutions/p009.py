"""Project Euler Problem 9: Special Pythagorean triplet

https://projecteuler.net/problem=9
(Copied verbatim from project_euler.ipynb, cell 9.)
"""

# Problem 9: Special Pythagorean triplet
# substitute and get $a*b+1000*c==500000$ ### it cost more time ###
# triangle for any a+b>c, so for any a,b,c < 500 
for a in range(1,500):
    for b in range(a+1,500):
        c = 1000 - a - b
        if a*a+b*b==c*c:
            print(a*b*(1000-a-b))
