"""Project Euler Problem 67: Maximum path sum II

https://projecteuler.net/problem=67
(Copied verbatim from project_euler.ipynb, cell 67.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 67: Maximum path sum II
# Compare it with problem 18 
# That is the count partition (or number partition) we learnt in CS61A for Tree Recursion in UCBerkeley: https://inst.eecs.berkeley.edu/~cs61a/fa13/slides/08-Tree_1pps.pdf
    
f=open('p067_triangle.txt','r')
tri_list=[item.split(" ") for item in f.read().strip("\n").split("\n")]  ### string list ###
f.close()
tri_list=[[int(y) for y in x] for x in tri_list]
#print(tri_list)
def MaxSumPath_iter(tri):
    for i in range(len(tri)-2,-1,-1):
        for j in range(i+1):
            if tri[i+1][j]>tri[i+1][j+1]:
                tri[i][j]+=tri[i+1][j]
            else:
                tri[i][j]+=tri[i+1][j+1]
    return tri[0][0]
if __name__=="__main__":
    print(MaxSumPath_iter(tri_list))
# you cannot use the recursion, cuz it takes forever long.
