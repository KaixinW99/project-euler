"""Project Euler Problem 18: Maximum path sum I

https://projecteuler.net/problem=18
(Copied verbatim from project_euler.ipynb, cell 18.)
"""

# Problem 18: Maximum path sum I
# That is the count partition (or number partition) we learnt in CS61A for Tree Recursion in UCBerkeley: https://inst.eecs.berkeley.edu/~cs61a/fa13/slides/08-Tree_1pps.pdf

# totcase = 2^(height-1)
input_tri='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.split('\n')
tri_str=[x.split(' ') for x in input_tri]
tri_int=[[int(y) for y in x] for x in tri_str]
#print(tri_str)
#print(tri_int)
#length=len(tri_str[-1])
### from Bottom to top: iteration ###
def MaxSumPath_iter(tri):
    for i in range(len(tri)-2,-1,-1):
        for j in range(i+1):
            if tri[i+1][j]>tri[i+1][j+1]:
                tri[i][j]+=tri[i+1][j]
            else:
                tri[i][j]+=tri[i+1][j+1]
    return tri[0][0]
print(MaxSumPath_iter(tri_int))

### from top to bottom: recursion ###
tri_int=[[int(y) for y in x] for x in tri_str]
def MaxSumPat_recu(tri,i,j):
    if j==len(tri) or i==len(tri):
        return 0
    else:
        return tri[i][j]+max(MaxSumPat_recu(tri,i+1,j),MaxSumPat_recu(tri,i+1,j+1))
print(MaxSumPat_recu(tri_int,0,0))

##########ATTANTION############
# The change of list in the func will change it globally!!!!!!! #
# list is a class #
