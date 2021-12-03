def get_input(file_name):
    with open(file_name,'r') as f:
        data  = [line.strip() for line in f]
        binary_list =[[x for x in bin_num] for bin_num in data]
        return binary_list
def get_common(bin_list,bin_pos):
    zeros = len([ x[bin_pos]  for x in bin_list if x[bin_pos]== '0'])
    ones = len([ x[bin_pos]  for x in bin_list if x[bin_pos]== '1'])
    if zeros > ones:return ('0','1')#first pos is most common and second is least common
    elif ones > zeros:return ('1','0')
    else:return ('1','0')
def list_bin_converter(bin_list):
    binary_num = ''
    for bit in bin_list:
        binary_num += bit
    return int(binary_num,2)
    
def oxy_and_carb(bin_data,common,bin_pos):
    oxygen = [x for x in bin_data if x[bin_pos] == common[0]]
    carbon = [x for x in bin_data if x[bin_pos] == common[1]]
    return oxygen,carbon
def oxy(oxy_list,common,bin_pos):
    oxygen = [x for x in oxy_list if x[bin_pos] == common[0]]
    return oxygen
def carb(carb_list,common,bin_pos):
    carbon = [x for x in carb_list if x[bin_pos] == common[1]]
    return carbon


def main():
    bin_data = get_input('Day-3/input.txt')
    bin_common = get_common(bin_data,0)
    oxygen_list,carbon_list = oxy_and_carb(bin_data,bin_common,0)
    result = []
    
    for bin_pos in range(1,13):
        # for oxygen in oxygen_list:
        if len(oxygen_list) == 1:
            result.append(oxygen_list[0])
            break
        else:
            oxy_common = get_common(oxygen_list,bin_pos)
            oxygen_list = oxy(oxygen_list,oxy_common,bin_pos)
        
    for bin_pos in range(1,13):
        # for carbon in carbon_list:
        if len(carbon_list) == 1:
            result.append(carbon_list[0])
            break
        else:
            carb_common = get_common(carbon_list,bin_pos)
            carbon_list = carb(carbon_list,carb_common,bin_pos)
    if len(result) == 2 : return result
        
if __name__ == '__main__':
    oxygen,carbon = main()
    oxy_gen,co2_scrubber = list_bin_converter(oxygen),list_bin_converter(carbon)
    print(oxy_gen*co2_scrubber)