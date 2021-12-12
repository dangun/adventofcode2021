from collections import defaultdict

paths = defaultdict(set)

with open('input') as file:
    for line in file:
        line = line.strip().split('-')
        paths[line[0]].add(line[1])
        if line[0] != 'start':
            paths[line[1]].add(line[0])

def step(current, visited):
    if current == 'end':
        return 1
    if current.islower():
        visited = visited | {current}
    result = 0
    result += sum(step(node, visited) for node in paths[current] - visited)
    return result

paths = step('start', set())

print(f'Answer: {paths}')
