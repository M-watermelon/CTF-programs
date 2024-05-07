file = open(r'input4.txt', 'r')

card = []
winNums = []
final = 0 
full = [] # original list
winners = []
num = 0
totalWinners = 0
fixedList = [] # modified list with copies
lenWinners = []

for line in file:
    score = 0
    l = line.strip("\n").split(" ")
    full.append(l)

for i in full:
    num+=1
    card = list(filter(None, i[2:i.index('|')])) # make list of cards
    winNums =list(filter(None, i[i.index('|')+1: len(i)]))  # make list of winning numbers
    #print("Card is ", card)
    #print("WinNums is " , winNums)

    common = list(set(winNums) & set(card))
    #print("set is ", common)

    if len(common) != 0:  # winners
        totalWinners = len(common)
        winners.append(num)
        lenWinners.append(totalWinners)

fixedList = full
for i in winners: # i is the line number of the winning card
    for x in range(1,lenWinners[winners.index(i)]+1): # up to winning number
        print(i, x)
        if x + i < 202:
            fixedList.insert(i+x,full[x + i])
            print("next is ",full[x + i])


#print(full)
totalWinners = 0
for i in fixedList:
    card = list(filter(None, i[2:i.index('|')])) # make list of cards
    winNums =list(filter(None, i[i.index('|')+1: len(i)]))  # make list of winning numbers
    new = list(set(winNums) & set(card))
    #print(i, card)
    if len(new) != 0:
        totalWinners+=1

    
print("total winners = ", totalWinners)
print(winners)
print(lenWinners)
#print(fixedList)

######

