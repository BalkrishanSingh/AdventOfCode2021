class Fish:
    def __init__(self,time:int) -> None:
        self.time = time
    def next_day(self):
        self.time -= 1
    def birth(self):
        self.time = 6
        return Fish(8)
    def __repr__(self) -> str:
        return f'{self.time}'
class School:
    def __init__(self,initial_time_list:list) -> None:
        self.school = []
        for time in initial_time_list:
            self.school.append(Fish(time))
    def next_day(self):
        bucket = []
        for fish in self.school:
            fish.next_day()
            if fish.time == -1:
                bucket.append(fish.birth())
        self.school.extend(bucket)
    def __len__(self):
        return len(self.school)
def get_school(file_name):
    with open(file_name,'r') as f:
        initial_time_list = [int(time) for time in (f.read().split(','))]
    school = School(initial_time_list)
    return school
def main(days):
    school = get_school('./Day-6/input.txt')
    for _ in range(days):
        school.next_day()
    return(len(school))
if __name__ == '__main__':
    fish_amount =  main(80)
    print(fish_amount)
