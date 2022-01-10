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
def get_adj_basin_points(x,y,array,array_height,array_width):
    adj_points = get_adjacent(x,y,array_height,array_width)
    adj_basin_points = []
    for (x,y) in adj_points:
        if array[y][x] < 9:
            adj_basin_points.append((x,y))
    return adj_basin_points
def get_basin_points(x,y,array,array_height,array_width,basin_points=[]):
    basin_points = list(basin_points)
    basin_points.append((x,y))
    adj_basin_points = get_adj_basin_points(x,y,array,array_height,array_width)
    for (x,y) in adj_basin_points:
        if (x,y) not in basin_points:
            basin_points = (get_basin_points(x,y,array,array_height,array_width,basin_points))
    return basin_points    
def get_multiple_of_three_largest(basin_sizes):
    multiple_of_three_largest = 1
    length = len(basin_sizes)
    for i in range(length-1):
        for j in range(length-i-1):
            if basin_sizes[j] < basin_sizes[j+1]:
                basin_sizes[j],basin_sizes[j+1] = basin_sizes[j+1],basin_sizes[j]
    for basin_size in basin_sizes[:3]:
        multiple_of_three_largest *= basin_size
    return multiple_of_three_largest
def main():
    array = get_input('input.txt')
    array_height,array_width = len(array),len(array[0])
    lows = []
    basins = []
    for y,row in enumerate(array):
        for x,height in enumerate(row):
            if is_low(x,y,array,array_height,array_width):
                lows.append((x,y))
    for low in lows:
        x,y = low
        basins.append(get_basin_points(x,y,array,array_height,array_width))
    basin_sizes = [len(basin) for basin in basins]
    return get_multiple_of_three_largest(basin_sizes)

if __name__ == "__main__":
    print(main())