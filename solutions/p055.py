"""Project Euler Problem 55: Lychrel numbers

https://projecteuler.net/problem=55
(Copied verbatim from project_euler.ipynb, cell 55.)
"""

# Problem 55: Lychrel numbers
### that only works for the number smaller than 10000 ###
### 10677 is the first number to be shown to require over 50 iterations (53 iterations) ###
def lychrel(n):
    for i in range(50):
        n+=int(str(n)[::-1])
        if str(n)==str(n)[::-1]:
            return False
    return True
if __name__=="__main__":
    num=0
    for n in range(10000):
        if lychrel(n):
            num+=1
    print(num)
