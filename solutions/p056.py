"""Project Euler Problem 56: Powerful digit sum

https://projecteuler.net/problem=56
(Copied verbatim from project_euler.ipynb, cell 56.)
"""

# Problem 56: Powerful digit sum
import numpy as np
def digitsum(n):
    digsum=0
    while n>0:
        digsum+=n%10
        n//=10
    return digsum
if __name__=="__main__":
    powerlist=np.array([a**b for a in range(1,100) for b in range(1,100)])
    sumdiglist=np.array([])
    for x in powerlist:
        sumdiglist=np.append(sumdiglist,digitsum(x))
    #print(powerlist)
    print(int(max(sumdiglist)))
    #print(powerlist[sumdiglist==max(sumdiglist)][0])
