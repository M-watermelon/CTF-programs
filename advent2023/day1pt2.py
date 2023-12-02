digits = {'one': '1', 'two': '2', 'three': '3', 
    'four': '4', 'five': '5', 'six': '6', 
    'seven': '7', 'eight': '8', 'nine':'9' }

file = open(r'input.txt', 'r')
numList = []
for i in file:
    nums =[]
    for x in i:
        
        if x.isdigit():
            nums.append(x)
            print(nums)
        else:
            test = 

    if len(nums)>1:
        num = int(nums[0] + nums[len(nums)-1])
        numList.append(num)
        print(num)
    elif len(nums) == 1:
        num = int(nums[0] + nums[0])
        print(num)
        numList.append(num)
sum = 0
print(numList)
for i in numList:
    sum += i
print(sum)

file.close()