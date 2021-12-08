def get_input(file_name):
    with open(file_name,'r') as f:
        initial_positions = list(map(int,f.read().split(',')))
    return initial_positions
def calculate_fuel(goal,current_pos):
    fuel_consumption = 0
    if  goal > current_pos :
        fuel_consumption += (goal-current_pos)
    elif goal < current_pos:
        fuel_consumption += (current_pos-goal)
    elif goal == current_pos:
        fuel_consumption += 0
    return fuel_consumption
def main():
    initial_positions = get_input('Day-7/input.txt')
    # initial_positions = [16,1,2,0,4,2,7,1,2,14] #Example input
    fuel_consumption_each_round = [] 
    for goal in initial_positions:
        total_fuel_consumption = 0
        for current_pos in initial_positions:
            total_fuel_consumption += calculate_fuel(goal,current_pos)
        fuel_consumption_each_round.append(total_fuel_consumption)
    return min(fuel_consumption_each_round)
if __name__ == '__main__' :
    print(main())