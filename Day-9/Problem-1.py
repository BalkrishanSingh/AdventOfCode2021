def get_input(file_name):
    with open(file_name,'r') as f:
        array = [[int(digit) for digit in line.strip()] for line in f]
    return array
def find_lows(array):
    lows = []
    for line_pos,line in enumerate(array):
        for digit_pos,digit in enumerate(line):
            if (line_pos != 0 and line != array[-1]) and (digit_pos != 0 and digit != array[line_pos][-1]): #For Middle Values
                if all(digit < condition for condition in [
                    array[line_pos + 1][digit_pos],
                    array[line_pos - 1][digit_pos],
                    array[line_pos][digit_pos + 1],
                    array[line_pos][digit_pos - 1]]):
                    lows.append(digit)
            elif (line_pos == 0 or line == array[-1])and (digit_pos != 0 and digit != array[line_pos][-1]): #For Uppermost and Lowermost line excluding corners
                if line_pos == 0:
                    if all(digit < condition for condition in [
                        array[line_pos + 1][digit_pos],
                        array[line_pos][digit_pos + 1],
                        array[line_pos][digit_pos - 1]]):
                        lows.append(digit)
                elif line == array[-1]:
                    if all(digit < condition for condition in [
                        array[line_pos - 1][digit_pos],
                        array[line_pos][digit_pos + 1],
                        array[line_pos][digit_pos - 1]]):
                        lows.append(digit)
                        
            elif (digit_pos == 0 or digit == array[line_pos][-1]) and (line_pos == 0 or line == array[-1]):#For Uppermost and Lowermost lines including corners
                if digit_pos == 0:
                        if line_pos == 0:
                            if all(digit < condition for condition in [
                                array[line_pos + 1][digit_pos],
                                array[line_pos][digit_pos + 1]]):
                                lows.append(digit)
                        elif line == array[-1]:
                            if all(digit < condition for condition in [
                                array[line_pos - 1][digit_pos],
                                array[line_pos][digit_pos + 1]]):
                                lows.append(digit)
                elif digit == array[line_pos][-1]:
                        if line_pos == 0:
                            if all(digit < condition for condition in [
                                array[line_pos + 1][digit_pos],
                                array[line_pos][digit_pos - 1]]):
                                lows.append(digit)
                        elif line == array[-1]:
                            if all(digit < condition for condition in [
                                array[line_pos - 1][digit_pos],
                                array[line_pos][digit_pos - 1]]):
                                lows.append(digit)
            elif (digit_pos == 0 or digit == array[line_pos][-1]) and (line_pos != 0 or line != array[-1]):#For Leftmost and Rightmost columns.
                if digit_pos == 0:
                    if all(digit < condition for condition in [
                        array[line_pos + 1][digit_pos],
                        array[line_pos - 1][digit_pos],
                        array[line_pos][digit_pos + 1]]):
                        lows.append(digit)
                elif digit_pos == 0:
                    if all(digit < condition for condition in [
                        array[line_pos + 1][digit_pos],
                        array[line_pos - 1][digit_pos],
                        array[line_pos][digit_pos - 1]]):
                        lows.append(digit)
    return lows
def main():
    array = get_input('input.txt')
    lows = find_lows(array)
    risk_values = [(low + 1) for low in lows]
    return sum(risk_values)
if __name__ == "__main__":
    print(main())
        
    
