"""Project Euler Problem 17: Number letter counts

https://projecteuler.net/problem=17
(Copied verbatim from project_euler.ipynb, cell 17.)
"""

# Problem 17: Number letter counts
# one two three four five six seven eight nine (3 3 5 4 4 3 5 5 4)
# ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen (3 6 6 8 8 7 7 9 8 8)
# twenty thirty forty fifty sixty seventy eighty ninety (6 6 5 5 5 7 6 6)
# hundred (7) thousand (8)
dec = 3+6+6+8+8+7+7+9+8+8
def one_digit():
    return 3+3+5+4+4+3+5+5+4
def two_digit():
    tot = dec
    for x in [6,6,5,5,5,7,6,6]:
        tot+=x*10+one_digit()
    return tot
#print(two_digit()+one_digit())
def three_digit():
    tot = 0-3*9 # one hundred without 'and'
    for x in [3,3,5,4,4,3,5,5,4]:
        tot+=(x+7+3)*100+two_digit()+one_digit()
    return tot
print(one_digit()+two_digit()+three_digit()+3+8)
