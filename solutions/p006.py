"""Project Euler Problem 6: Sum square difference

https://projecteuler.net/problem=6
(Copied verbatim from project_euler.ipynb, cell 6.)
"""

# Problem 6: Sum square difference
f, diff = 100, 0
for i in range(1,f+1):
    for j in range(i+1,f+1):
        diff+=i*j*2
print(diff)
