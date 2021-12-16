from collections import defaultdict, Counter

polymer = ''
rules = {}
letters = defaultdict(int)

with open('input') as file:
    input = file.read().split('\n\n')
    polymer = input[0]
    for line in input[1].splitlines():
        lhs, rhs = line.split(' -> ')
        rules[lhs] = (lhs[0]+rhs,rhs+lhs[1])

for i in range(len(polymer)-1):
    pairs = {polymer[i:i+2]: 1}

    for _ in range(40):
        next_pairs = defaultdict(int)
        for k, v in pairs.items():
            next_pairs[rules[k][0]] += v
            next_pairs[rules[k][1]] += v
        pairs = next_pairs
    for k, v in pairs.items():
        letters[k[0]] += v
  
letters[polymer[-1]] += 1
c = Counter(letters)
print(f'Answer: {c.most_common()[0][1] - c.most_common()[-1][1]}')