"""Project Euler Problem 78: Coin partitions

https://projecteuler.net/problem=78
(Copied verbatim from project_euler.ipynb, cell 78.)
"""

# Problem 78: Coin partitions
""" Number partition generating function: https://www.whitman.edu/mathematics/cgt_online/book/section03.03.html 
    Definition of number partition: https://en.wikipedia.org/wiki/Partition_%28number_theory%29 
    Pentagonal number theorem: https://en.wikipedia.org/wiki/Pentagonal_number_theorem """
def coin_partition(module):
    partition = [1]
    n=1
    while True:
        partition.append(0)
        penta = 1
        i = 0
        while penta<=n:
            ### sign of multiplier ###
            if i%4>1:
                sign=-1
            else:
                sign=1
            partition[n]+=sign*partition[n-penta]
            i+=1
            ### pentagonal number ###
            if i&1:
                k=-(i+1)/2
            else:
                k=i/2+1
            penta=int(k*(3*k-1)/2)
        if partition[-1]%module==0:
            break
        else:
            n+=1
    return n
print(coin_partition(int(1e6)))
