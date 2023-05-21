file = open(r"input8.txt", "r")


lines = file.readlines()

for i in lines:   # i is an individual line
    if lines.index(i)!=0 and lines.index(i)!= len(lines)-1:
        print(lines.index(i) , " ",i)
        for w in i:
            if w
