"""Project Euler Problem 26: Reciprocal cycles

https://projecteuler.net/problem=26
(Copied verbatim from project_euler.ipynb, cell 26.)
"""

# Problem 26: Reciprocal cycles
import numpy as np
def recipr_cycle(n):
    if n==0:
        return 0
    lastpos=np.zeros(n)
    position=1
    dividend=1
    while True:
        remainder=dividend%n
        if remainder==0:
            return 0
        if lastpos[remainder]!=0:
            return position - lastpos[remainder]
        lastpos[remainder]=position
        position+=1
        dividend=remainder*10
#print(recipr_cycle(28))
if __name__=="__main__":
    len_list=[]
    for x in range(1000):
        len_list.append((x,recipr_cycle(x)))
    print(max(len_list,key=lambda m:m[1]))
    print(max(len_list,key=lambda m:m[1])[0])
    #print(len_list)
