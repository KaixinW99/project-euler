"""Project Euler Problem 84: Monopoly odds

https://projecteuler.net/problem=84
(Copied verbatim from project_euler.ipynb, cell 84.)
"""

# Problem 84: Monopoly odds
#* Monte Carlo Method, for solving the top three ranking problem
#* Markov chain: Math method can help us ranking all the probability of each square
import random

class CardDesk:
    def __init__(self,size) -> None:
        self.index = size
        self.cards = list(range(size))
    
    def next_card(self):
        if self.index == len(self.cards):
            random.shuffle(self.cards)
            self.index = 0
        result = self.cards[self.index]
        self.index += 1
        return result

TRIALS = 10**7
visitcounts = [0]*40

chance = CardDesk(16)
communitychest = CardDesk(16)
consecutivedoubles = 0
location = 0

for i in range(TRIALS):
    # Roll tetrahedral dice
    die0 = random.randint(1,4)
    die1 = random.randint(1,4)
    consecutivedoubles = (consecutivedoubles+1) if die0==die1 else 0
    if consecutivedoubles < 3:
        location = (location + die0 + die1) % 40
    else:
        location = 30
        consecutivedoubles = 0
    
    # Process sctions for some locations
    if location in (7,22,36): # chance
        card = chance.next_card()
        if card == 0: location = 0
        elif card == 1: location = 10
        elif card == 2: location = 11
        elif card == 3: location = 24
        elif card == 4: location = 39
        elif card == 5: location = 5
        elif card in (6,7): # next railway
            location = (location+5)//10%4*10+5
        elif card == 8: # next utility
            location = 28 if (12<location<28) else 12
        elif card == 9: location -= 3
        else: pass
    elif location == 30: # Go to jail
        location = 10
    else: pass

    if location in (2,17,33): # community chest
        card = communitychest.next_card()
        if card == 0: location = 0
        if card == 2: location = 10
    
    visitcounts[location] += 1

temp = sorted(enumerate(visitcounts), key=(lambda ic: ic[1]), reverse=True)
ans = "".join(f"{i:02d}" for (i,c) in temp[:3])
#* 02d formats an integer (d) to a field of min width 2 (2), with zero-padding on the left (leading 0)
# https://stackoverflow.com/questions/36543804/what-does-02d-mean-in-python
print(ans)
