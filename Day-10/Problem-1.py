CORRECT_SYNTAX = {')':'(',
                  ']':'[',
                  '}':'{',
                  '>':'<'}
INCORRECT_SYNTAX_POINTS = {')':3,
                           ']':57,
                           '}':1197,
                           '>':25137}
def get_input(file_name):
    with open(file_name,'r') as f:
        lines =  [line  for line in f]
    return lines
def check_syntax(line):
    symbol_stack = []
    for char in line:
        if char in CORRECT_SYNTAX.values():
            symbol_stack.append(char)
       
        elif symbol_stack and char in CORRECT_SYNTAX.keys():
            if symbol_stack.pop() == CORRECT_SYNTAX[char]:
                continue
            else:
                return char
def main():
    lines = get_input('input.txt')
    score = 0
    for line in lines:
        if result := check_syntax(line):
            score += INCORRECT_SYNTAX_POINTS[result]
    return score
if __name__ == "__main__":
    print(main())

        
