"""Project Euler Problem 43: Sub-string divisibility

https://projecteuler.net/problem=43
(Copied verbatim from project_euler.ipynb, cell 43.)
"""

# Problem 43: Sub-string divisibility
# d2d3d4 is divisible by 2 -> d4 even
# d3d4d5 is divisible by 3 -> d3+d4+d5 is divisible by 3
# d4d5d6 is divisible by 5 -> d6 is either 0 or 5
# d6d7d8 is divisible by 11 -> d6 cann only be 5, or (011,022,...,099), so should be (506,517,528,539,561,572,583,594)
# d7d8d9 is divisible by 13 -> d6d7d8d9 is reduced to be (5286,5390,5728,5832)
# d8d9d10 is divisible by 17 -> d6d7d8d9d10 is reduced to be (52867,53901,57289)
# trace back to d5d6d7, which is divisible ty 7 -> d5d6d7d8d9d10 is reduced to be (952867,357289)
# Finally, d3d4d5d6d7d8d9d10 can be reduced to be (30952867,60357289,06357289)
import itertools as itert
substring=[]
for p in itert.permutations(range(10)):
    s = "".join([str(x) for x in p])
    cond1 = int(s[1:4])%2==0
    cond2 = int(s[2:5])%3==0
    cond3 = int(s[3:6])%5==0
    cond4 = int(s[4:7])%7==0
    cond5 = int(s[5:8])%11==0
    cond6 = int(s[6:9])%13==0
    cond7 = int(s[7:10])%17==0
    if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7:
        substring.append(int(s))
print(substring)
print(sum(substring))
######## it takes 13.3s to run ########
