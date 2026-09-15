"""Project Euler Problem 54: Poker hands

https://projecteuler.net/problem=54
(Copied verbatim from project_euler.ipynb, cell 54.)
"""
import os as _os  # added for the repository layout: data files live in ../data
_os.chdir(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data"))

# Problem 54: Poker hands
import collections as coll
def convert_to_lists(s):
    """
    This function will convert a given
    string to lists with the value of cards
    and the suite of the cards
    Example: '8C TS KC 9H 4S'
    => [['8', 'T', 'K', '9', '4'],['C', 'S', 'C', 'H', 'S']]
    """
    cards = s.split(' ')
    card_value = []
    card_type  = []
    for i in cards:
        card_value.append(i[0])
        card_type.append(i[1])
    return [card_value, card_type]

def high_card(hand):
    """
    This function will return the
    value of highest valued card in the
    given hand
    Example: ['5', '6', 'A', 'J'] => 14('A')
    """
    highest = 0
    for i in hand:
        if i == 'A':
            return 14
        elif i == 'K':
            if 13 >= highest:
                highest = 13
        elif i == 'Q':
            if 12 >= highest:
                highest = 12
        elif i == 'J':
            if 11 >= highest:
                highest = 11
        elif i == 'T':
            if 10 >= highest:
                highest = 10
        elif int(i) > highest:
            highest = int(i)
    return highest

def number_of_pairs(l):
    """
    This function will return the number of pairs
    a given hand has. Also 1 is added to the
    pairs according to the priority list.
    Example: ['5','5','7','6','3'] => 2(one pair)
    ['5','5','6','6','7'] => 3(two pairs)
    ['4','3','Q','K','T'] => 0
    """
    pairs = 0
    for number, degeneracy in coll.Counter(l).items():
        if degeneracy==2:
            pairs += 1
    return pairs

def three_of_a_kind(l):
    """
    This function will return 4 if
    there are three cards of same value.
    Returning of 4 is according to priority list.
    Example: ['5','5','5','T','Q'] => 4
    ['5', '7', 'Q', 'T', 'K'] => 0
    """
    for number, degeneracy in coll.Counter(l).items():
        if degeneracy==3:
            return 3
    return 0

def straight(l):
    """
    This function will return 5
    if all cards are consecutive values.
    Returning 5 is according to priority list.
    Example: ['K', 'Q', 'J', 'T', '9'] => 5
    ['Q', 'T', '3', '2', '1'] => 0
    """
    rating = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: 'T', 9: '9',
              8: '8', 7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2', 1: '1'}
    # highest value of the hand
    hv = high_card(l)
    if rating[hv-1] in l:
        if rating[hv-2] in l:
            if rating[hv-3] in l:
                if rating[hv-4] in l:
                    return 4
    return 0

def flush(v):
    """
    This function will return 6
    if all All cards of the same suit.
    Returning 6 is according to priority list.
    Example: ['S', 'S', 'S', 'S', 'S'] => 6
    ['C', 'C', 'S', 'S', 'D'] => 0
    """
    if len(set(v)) == 1:
        return 5
    return 0

def full_house(l):
    """
    This function will return 7 if
    Three of a kind and a pair.
    Returning 7 is according to priority list.
    Example: ['T', 'T', 'T', 'A', 'A'] => 7
    ['A', '9', '8', 'Q', 'T'] => 0
    """
    if three_of_a_kind(l):
        if number_of_pairs(l) == 1:
            return 6
    return 0

def four_of_a_kind(l):
    """
    This function will return 8
    if Four cards of the same value.
    Returning 8 is according to priority list.
    Example: ['K', 'K', 'K', 'K', '3'] => 8
    ['Q', 'K', 'T', '5', '3'] => 0
    """
    for number, degeneracy in coll.Counter(l).items():
        if degeneracy == 4:
            return 7
    return 0

def straight_flush(l, v):
    """
    This function will return 9
    if All cards are consecutive values of same suit.
    Returning 9 is according to priority list.
    Example:
    ['4', '5', '6', '7', '8']['S', 'S', 'S', 'S', 'S'] => 9
    ['3', '9', 'Q', 'T', '2']['C', 'D', 'H', 'S', 'S'] => 0
    """
    if straight(l) and flush(v):
        return 8
    return 0

def royal_flush(l, v):
    """
    This function will return 10
    if Ten, Jack, Queen, King, Ace, in same suit.
    Returning 10 is according to priority list.
    Example:
    ['T', 'J', 'Q', 'K', 'A']['H', 'H', 'H', 'H', 'H'] => 10
    ['3', 'T', '9', '8', 'A']['S', 'D', 'H', 'S', 'S'] => 0
    """
    if set(['T', 'J', 'Q', 'K', 'A']) == set(l):
        if len(set(v)) == 1:
            return 9
    return 0

def paired_number(l):
    """
    This function will return largest number, if
    there is a pair in the hand. The number returned
    will be in the format of high_card function
    Example: ['5', '5', '6', '7', 'K'] => 5
    ['K', 'K', 'T', 'T', '8'] => 13
    """  
    rating = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
              '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}
    highest = 0
    for number, degeneracy in coll.Counter(l).items():
        if degeneracy==4:
            highest = rating[number]
        elif degeneracy==3:
            highest = rating[number]
        elif degeneracy==2:
            if rating[number] > highest:
                highest = rating[number]
    return highest

f=open("p054_poker.txt","r")
games=f.read()
f.close()

# make a list of hands in each game
two_hands=games.strip("' '\n").split("\n")

# hands list to store the cards and suites of each player for a given game
hands = []

# for loop to convert hand to a list
for i in two_hands:
    # player 1 hand
    fh = convert_to_lists(i[:14])
    # player 2 hand
    sh = convert_to_lists(i[15:])
    hands.append([fh, sh])

# number of times player 1 wins
player1 = 0

# take each game
for i in hands:
    # card values of player 1
    p1v = i[0][0]
    # card values of player 2
    p2v = i[1][0]
    # suites of player 1
    p1s = i[0][1]
    # suites of player 2
    p2s = i[1][1]
    # score of player 1
    p1 = 0
    # score of player 2
    p2 = 0
    # flag for checking the paired cards
    flag = False
    # conditions for player 1
    if number_of_pairs(p1v):
        p1 = number_of_pairs(p1v)
        flag = True
    if three_of_a_kind(p1v):
        p1 = three_of_a_kind(p1v)
        flag = True
    if straight(p1v):
        p1 = straight(p1v)
    if flush(p1s):
        p1 = flush(p1s)
    if full_house(p1v):
        p1 = full_house(p1v)
        flag = True
    if four_of_a_kind(p1v):
        p1 = four_of_a_kind(p1v)
        flag = True
    if straight_flush(p1v, p1s):
        p1 = straight_flush(p1v, p1s)
    if royal_flush(p1v, p1s):
        p1 = royal_flush(p1v, p1s)

    # conditions for player 2
    if number_of_pairs(p2v):
        p2 = number_of_pairs(p2v)
        flag = True
    if three_of_a_kind(p2v):
        p2 = three_of_a_kind(p2v)
        flag = True
    if straight(p2v):
        p2 = straight(p2v)
    if flush(p2s):
        p2 = flush(p2s)
    if full_house(p2v):
        p2 = full_house(p2v)
        flag = True
    if four_of_a_kind(p2v):
        p2 = four_of_a_kind(p2v)
        flg = True
    if straight_flush(p2v, p2s):
        p2 = straight_flush(p2v, p2s)
    if royal_flush(p2v, p2s):
        p2 = royal_flush(p2v, p2s)

    # score more for player 1
    if p1 > p2:
        player1 += 1
    # both players same score
    elif p1 == p2:
        # cards having pairs
        if flag:
            # condition with highest in a pair
            if paired_number(i[0][0]) > paired_number(i[1][0]):
                player1 += 1
            # condition with equal highest in a pair
            elif paired_number(i[0][0]) == paired_number(i[1][0]):
                if high_card(i[0][0]) > high_card(i[1][0]):
                    player1 += 1
        # cards not having pairs
        else:
            if high_card(i[0][0]) > high_card(i[1][0]):
                player1 += 1

# printing number of times player 1 wins
print(player1)
