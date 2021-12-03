def  read_binary(file_name):
    clean_data  = []
    with open(file_name,'r+') as f:
        data  = f.readlines()
        for binary in data:
            clean_binary =  [bit for bit in binary.strip()]
            clean_data.append(clean_binary)
    return clean_data

def main():
    binary_data = read_binary('input.txt')
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

