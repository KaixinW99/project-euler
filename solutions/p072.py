"""Project Euler Problem 72: Counting fractions

https://projecteuler.net/problem=72
(Copied verbatim from project_euler.ipynb, cell 72.)
"""

# Problem 72: Counting fractions
""" Combine Euler's totient function and Sieve of Eratosthenes together. (find all coprime pairs)
    Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes 
    Euler's totient function: "https://en.wikipedia.org/wiki/Euler's_totient_function" """
def num_fractions(limit):
    phi=list(range(0,limit+1))
    result=0
    for i in range(2,limit+1):
        if phi[i]==i:
            for j in range(i,limit+1,i):
                phi[j]=int(phi[j]/i*(i-1))  # for each i, do totient function to its multipliers
        result+=phi[i]
    return result
if __name__=="__main__":
    limit=1000000
    print(num_fractions(limit))
