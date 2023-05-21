#After the rearrangement procedure completes, 
#what crate ends up on top of each stack?

# move # of crates
# from OG LOCATION
# to NEW LOCATION

file = open(r"input5.txt", "r")
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8 =[]
list9=[]


lines = file.readlines()

total = 0


for i in lines:
    templist = []
    w = i.strip("\n")
    for x in w:
        templist.append(x)
    for a in templist:
        if a == " ":
            pass
        else:
            if a == 0:
                list1.append[a]
            if a == 1:
                list2.append[a]
            if a == 2:
                list3.append[a]
            if a== 3:
                list4.append[a]
            if a == 4:
                list5.append[a]
            if a ==5:
                list6.append[a]
            if a ==6:
                list7.append[a]
            if a ==7:
                list8.append[a]
            if a ==8:
                list9.append[a]

print(list2)



file = open(r"input5.txt", "r")

lines = file.readlines()