"""Project Euler Problem 46: Goldbach's other conjecture

https://projecteuler.net/problem=46
(Copied verbatim from project_euler.ipynb, cell 46.)
"""

# Problem 46: Goldbach's other conjecture
# verify n=p+2k^2, to make it more quicker, you can check k
# Sieve of Eratosthenes methods
# for more details, please check https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def Sieve_of_Eratosthenes(prime):
    prime[1]=0 # 1 is not taken into account
    l = len(prime)
    for i in range(2,l):
        for j in range(i*i,l,i): #like the 9*9 multiply table
            prime[j]=0

def Goldbach(lim):
    prime=list(range(int(lim)+1))
    Sieve_of_Eratosthenes(prime)
    #print(prime)
    for n in range(9,len(prime),2):
        if prime[n]==0:
            #print(n)
            k=1
            wit=False
            while 2*k*k<n:
                if prime[int(n-2*k*k)]!=0:
                    wit=True
                    break
                k+=1
            if not wit:
                return n

if __name__=="__main__":
    print(Goldbach(int(10**6)))
