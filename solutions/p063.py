"""Project Euler Problem 63: Powerful digit counts

https://projecteuler.net/problem=63
(Copied verbatim from project_euler.ipynb, cell 63.)
"""

# Problem 63: Powerful digit counts
### that is quite similar to problem 25 ###
# L(n^k) = k -> k = floor(1+log(n^k,base=10)) -> k-1 <= log(n^k,base=10) < k
# log(n^k,base=10) < k -> n<10
# k-1 <= log(n^k,base=10) -> k < log(10,base=10/n) < log(10,base=10/9) ~ 21.85
# and it is k=floor(log(10,base=10/n)), the number of possible solution
import math
def PowerDigitCount():
    c=0
    for n in range(1,10):
        c+=math.floor(1/math.log10(10/n))
    return c
if __name__=="__main__":
    print(PowerDigitCount())
