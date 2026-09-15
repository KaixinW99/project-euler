"""Project Euler Problem 93: Arithmetic expressions

https://projecteuler.net/problem=93
(Copied verbatim from project_euler.ipynb, cell 93.)
"""

# Problem 93: Arithmetic expressions
import re
import itertools as itert
from collections import defaultdict
op = list(itert.product("+-*/",repeat=3))
num= list(itert.combinations("0123456789",4))
brackets = ["a1b2c3d","(a1b)2c3d","a1(b2c)3d","a1b2(c3d)","(a1b)2(c3d)","(a1b2c)3d","((a1b)2c)3d","(a1(b2c))3d","a1(b2c3d)","a1((b2c)3d)","a1(b2(c3d))",]
arith_expr = defaultdict(set)
for n in num:
    n_str = "".join(n)
    n_list = list(itert.permutations(n,4))
    for o in op:
        for e_n in n_list:
            for par in brackets:
                for it in o: par = re.sub(r"[1-3]",it,par,count=1)
                for it in e_n: par = re.sub(r"[a-d]",it,par,count=1)
                try:
                    ans = eval(par)
                except ZeroDivisionError:
                    pass
                if (ans%1==0) and (ans>0): arith_expr[n_str].add(int(ans))

#! Python program to find longest contiguous subsequence
#! https://www.geeksforgeeks.org/longest-consecutive-subsequence/
#! Hashing method
def findLongestConseqSubseq(arr, n, start=None):
    ans = 0
    # Hash all the array elements
    s = set(arr)
    # check each possible sequence from the start
    # then update optimal length
    if start == None:
        for i in range(n):
            # if current element is the starting element of a sequence
            if (arr[i]-1) not in s:
                # Then check for next elements in the sequence
                j = arr[i]
                while (j in s):
                    j += 1
                # update optimal length if this length is more
                ans = max(ans, j-arr[i])
    else:
        j = start
        while (j in s):
            j += 1
        ans = j-start
    return ans
arith_expr_count = {}
for i, it in arith_expr.items():
    arith_expr_count[i]=findLongestConseqSubseq(list(it),len(it),start=1)
print(max(arith_expr_count.items(),key=lambda x: x[1]))
# ! it takes about 40s
