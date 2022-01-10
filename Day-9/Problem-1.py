def get_input(file_name):
    with open(file_name,'r') as f:
        array = [[int(digit) for digit in line.strip()] for line in f]
    return array
def get_adjacent(x,y,array_height,array_width):
    adjacent_points = []
    if x > 0:
        adjacent_points.append((x-1,y))
    if x < array_width - 1:
        adjacent_points.append((x+1,y))
    if y > 0:
        adjacent_points.append((x,y-1))
    if y < array_height - 1:
        adjacent_points.append((x,y+1)) 
    return adjacent_points
def is_low(x,y,array,array_height,array_width):
    height = array[y][x]
    adjacent_points = get_adjacent(x,y,array_height,array_width)
    for (x,y) in adjacent_points:
        if height >= array[y][x]:
            return False
    else:
        return True
def main():
    array = get_input('input.txt')
    array_height,array_width = len(array),len(array[0])
    lows = []
    for y,row in enumerate(array):
        for x,height in enumerate(row):
            if is_low(x,y,array,array_height,array_width):
                lows.append(height)
    risk_values = [(low + 1) for low in lows]
    return sum(risk_values)
if __name__ == "__main__":
    print(main())