file = open(r"input4.txt", "r")

lines = file.readlines()

total = 0

for i in lines:
	w=i.strip("\n")
	string = w.split(",")
	first = string[0].split("-")
	print(first)
	a = int(first[0]) # boundary and range numbers are two different things
	b = int(first[1])+1
	second = string[1].split("-")
	print(second)
	c = int(second[0])
	d = int(second[1])+1
	print("set: ", set(range(a,b)) & set(range(c,d)))
	if len (set(range(a,b)) & set(range(c,d))) >0 :
		total +=1
		
		print("total ", total)

print("total ", total)
