def read_file(file_name):
    forwards = []
    downs = []
    ups = []
    with open(f'{file_name}','r+') as f:
        for line in f:
            temp_list =  line.split()
            if temp_list[0] == 'forward':
                forwards.append(int(temp_list[1]))
            elif temp_list[0] == 'down':
                downs.append(int(temp_list[1]))
            elif temp_list[0] == 'up':
                ups.append(int(temp_list[1]))
    return  forwards,downs,ups
forwards,downs,ups = read_file('./input.txt')
horizontal = 0
depth = 0
for i in forwards:
    horizontal += i
for i in downs:
    depth += i
for i in ups:
    depth -= i
print(depth*horizontal)
