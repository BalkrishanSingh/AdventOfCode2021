def read_file(file_name):
    directions = []

    with open(f'{file_name}','r+') as f:
        for line in f:
            temp_list =  tuple(line.split())
            directions.append(temp_list)
    return  directions
def main():
    directions = read_file('./input.txt')
    aim = 0
    horizontal = 0
    depth = 0
    for direction,magnitude in directions:
        if direction == 'down':
            aim += int(magnitude)
        elif direction == 'up':
            aim -= int(magnitude)
        elif direction =='forward':
            horizontal += int(magnitude)
            depth += (aim * int(magnitude))

    print(horizontal*depth)
if __name__ == '__main__':
    main()