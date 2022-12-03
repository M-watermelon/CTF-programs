#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. 

# find total score given input2.txt
# 1 point for Rock, 2 for Paper, and 3 for Scissors
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

#A for Rock, B for Paper, and C for Scissors.


file = open(r'input2.txt', 'r')
myshoot= 0
result = 0
r = 1
p = 2
s = 3
lose = "X"
draw = "Y"
win = "Z"
scissors = "C" 
paper= "B"
rock = "A"
me = []
opponent = []
total = 0
for i in file:
    input = [*i]
    opponent.append(input[0])
    me.append(input[2])

for i, value in enumerate(opponent):
    if me[i] == lose:
        result = 0
        if opponent[i] == rock:
            myshoot= s
        if opponent[i] == scissors:
            myshoot= p
        if opponent[i] == paper:
            myshoot= r
    if me[i] == win:
        result = 6
        if opponent[i] == rock:
            myshoot= p
        if opponent[i] == scissors:
            myshoot= r
        if opponent[i] == paper:
            myshoot= s
    if me[i] == draw:
        result = 3
        if opponent[i] == rock:
            myshoot= r
        if opponent[i] == scissors:
            myshoot= s
        if opponent[i] == paper:
            myshoot= p
    total = total + myshoot + result


print(total)









# rock = ("A", 1)
# paper = ("B", 2)
# scissors = ("C", 3)
# lose = ("X",0)
# tie = ("Y", 3)
# win = ("Z", 6)
# opponent = []
# me = []
# semitotal = 0
# total = 0

# def score(shape, outcome):
#     global semitotal, total
#     semitotal = shape[2] + outcome
#     total = total + semitotal


# for i in file:
#     input = [*i]
#     opponent.append(input[0])
#     me.append(input[2])

# for i, value in enumerate(opponent):

#     if (value in rock):
#         if (me[i] in tie):
#             score(rock, tie)
#         elif(me[i] in win):
#             score(paper, win)
#         else:
#             score(scissors, lose)
#     elif(value in paper):
#         if (me[i] in tie):
#             score(paper, tie)
#         elif(me[i] in lose):
#             score(rock, lose)
#         else:
#             score(scissors, win)
#     elif(value in scissors) :
#         if (me[i] in lose):
#             score(paper, lose)
#         elif(me[i] in win):
#             score(rock, win)
#         else:
#             score(scissors, tie)




# #print(total)