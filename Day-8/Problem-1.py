def get_input(file_name):
    with open(file_name,'r') as f:
        signal_patterns = []
        output_val = []
        for line in f:
            input_var = line.split('|')
            signal_patterns.append(input_var[0].split())
            output_val.append(input_var[1].split())
        return output_val
def main():
    output_values = get_input('./Day-8/input.txt')
    values = {2:1,4:4,3:7,7:8}
    count = 0
    for output in output_values:
        for digit in output:
            if len(digit) in values:
                count += 1
    print(count)
if __name__ == "__main__":
    main()