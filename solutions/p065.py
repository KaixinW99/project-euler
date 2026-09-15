"""Project Euler Problem 65: Convergents of e

https://projecteuler.net/problem=65
(Copied verbatim from project_euler.ipynb, cell 65.)
"""

# Problem 65: Convergents of e
# we can easily know that the numerator is n{k}=a{k}*n{k-1}+n{k-2}
# the continued fraction of e is [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10,...] from http://oeis.org/A003417
def convergents_of_e(upperbound) -> int:
    k_1 = 2 # index{k-1}
    k_2 = 1 # index{k-2}
    for i in range(2,upperbound+1):
        temp = k_2
        if i%3==0:
            a = int(2*(i/3))
        else:
            a = 1
        k_2 = k_1
        k_1 = int(a*k_2 + temp)
    return int(k_1)
digit_lst = [int(x) for x in list(str(convergents_of_e(100)))] # input greater than 1
digitsum  = sum(digit_lst)
print(digitsum)
