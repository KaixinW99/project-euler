"""Project Euler Problem 75: Singular integer right triangles

https://projecteuler.net/problem=75
(Copied verbatim from project_euler.ipynb, cell 75.)
"""

# Problem 75: Singular integer right triangles
""" Euclid's formula to generate all primitive Pythagorean triplets: https://en.wikipedia.org/wiki/Pythagorean_triple
    Primitive Pythagorean triplets: a= m^2 - n^2 ; b= 2mn ; c= m^2 + n^2 with m > n > 0; m,n coprime; m+n odd """
import numpy as np
def integer_right_tri(limit):
    mlimit = int((limit/2)**0.5) # a+b>c and a+b+c=l --> c<l/2 --> m<sqrt(l/2)
    P_triplets = np.zeros(limit+1,dtype=int)
    for m in range(2,mlimit+1): # m>n>0
        for n in range(1,m):
            if ((m+n)&1) and (np.gcd(m,n)==1):
                a = int(m**2-n**2)
                b = int(2*m*n)
                c = int(m**2+n**2)
                l = a+b+c
                while l<=limit:
                    P_triplets[l]+=1
                    l+=a+b+c # this method can only figure out the primitive Pythagoream triplets, i.e., 3,4,5 instead of 3k, 4k, 5k with respect to k belonging to integer
    return P_triplets
if __name__=="__main__":
    limit = int(15e5)
    singular = np.count_nonzero(integer_right_tri(limit)==1)
    print(singular)
