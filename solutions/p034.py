"""Project Euler Problem 34: Digit factorials

https://projecteuler.net/problem=34
(Copied verbatim from project_euler.ipynb, cell 34.)
"""

# Problem 34: Digit factorials
from math import factorial
def digitfetch(i):
    listofdigit=[]
    while i>0:
        listofdigit.append(i%10)
        i//=10
    return listofdigit
def rec_factorial(n):
    if n<=1:
        return 1
    else:
        return factorial(n-1)*n
def digitfactorial():
    listoffactorial=[]
    for i in range(3,10**6):
        sumoffactorialdigit=sum([factorial(x) for x in digitfetch(i)])
        if sumoffactorialdigit==i:
            listoffactorial.append(i)
    return listoffactorial
if __name__=="__main__":
    listoffactorial=digitfactorial()
    print(listoffactorial)
    print(sum(listoffactorial))
