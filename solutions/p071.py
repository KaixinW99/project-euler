"""Project Euler Problem 71: Ordered fractions

https://projecteuler.net/problem=71
(Copied verbatim from project_euler.ipynb, cell 71.)
"""

# Problem 71: Ordered fractions
# HCF represents highest common factor
""" theory:     p/q < a/b  <=>  pb < aq  <=>  pb <= aq-1  <=>  p <= (aq-1)/b
    condition:  p/q > r/s and p/q is much better
    lowerbound: a/b-p/q = (aq-pb)/bq  <=>  (aq-pb)/bq >= 1/bq 
                p/q is better than r/s  <=>  (as-rb)/bs > (aq-pb)/bq >= 1/bq  <=>  s/(as-rb) < q """
def left_fraction(a,b,q):
    r,s=0,1
    lowerbound = 2
    while q>lowerbound:
        p=int((a*q-1)/b)
        if p*s>r*q:
            r,s=p,q
            lowerbound=s/(a*s-b*r)
        q-=1
    return r,s
if __name__=="__main__":
    numerator,denominator,upperbound=3,7,1000000
    print("Left fraction of {0:d}/{1:d} under precision of denominator {2:d} is {3:d}/{4:d}".format( \
        numerator,denominator,upperbound,*left_fraction(numerator,denominator,upperbound)))
