"""Project Euler Problem 28: Number spiral diagonals

https://projecteuler.net/problem=28
(Copied verbatim from project_euler.ipynb, cell 28.)
"""

# Problem 28: Number spiral diagonals
# turn 4 times with each 2 steps, 3 steps and so on
# the counting of matrix is on the odd column/row
def num_spiral(n):
    sumofspiral=1
    position=1
    if n==1:
        return sumofspiral
    for i in range(3,n+1,2): # the matrix
        for j in range(4): # the number in the diagonal
            position+=i-1
            sumofspiral+=position
    return sumofspiral
if __name__=="__main__":
    #print(num_spiral(5))
    print(num_spiral(1001))
