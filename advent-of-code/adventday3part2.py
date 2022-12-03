#find the common letter between every three lines
import statistics
from statistics import mode 
file = open(r"input3.txt", "r")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
best = []
letters = []
total = 0
lines = file.readlines()

for i in range(0,len(lines), 3): #iterate every 3 lines
    elf1 = [*lines[i].strip("\n")] # every 3 lines split up into characters
    elf2 = [*lines[i+1].strip("\n")]
    elf3 = [*lines[i+2].strip("\n")]
    for a in elf1:
        if a in elf2 and a in elf3:
            letters.append(a)
    best.append(mode(letters))  
    letters = [] 
print(best, len(best))

for z in best:
    semisum = alphabet.index(z) +1
    total = semisum + total


print(total) 