"""Project Euler Problem 37: Truncatable primes

https://projecteuler.net/problem=37
(Copied verbatim from project_euler.ipynb, cell 37.)
"""

# Problem 37: Truncatable primes
# The truncatable primes can only start with 2 3 5 7 and end with 3 5 7
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n/2)+1):
        if n%i==0:
            return False
    return True

def TruncatedNum(n): #start with the pure num
    ltor=rtol=str(n)
    num_set=set([n])
    while len(ltor)>1:
        ltor=ltor[1:]
        num_set.add(int(ltor))
    while len(rtol)>1:
        rtol=rtol[:-1]
        num_set.add(int(rtol))
    return num_set

if __name__=="__main__":
    #print(TruncatedNum(999))
    #print(max(TruncatedNum(999)))
    truncprime_list=[]
    possible_num={2,3,5,7}
    for i in range(11,int(10**6),2):
        if not ((i%10 in possible_num) and (int(str(i)[0]) in possible_num)):
            continue
        numset=TruncatedNum(i)
        for num in numset:
            if not is_prime(num):
                numset.add(0)    ### add 0 to mark the non-truncated prime list
                break
        if not (0 in numset):
            truncprime_list.append(max(numset))
    print(truncprime_list)
    print(sum(truncprime_list))

########## it takes about 43.7s to run. ###########
