"""Project Euler Problem 90: Cube digit pairs

https://projecteuler.net/problem=90
(Copied verbatim from project_euler.ipynb, cell 90.)
"""

# Problem 90: Cube digit pairs
SQUARES = [divmod(i*i,10) for i in range(1,10)] #* divmod provides both quotient and remainder
#print(SQUARES)
def test_bit(x,i): return ((x>>i)&1) #* test whether the number i is in the set
def is_arrangement_valid(a,b):
    if test_bit(a,6) or test_bit(a,9):
        a |= (1<<6) | (1<<9)    #* either 6 or 9 in the set would consider the same
    if test_bit(b,6) or test_bit(b,9):
        b |= (1<<6) | (1<<9)    #* either 6 or 9 in the set would consider the same
    return all( (test_bit(a,c) and test_bit(b,d)) or (test_bit(a,d) and test_bit(b,c)) for (c,d) in SQUARES)
def hamming(x: int) -> int: return bin(x).count("1") #* Hamming weight: counting the number of 1's in binary representation
ans = sum(1
        for i in range(1<<10)
        for j in range(i,1<<10) #* force the dice to be orderless
        if (hamming(i)==hamming(j)==6) and (is_arrangement_valid(i,j))
        )
print(ans)
