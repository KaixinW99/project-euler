"""Project Euler Problem 87: Prime power triples

https://projecteuler.net/problem=87
(Copied verbatim from project_euler.ipynb, cell 87.)
"""

# Problem 87: Prime power triples
# ! max of prime square below 50e6: 7071
# ! max of prime cube below 50e6  : 368
# ! max of prime fourth power below 50e6: 84
import sympy as Sym
import numpy as np
prime_arr = np.array(list(Sym.sieve.primerange(1,7072)))
sq = prime_arr[prime_arr<=7071] 
cu = prime_arr[prime_arr<=368]
fo = prime_arr[prime_arr<=84]
uplimit = int(50e6)

p_power_triples = set()
for a in sq:
    for b in cu:
        for c in fo:
            tri = a**2+b**3+c**4
            if tri<uplimit:
                p_power_triples.add(tri)
print(len(p_power_triples))
#! or the following
#! p_power_triples = {a**2+b**3+c**4 for a in sq for b in cu for c in fo if a**2+b**3+c**4<uplimit}
