"""Project Euler Problem 36: Double-base palindromes

https://projecteuler.net/problem=36
(Copied verbatim from project_euler.ipynb, cell 36.)
"""

# Problem 36: Double-base palindromes
def dec_bin_palindrome(n):
    decstr=str(n)
    binstr="{0:b}".format(n)   #bin(n)[2:]
    if decstr==decstr[::-1] and binstr==binstr[::-1]:
        return True
    else:
        return False
if __name__=="__main__":
    dipalindrome_sum=0
    for i in range(int(10**6)):
        if dec_bin_palindrome(i):
            dipalindrome_sum+=i
    print(dipalindrome_sum)
