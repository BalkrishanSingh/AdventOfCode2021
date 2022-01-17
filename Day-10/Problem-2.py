def get_input(file_name):
    with open(file_name,'r') as f:
        lines =  [line  for line in f]
    return lines
def check_syntax(line):
    CORRECT_SYNTAX_CLOSING = {')':'(',
                  ']':'[',
                  '}':'{',
                  '>':'<'}
    symbol_stack = []
    for char in line:
        if char in CORRECT_SYNTAX_CLOSING.values():
            symbol_stack.append(char)
       
        elif symbol_stack and char in CORRECT_SYNTAX_CLOSING.keys():
            if symbol_stack.pop() == CORRECT_SYNTAX_CLOSING[char]:
                continue
            else:
                return char
    if symbol_stack:
        return ''.join(symbol_stack)
def complete_line(incompletion):
    CORRECT_SYNTAX_OPENING = {'(':')',
                  '[':']',
                  '{':'}',
                  '<':'>'}
    completetion = []
    for char in incompletion[::-1]:
        completetion.append(CORRECT_SYNTAX_OPENING[char])
    return ''.join(completetion)
def completion_score(completion):
    SYNTAX_SCORE_VALUES = {')': 1,
                ']': 2,
                '}': 3,
                '>': 4}
    completion_score = 0
    for char in completion:
        completion_score = completion_score * 5 + SYNTAX_SCORE_VALUES[char]
    return completion_score
def middle_score(completion_scores):
    completion_scores = sorted(completion_scores)
    return completion_scores[len(completion_scores)//2]
def main():
    lines = get_input('input.txt')
    incorrections = []
    incompletions = []
    completions = []
    completion_scores = []
    for line in lines:
        if len(result := check_syntax(line)) == 1:
            incorrections.append(result)
        elif len(result) > 1:
            incompletions.append(result)
    for incompletion in incompletions:
        completions.append(complete_line(incompletion))
    for completion in completions:
        completion_scores.append(completion_score(completion))
    return middle_score(completion_scores)
if __name__ == "__main__":
    print(main())