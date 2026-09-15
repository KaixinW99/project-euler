"""Project Euler Problem 35: Circular primes

https://projecteuler.net/problem=35
(Copied verbatim from project_euler.ipynb, cell 35.)
"""

# Problem 35: Circular primes
# Sieve of Sundaram to sieve the prime number: https://en.wikipedia.org/wiki/Sieve_of_Sundaram
# more detailed info about other language: https://www.geeksforgeeks.org/circular-primes-less-than-n/
def sieve_of_Sundaram(n):
    k = (n-2)//2
    integers_list=[True]*(k+1)
    for i in range(1,k+1):
        j=i
        while i+j+2*i*j<=k:
            integers_list[i+j+2*i*j]=False
            j+=1
    return integers_list # it can be muted
    '''
    if n>2:
        print(2,end=' ')
    for i in range(1,k+1):
        if integers_list[i]:
            print(2*i+1,end=' ')
    '''
def Countdigit(n):
    digit=0
    while n!=0:
        n//=10
        digit+=1
    return digit
def Rotate(n):
    rem=n%10
    rem=rem*(10**(Countdigit(n)-1))
    n//=10
    n+=rem
    return n

def CircularPrime(n):
    integers_list=sieve_of_Sundaram(n)
    circularprime_list=[2]  # 2 is not included in sieve of sundaram
    for i in range(1,len(integers_list)):
        if integers_list[i]==False:
            continue
        num=Rotate(2*i+1)
        while num!=2*i+1:
            if num%2==0:
                break
            if integers_list[(num-1)//2]:
                num=Rotate(num)
            else:
                break
        if num==2*i+1:
            circularprime_list.append(num)     
    return circularprime_list  

if __name__=="__main__":
    #sieve_of_Sundaram(2000)
    #print(Rotate(971))
    circularprime=CircularPrime(int(10**6))
    print(len(circularprime))
