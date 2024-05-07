file = open(r'input8.txt', 'r')

instructions = 'LRLRLRLLRRLRRLRRRLRRLRLLRRRLRRRLRRLLLLRRRLRLLRRLRRLRRLLLRRRLRRRLRRLRLRRLRLRLRLLRRRLRRRLLRRRLRRRLRRRLRLLLRRLRLRRRLRLRRRLLRRRLRLLRLRRRLRLRRRLRRLLRLRLRRLRLRLRRLRLRLRRRLRRLRLLRRLRRRLRRRLRRLRRRLRRLRLRRRLLRRRLLRRLRLRRRLRRRLLRRRLRLRRLRLRLRRLRLLRRLRLRLRRLRRRLRRRLRLRRLRRLLLRRRLLRLRRRLLRRRR'
instructions = [*instructions]
print(instructions)


#for loop to go thru lines and create dictionary

   #  start with first line
key = dictionary[first loc]
steps =0
def searcher():
    for i in instructions:
        if key == "ZZZ":
            return steps
   # access dictionary entry at key
   # 
   # if i = l access value [0]:
   # set key = accessed value
   # if i = r access value [1]:
   # set key = accessed value
        steps +=1