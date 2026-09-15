"""Project Euler Problem 32: Pandigital products

https://projecteuler.net/problem=32
(Copied verbatim from project_euler.ipynb, cell 32.)
"""

# Problem 32: Pandigital products
# For more details about other languages: https://www.geeksforgeeks.org/pandigital-product/
def PandigitalProduct_1to9(n):
    i = 1
    while i**2<=n:
        if (n%i==0) and (isPandigital(str(n)+str(i)+str(n//i))):
            return True
        i+=1
    return False
def isPandigital(Str):
    if len(Str)!=9:
        return False
    chr="".join(sorted(Str))
    if chr=="123456789":
        return True
    else:
        return False

if __name__=="__main__":
    pandigitalproduct_list=[]
    for i in range(1,int(10**5)):
        if PandigitalProduct_1to9(i):
            pandigitalproduct_list.append(i)
    print(pandigitalproduct_list)
    print(sum(pandigitalproduct_list))
