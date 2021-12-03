nums = []
with open('./Input.txt','r') as f:
    for line in f:
        nums.append(int(line))
count = 0
for i,num in enumerate(nums):
    if nums[i-1] < num:
        count +=1
print(count)