"""Project Euler Problem 89: Roman numerals

https://projecteuler.net/problem=89
(Copied verbatim from project_euler.ipynb, cell 89.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 89: Roman numerals
ROMAN_NUM_PREFIXES = [
    ("M", 1000),
    ("CM", 900),
    ("D",  500),
    ("CD", 400),
    ("C",  100),
    ("XC",  90),
    ("L",   50),
    ("XL",  40),
    ("X",   10),
    ("IX",   9),
    ("V",    5),
    ("IV",   4),
    ("I",    1),
]

def roman_to_num(s):
    result = 0
    while len(s)>0:
        for (prefix, val) in ROMAN_NUM_PREFIXES:
            if s.startswith(prefix): #! https://www.w3schools.com/python/ref_string_startswith.asp
                result+=val
                s = s[len(prefix):]
                break
    return result
def num_to_roman(n):
    s = ""
    while n>0:
        for (prefix, val) in ROMAN_NUM_PREFIXES:
            if n>=val:
                s+=prefix
                n-=val
                break
    return s

if __name__=="__main__":
    f = open("p089_roman.txt","r")
    roman_l = [line.strip() for line in f.readlines()]
    f.close()
    ans = sum(len(s)- len(num_to_roman(roman_to_num(s))) for s in roman_l)
    print(ans)
