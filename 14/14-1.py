from collections import Counter, defaultdict

polymer = ''
rules = {}
letters = {}

with open('input') as file:
    input = file.read().split('\n\n')
    polymer = input[0]
    for line in input[1].splitlines():
        lhs, rhs = line.split(' -> ')
        letters[lhs] = rhs
        rules[lhs] = (lhs[0]+rhs,rhs+lhs[1])

counter = defaultdict(int)
def step(current, depth = 0):
    if depth == 10:
        return
    counter[letters[current]] += 1
    next1, next2 = rules[current]
    step(next1, depth+1)
    step(next2, depth+1)

for i in range(len(polymer)-1):
    step(polymer[i:i+2])

for letter in polymer:
    counter[letter] += 1

c = Counter(counter)
print(f'Answer: {c.most_common()[0][1] - c.most_common()[-1][1]}')
