#In how many assignment pairs does one range fully contain the other?

file = open(r"input4.txt", "r")

lines = file.readlines()

total = 0

for i in lines:
	w=i.strip("\n")
	string = w.split(",")
	first = string[0].split("-")
	print(first)
	a = int(first[0])-1 # boundary and range numbers are two different things
	print(a)
	b = int(first[1])+1
	print(b)
	second = string[1].split("-")
	print(second)
	c = int(second[0])-1
	print(c)
	d = int(second[1])+1
	print(d)

	if set((range(a,b))).issubset(range(c,d)) or set((range(c,d))).issubset(range(a,b)):
		total +=1
		
		print("total ", total)

print("total ", total)



