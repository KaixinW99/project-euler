"""Project Euler Problem 62: Cubic permutations

https://projecteuler.net/problem=62
(Copied verbatim from project_euler.ipynb, cell 62.)
"""

# Problem 62: Cubic permutations
# https://www.xarg.org/puzzle/project-euler/problem-62/
import collections as coll
def cubic_permutation(numofperm):
    cubic_perm=coll.defaultdict(list)
    for n in range(1,10000):
        n3=int(n**3)
        tuple_index=tuple(sorted(list(str(n3))))
        cubic_perm[tuple_index].append(n3)
        value=cubic_perm[tuple_index]
        if len(value)==numofperm:
            return value[0]
print(cubic_permutation(5))
