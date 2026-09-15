"""Project Euler Problem 38: Pandigital multiples

https://projecteuler.net/problem=38
(Copied verbatim from project_euler.ipynb, cell 38.)
"""

# Problem 38: Pandigital multiples
def isPandigital(Str):
    if len(Str)!=9:
        return False
    chr="".join(sorted(Str))
    if chr=="123456789":
        return True
    else:
        return False

def Pandig_mul():
    """ 9(1 2 3 4 5) -> 918273645 (9 digits)
        start with 9
        91~98: 2+3+3+3+...<> 9 digits (x)
        912~987: 3+4+4 <> 9 digits (x)
        9123~9876: 4+5 = 9 digits (ok)
        double 1 with 9*2: 9234~9876
        double 9 if second digit >4: 9234~9487"""
    pand_list=[]
    for num in range(9234,9488):
        com=num*(100000+2)
        if isPandigital(str(com)):
            pand_list.append(com)
    return pand_list

if __name__=="__main__":
    pand_list=Pandig_mul()
    print(pand_list)
    print(max(pand_list))
