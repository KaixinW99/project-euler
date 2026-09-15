"""Project Euler Problem 30: Digit fifth powers

https://projecteuler.net/problem=30
(Copied verbatim from project_euler.ipynb, cell 30.)
"""

# Problem 30: Digit fifth powers
def digitfetch(i):
    listofdigit=[]
    while i>0:
        listofdigit.append(i%10)
        i//=10
    return listofdigit

def digitpower(n):
    listofpower=[]
    for i in range(2,int(10**(n+1))):
        sumofpowerdigit=sum([x**n for x in digitfetch(i)])
        if sumofpowerdigit == i:
            listofpower.append(i)
    return listofpower
if __name__=="__main__":
    power5=digitpower(5)
    print(power5)
    print(sum(power5))
# I don't know whether there are some other big numbers
