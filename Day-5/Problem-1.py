import re
class Line:
    def __init__(self,x1,y1,x2,y2) -> None:
        if x1 == x2:
            self.line = [(x1,y) for y in (range(y1,y2+1) if y1 < y2 else range(y2,y1+1))]
        elif y1 == y2:
            self.line = [(x,y1) for x in (range(x1,x2+1) if x1 < x2 else range(x2,x1+1))]
        else:
            self.line = None
    def __repr__(self) -> str:
        return f'{self.line}'
    def __len__(self):
        return len(self.line)
    def __getitem__(self,position):
        return self.line[position]
class Board:
    def __init__(self,x,y):
        self.board = [[0 for i in range(x)] for i in range(y)]
    def add_line(self,Line):
        for point in Line:
            x,y = point
            self.board[y][x] += 1
    def overlapping_line(self):
        count = 0
        for row in self.board:
            for point in row:
                if point >1:
                    count += 1
        return count                
def get_input(file_name):
    with open(file_name,'r') as f:
        lines = []
        for line in f:
            line = line.strip()
            pattern = r',| -> '
            line =  tuple(map(int,re.split(pattern,line)))
            lines.append(line)
    return lines
def get_max(lines):
    max_val  = 0
    for line in lines:
        if max(line) > max_val:
            max_val = max(line)
    return max_val
def main(): 
    points = get_input('./Day-5/input.txt')
    max_x  = max_y = get_max(points)
    lines = [Line(x1,y1,x2,y2) for x1,y1,x2,y2 in points]
    board = Board(max_x,max_y)
    for line in lines:
        if line.line != None:
            board.add_line(line)
    count = board.overlapping_line()
    print(count)
if __name__ == '__main__':
    main()
