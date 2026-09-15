"""Project Euler Problem 88: Product-sum numbers

https://projecteuler.net/problem=88
(Copied verbatim from project_euler.ipynb, cell 88.)
"""

# Problem 88: Product-sum numbers
# ! minSumProd(k) > k: 1+1+...+1=k and 1*1*...*1=1
# ! minSumProd(k)<=2k: 1+1+...+1+2+k = (k-2)*1+(2+k) = 2k and 1*1*...*1*2*k = 2k
# ! minSumProd(k) is not a prime number
LIMIT = 12000
minSumProd = [None] * (LIMIT+1)
def factorize(n, remain, maxfactor, sum, terms):
    if remain==1:
        terms += n-sum
        if terms<=LIMIT and (minSumProd[terms] is None or n<minSumProd[terms]):
            minSumProd[terms] = n
    else:
        for f in range(2,maxfactor+1):
            if remain%f==0:
                factorize(n, remain//f, min(f,maxfactor), sum+f, terms+1)
for i in range(2, LIMIT*2+1):
    factorize(i,i,i,0,0)
print(sum(set(minSumProd[2:])))
# ! it takes about 15s
