"""Project Euler Problem 59: XOR decryption

https://projecteuler.net/problem=59
(Copied verbatim from project_euler.ipynb, cell 59.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 59: XOR decryption
# XOR: same bits -> False; different bits --> True

f=open("p059_cipher.txt","r")
cipher=[int(x) for x in f.read().strip("\n").split(",")]
f.close()

### brute force all possible keys ###
def brute_force(cipher):
    def check_english(xor):
        """check whether that is the English word (lowercase 32~90; uppercase 97~122)"""
        if 32<=xor<=122 and xor!=96: ### after giving out a lot of wrong one, "`" (ASCII 96) is not included in 
            return True
        else:
            return False
    def decrypt(w,key):
        """take the w xor key to find the real solution"""
        return "".join(chr(a^ord(b)) for a,b in zip(a,b))

    for i in range(97,123):
        for j in range(97,123):
            for k in range(97,123):
                decode=[]
                t=[i,j,k]
                for p in range(len(cipher)):
                    c=t[p%3]^cipher[p]
                    if not check_english(c):
                        break
                    decode.append(c)
                if len(decode)==len(cipher):
                    plain_text=list(map(chr,decode))
                    print("".join(plain_text))
                    print("Sum of all ASCII is %i"%sum(decode))
                    print("Keys are",*t)

print("### Brute Force ###")
brute_force(cipher)
print("-"*36)

### analyze the frequency of characters ###
def most_freq_char(cipher):
    import itertools as itert
    def guess(cipher, keylength):
        freq=[]
        length=len(cipher)
        key=list(itert.repeat(0,keylength))
        for i in range(keylength):
            freq.append(list(itert.repeat(0,length)))
        for i in range(length):
            k=i%keylength
            freq[k][cipher[i]]+=1
            ### Method 1: compare during the loop ###
            if freq[k][cipher[i]] > freq[k][key[k]]:
                key[k]=cipher[i]
        '''
        ### Method 2: find the maximum frequecy ###
        for i in range(keylength):
            key[i]=freq[i].index(max(freq[i]))
        '''
        return list(map(lambda a: a^32, key))
    keylength=3
    key = guess(cipher,keylength)
    decode=[cipher[c]^key[c%keylength] for c in range(len(cipher))]
    plain_text=list(map(chr,decode))
    print("".join(plain_text))
    print("Sum of all ASCII is %i"%sum(decode))
    print("Keys are",*key)

print("### check the frequency of character ('space' is the most common in the sentence) ###")
most_freq_char(cipher)
