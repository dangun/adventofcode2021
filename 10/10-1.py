points = {')': 3, ']': 57, '}': 1197, '>': 25137}
bracket_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}

with open('input') as file:
    input = file.readlines()

score = 0
for line in input:
    open_stack = []
    for c in line.strip():
        if c in bracket_dict:
            open_stack.append(c)
        elif bracket_dict[open_stack.pop()] != c:
            score += points[c]
            break

print(f'Answer: {score}')