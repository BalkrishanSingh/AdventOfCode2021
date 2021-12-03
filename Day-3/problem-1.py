def get_input(file_name):
    with open(file_name,'r') as f:
        data  = [line.strip() for line in f]
        binary_list =[[x for x in bin_num] for bin_num in data]
        return binary_list

def main():
    binary_data = get_input('./Day-3/input.txt')
    binary_len = len(binary_data[0])
    epsilon = '0b'
    gamma = '0b'
    for bit_pos in range(binary_len):
        zeros = 0
        ones = 0
        for binary in binary_data:
            if binary[bit_pos] == '0':
                zeros += 1
            elif binary[bit_pos] == '1':
                ones += 1
        if zeros > ones:
            gamma += '0'
            epsilon += '1'
        elif ones > zeros:
            gamma += '1'
            epsilon += '0'
    power_consumption = eval(epsilon) * eval(gamma)
    return power_consumption
if __name__ == '__main__':
    print(main()) 

