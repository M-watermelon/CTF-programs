#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
#Find the item type that appears in both compartments of each rucksack. 
#What is the sum of the priorities of those item types?

import statistics
from statistics import mode 

file = open(r"input3.txt", "r")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
best = []

lines = file.readlines()

#print(alphabet)
total = 0

letters = []

# Selecting each individual line of the input
for i in lines:
    #Splitting the line into list of characters
    general = [*i.strip("\n")]
    #Dividing that list between the rucksacks
    ruck1 =  general[:len(general)//2]
    ruck2 =  general[len(general)//2:]

### TO CHECK FOR COMMON LETTERS WHILE PREVENTING REPEATS:
    for a in ruck1:
        if(a in ruck2):
            letters.append(a)
    
    best.append(mode(letters))
    #Empty letters for checking the next line, so that mode() can be used properly
    letters = []

#Letters is the temporary list for common characters which will contain repeats
#Best is the version of letters without the repeats

#300 lines, 300 common items/characters
print(best, len(best))

#totaling everything
for z in best:
    semisum = alphabet.index(z) +1
    total = semisum + total


print(total) 

