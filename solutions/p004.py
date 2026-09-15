"""Project Euler Problem 4: Largest palindrome product

https://projecteuler.net/problem=4
(Copied verbatim from project_euler.ipynb, cell 4.)
"""

# Problem 4: Largest palindrome product
# all the 6-digit palindromic number can be divided by 11
# only numeric number of 3-digit numbers can be divided by 11

#palind3d=[x*11 for x in range(10,90)]
#print(max([x*y for x in palind3d for y in range(100,999) if str(x*y)==str(x*y)[::-1]]))

# but it is much slower. LOL!!!

print(max([x*y for x in range(100,999) for y in range(100,999) if str(x*y)==str(x*y)[::-1]]))
