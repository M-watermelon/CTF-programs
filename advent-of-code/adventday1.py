file = open(r'input.txt', 'r')
valuesList = []
sumsList = []

#file.readline()

for i in file:
    input = i
    if input == "\n":
        sumsList.append(sum(valuesList))
        valuesList = []
    else:
        input = int(input)
        valuesList.append(input)
sumsList.sort()

newlist = []

newlist.append(sumsList[-1])
newlist.append(sumsList[-2])
newlist.append(sumsList[-3])

print(sum(newlist))

file.close()