# What is the sum of all of the calibration values?

file = open(r'input.txt', 'r')
numList = []
for i in file:
    nums =[]
    for x in i:
        
        if x.isdigit():
            nums.append(x)
            print(nums)
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