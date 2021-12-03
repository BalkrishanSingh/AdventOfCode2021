nums = []
with open('./Input.txt','r') as f:
    for line in f:
        nums.append(int(line))
count = 0

#method 1
# matrix = [nums[i:i+3] for i in range(len(nums)-2)]
# for i,vector in enumerate(matrix):
#     if sum(vector) > sum(matrix[i-1]):
#         count += 1


#method 2
matrix = []
for i in range(0,len(nums)):
    if  i != len(nums) - 2:
        vector = nums[i:i+3]
        matrix.append(vector)
for i,vector in enumerate(matrix):
    if sum(vector) > sum(matrix[i-1]):
        count +=1
print(count)