"""Project Euler Problem 61: Cyclical figurate numbers

https://projecteuler.net/problem=61
(Copied verbatim from project_euler.ipynb, cell 61.)
"""

# Problem 61: Cyclical figurate numbers
# The following is a long one.
'''
# the following digit is in range 1000 to 9999
tria = [int(n*(n+1)/2) for n in range(45,141)]
squa = [int(n**2) for n in range(32,100)]
pent = [int(n*(3*n-1)/2) for n in range(26,82)]
hexa = [int(n*(2*n-1)) for n in range(23,71)]
hept = [int(n*(5*n-3)/2) for n in range(21,64)]
octa = [int(n*(3*n-2)) for n in range(19,59)]

# tuples of 4 digit number split into 2-2 digits
tria_div=[(int(str(n)[:2]),int(str(n)[2:])) for n in tria]
squa_div=[(int(str(n)[:2]),int(str(n)[2:])) for n in squa]
pent_div=[(int(str(n)[:2]),int(str(n)[2:])) for n in pent]
hexa_div=[(int(str(n)[:2]),int(str(n)[2:])) for n in hexa]
hept_div=[(int(str(n)[:2]),int(str(n)[2:])) for n in hept]
octa_div=[(int(str(n)[:2]),int(str(n)[2:])) for n in octa]

# all polygonal numbers except octagonal numbers
tsphh = [hept_div, hexa_div, pent_div, squa_div, tria_div]

# function to find the sum of the given tuples
def find_sum(numbers):
    summation = 0
    for num in numbers:
        summation += num[0]*100+num[1]
    print(summation)

# polgon 2
for polygon2 in tsphh:
    # octagonal number tuples will be polygon 1
    for n1 in octa_div:
        # for each number in polygon 2
        for n2 in polygon2:
            # check the cyclicity
            if n1[1] == n2[0]:
                # polygon 3
                for polygon3 in tsphh:
                    # check if we are not using the same polygon again
                    if polygon3 != polygon2:
                        # for each number in polygon 3
                        for n3 in polygon3:
                            # check the cylicity
                            if n2[1] == n3[0]:
                                # polygon 4
                                for polygon4 in tsphh:
                                    if (polygon4 != polygon3 and
                                        polygon4 != polygon2):
                                        for n4 in polygon4:
                                            if n3[1] == n4[0]:
                                                # polygon 5
                                                for polygon5 in tsphh:
                                                    if (polygon5 != polygon4 and
                                                        polygon5 != polygon3 and
                                                        polygon5 != polygon2):
                                                        for n5 in polygon5:
                                                            if n4[1] == n5[0]:
                                                                # polygon 6
                                                                for polygon6 in tsphh:
                                                                    if (polygon6 != polygon5 and
                                                                        polygon6 != polygon4 and
                                                                        polygon6 != polygon3 and
                                                                        polygon6 != polygon2):
                                                                        for n6 in polygon6:
                                                                            if n6[0] == n5[1] and n6[1] == n1[0]:
                                                                                numbers = [n1, n2, n3, n4, n5, n6]
                                                                                find_sum(numbers)
'''

# A more smart one
import itertools as itert
def is_cyclical(i, j):
    return str(i)[2:] == str(j)[:2]
def append_to_list(l, e):
    return_list = []
    for i in l:
        for j in e:
            if is_cyclical(i[-1], j[0]):
                k = i[:]
                k.append(j[0])
                return_list.append(k)
 
    return return_list
def sum_of_cyclical_figurate(figurates):
    for p in itert.permutations([3, 4, 5, 6, 7, 8]):
        cy1 = append_to_list(figurates[p[0]], figurates[p[1]])
        cy2 = append_to_list(cy1, figurates[p[2]])
        cy3 = append_to_list(cy2, figurates[p[3]])
        cy4 = append_to_list(cy3, figurates[p[4]])
        cy5 = append_to_list(cy4, figurates[p[5]])
        for x in cy5:
            if is_cyclical(x[-1], x[0]):
                return sum(x)
figurates = [[]] * 9
figurates[3] = [[n] for n in [i * (i + 1) // 2 for i in range(3, 200)] if 999 < n < 10000]
figurates[4] = [[n] for n in [i ** 2 for i in range(3, 100)] if 999 < n < 10000]
figurates[5] = [[n] for n in [i * (3 * i - 1) // 2 for i in range(5, 100)] if 999 < n < 10000]
figurates[6] = [[n] for n in [i * (2 * i - 1) for i in range(6, 100)] if 999 < n < 10000]
figurates[7] = [[n] for n in [i * (5 * i - 3) // 2 for i in range(7, 100)] if 999 < n < 10000]
figurates[8] = [[n] for n in [i * (3 * i - 2) for i in range(8, 100)] if 999 < n < 10000]
print(sum_of_cyclical_figurate(figurates))
