from itertools import dropwhile

file = open(r'input4.txt', 'r')

card = []
winNums = []
final = 0 

for line in file:
    score = 0
    l = line.strip("\n").split(" ")
    card = l[2:l.index('|')]
    card = list(filter(None, card))
    winNums = l[l.index('|')+1: len(l)]
    winNums =list(filter(None, winNums))
    print("Card is ", card)
    print("WinNums is " , winNums)

    common = list(set(winNums) & set(card))
    print("set is ", common)
    if len(common) != 0:
        score = 1*2**(len(common)-1)
    print("SCORE ", score)
    
    final += score
print(final)