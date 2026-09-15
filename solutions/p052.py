"""Project Euler Problem 52: Permuted multiples

https://projecteuler.net/problem=52
(Copied verbatim from project_euler.ipynb, cell 52.)
"""

# Problem 52: Permuted multiples
from itertools import count # count is a generator, to range(N,inf)
def permut_mul():
    for x in count(start=10):
        digits = sorted(str(2 * x))
        if all(sorted(str(x * k)) == digits for k in range(6, 2, -1)):
            return x
if __name__=="__main__":
    print(permut_mul())
