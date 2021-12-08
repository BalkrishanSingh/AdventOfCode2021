EXAMPLE = [3,4,3,1,2]
def get_time(file_name):
    with open(file_name,'r') as f:
        initial_time_list = [int(time) for time in (f.read().split(','))]
    return initial_time_list
def next_day(fish_counter):
    zero_pos = fish_counter.pop(0)
    fish_counter.append(zero_pos)
    fish_counter[6] += zero_pos
def main(days):
    school_time  =  get_time('./Day-6/Input.txt')
    fish_counter = [0 for i in range(9)]
    for fish_time in school_time:
        fish_counter[fish_time] += 1
    for _ in range(days):
        next_day(fish_counter=fish_counter)
    return sum(fish_counter)  
if __name__ == '__main__':
    fish_amount =  main(256)
    print(fish_amount)