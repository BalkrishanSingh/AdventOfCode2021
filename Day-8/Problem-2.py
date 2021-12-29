def get_input(file_name):
    with open(file_name,'r') as f:
        lines = [line for line in f.readlines()]
        signal_patterns = [pattern.split() for pattern in [line.split('|')[0] for line in lines]]
        output_patterns = [pattern.split() for pattern in [line.split('|')[1] for line in lines]]
    return signal_patterns,output_patterns

def mapper(signal_pattern):
    mappings_len = {2:1,4:4,7:8,3:7}
    mappings = {}
    for pattern in signal_pattern: # Finding 1,4,7,8
        if len(pattern) in mappings_len:
            mappings[mappings_len[len(pattern)]] = frozenset(pattern)
    for pattern in signal_pattern:# Finding 3,5,2
        if len(pattern) == 5:
            if frozenset(pattern).issuperset(mappings[1]):#3
                mappings[3] = frozenset(pattern)
            elif frozenset(pattern).issuperset(mappings[4] - mappings[1]):#5
                mappings[5] = frozenset(pattern)
            else:
                mappings[2] = frozenset(pattern)#2
    mappings[9] = frozenset((mappings[1].union(mappings[5])))#9
    mappings[6] = frozenset((mappings[8] - mappings[1]).union(mappings[5])) #6
    for pattern in signal_pattern: #0
        if frozenset(pattern) not in mappings.values():
            mappings[0] = frozenset(pattern)
    mappings = {pattern: digit for digit, pattern in mappings.items()}
    return mappings
def decoder(output_pattern,mappings):
    number = ''
    for pattern in output_pattern:
        if frozenset(pattern) in mappings:
            number += str(mappings[frozenset(pattern)])
    return int(number)
def main():
    answer = 0
    signal_patterns,output_patterns = get_input("./Day-8/input.txt")
    for signal_pattern,output_pattern in zip(signal_patterns,output_patterns):
        mappings = mapper(signal_pattern)
        answer += decoder(output_pattern,mappings)
    return answer
if __name__ == "__main__":
    print(main())