"""Project Euler Problem 22: Names scores

https://projecteuler.net/problem=22
(Copied verbatim from project_euler.ipynb, cell 22.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 22: Names scores
alphabet_dict = {"a":1,"b":2,"c":3,"d":4,"e":5, \
    "f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12, \
    "m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19, \
    "t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
f=open('p022_names.txt','r')
strlist=f.readline().strip(' " " ').split('","')
f.close()
strlist.sort()
#print(strlist)
#print(strlist.index("COLIN"))
sum_tot = 0
for i,item in enumerate(strlist):
    sum_num = 0
    for letter in item.lower():
        sum_num+=alphabet_dict[letter]
    sum_tot+=(i+1)*sum_num
print(sum_tot)
