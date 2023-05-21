# find total score given input2.txt
# 1 point for Rock, 2 for Paper, and 3 for Scissors
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

#A for Rock, B for Paper, and C for Scissors.
#X for Rock, Y for Paper, and Z for Scissors.

file = open(r'input2.txt', 'r')
rock = ("A", "X", 1)
paper = ("B", "Y", 2)
scissors = ("C", "Z", 3)
lose = 0
tie = 3
win = 6
opponent = []
me = []
semitotal = 0
total = 0

def score(shape, outcome):
    global semitotal, total
    #print(shape, outcome)         <- debugging
    semitotal = shape[2] + outcome
    total = total + semitotal


for i in file:
    input = [*i]
    opponent.append(input[0])
    me.append(input[2])
#print(opponent)  <- debugging
#print(me)  <- debugging
for i, value in enumerate(opponent):

    if (value in rock):
        if (me[i] in rock):
            score(rock, tie)
        elif(me[i] in paper):
            score(paper, win)
        else:
            score(scissors, lose)
    elif(value in paper):
        if (me[i] in paper):
            score(paper, tie)
        elif(me[i] in rock):
            score(rock, lose)
        else:
            score(scissors, win)
    elif(value in scissors) :
        if (me[i] in paper):
            score(paper, lose)
        elif(me[i] in rock):
            score(rock, win)
        else:
            score(scissors, tie)




print(total)