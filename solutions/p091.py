"""Project Euler Problem 91: Right triangles with integer coordinates

https://projecteuler.net/problem=91
(Copied verbatim from project_euler.ipynb, cell 91.)
"""

# Problem 91: Right triangles with integer coordinates
# from tqdm import tqdm_notebook
import numpy as np
points = [(x,y) for x in range(0,51) for y in range(0,51)][1:]    # you can use complex number or 2d-coords
l_p = len(points)
count_rtriangle = 0
for i1 in range(l_p):
    for i2 in range(i1+1,l_p):
        a,b,c = points[i1], points[i2], np.subtract(points[i1],points[i2])
        if np.dot(a,b)==0 or np.dot(a,c)==0 or np.dot(b,c)==0:
            count_rtriangle+=1
print(count_rtriangle)
# ! it takes about 46s
