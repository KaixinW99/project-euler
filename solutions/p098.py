"""Project Euler Problem 98: Anagramic squares

https://projecteuler.net/problem=98
(Copied verbatim from project_euler.ipynb, cell 98.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 98: Anagramic squares
from collections import defaultdict
def is_square(x: int) -> bool: return not (x**0.5)%1 if x>=0 else False

#* a and b must be anagrams of each other
def max_square_pair(a,b,index,assignments,isdigitused):
    if index == len(a):
        if (a[0] in assignments and assignments[a[0]] == 0) or \
            (b[0] in assignments and assignments[b[0]] == 0): #* leading 0 is not allowed
            return 0
        
        #* calculate all the possible answer
        anum = bnum = 0
        for (x,y) in zip(a,b):
            anum = anum * 10 + assignments[x]
            bnum = bnum * 10 + assignments[y]
        if is_square(anum) and is_square(bnum):
            return max(anum, bnum)
        else:
            return 0
        
    elif a[index] in assignments: #* skip for the repetitive character in the word, e.g., introduction with double "i"
        return max_square_pair(a,b,index+1,assignments,isdigitused)
    else:
        result = 0
        for i in range(10):
            if not isdigitused[i]:
                isdigitused[i] = True
                assignments[a[index]] = i
                result = max(max_square_pair(a,b,index+1,assignments,isdigitused),result)
                #* try other possibilites
                del assignments[a[index]]
                isdigitused[i] = False
        return result

f = open("p098_words.txt", "r")
WORDS = [it[1:-1] for it in f.readline().strip().split(",")] #* del the quotation marks
f.close()

anagrams = defaultdict(list)

#* find all anagrams
for word in WORDS:
    key = "".join(sorted(word))
    anagrams[key].append(word)

ans = 0
for key, words in anagrams.items():
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            assignments = {}
            ans = max(max_square_pair(words[i],words[j],0,assignments,[False]*10), ans)
print(ans)
#! it takes about 12s to run
