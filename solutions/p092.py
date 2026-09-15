"""Project Euler Problem 92: Square digit chains

https://projecteuler.net/problem=92
(Copied verbatim from project_euler.ipynb, cell 92.)
"""

# Problem 92: Square digit chains
def EndsWith89(n):
    if n==0: return False
    while n!=1 and n!=89:
        s=0
        while n:
            x=n%10
            s+=x*x
            n//=10
        n=s
    return n==89

def SquareDigitChains(cache):
    res=0
    factorials=[sym.factorial(i) for i in range(number_digit+1)]
    for g in range(10):
        for f in range(g+1):
            for e in range(f+1):
                for d in range(e+1):
                    for c in range(d+1):
                        for b in range(c+1):
                            for a in range(b+1):
                                cnt=list(itert.repeat(0,10)) # from 1 to 10
                                dig=[a,b,c,d,e,f,g]
                                SumSqDiCh=0
                                for di in dig:
                                    SumSqDiCh+=di*di
                                    cnt[di]+=1
                                if cache[SumSqDiCh]:
                                    den=1
                                    for ci in cnt:
                                        den*=factorials[ci]
                                    res+=factorials[-1]/den
    return res                            
if __name__=="__main__":
    import sympy as sym
    import itertools as itert
    number_digit=7 # number below 10 million
    cache=[False] # 0 is the first one to be False
    for i in range(1,9*9*7+1):
        cache.append(EndsWith89(i))  ### the question can be simplified to be range from 1 to 9*9*7 (square digit sum of 9999999)
    print(SquareDigitChains(cache))
