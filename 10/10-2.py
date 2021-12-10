from functools import reduce

points = {'(': 1, '[': 2, '{': 3, '<': 4}
bracket_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}

with open('input') as file:
    input = file.readlines()

scores = []
for line in input:
    open_stack = []
    corrupt = False
    for c in line.strip():
        if c in bracket_dict:
            open_stack.append(c)
        elif corrupt := (bracket_dict[open_stack.pop()] != c):
            break

    if not corrupt:
        scores.append(reduce(lambda score, x: score * 5 + x, (points[x] for x in open_stack[::-1])))

scores.sort()
print(f'Answer: {scores[int(len(scores)/2)]}')