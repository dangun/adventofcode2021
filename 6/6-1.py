from typing import Counter
REPR_CYCLE = 7
DAYS = 80

def parse_input(filename):
    return list(map(int, open(filename).readline().split(',')))

def build_dictionary(days):
    fish_exp_table = {}
    fish_exp_table[-2] = 0
    fish_exp_table[-1] = 0
    for i in range(0, days + 1):
        fish_count = 0
        for j in range(i - REPR_CYCLE, -1, -REPR_CYCLE):
            fish_count += fish_exp_table[j - 2]
        fish_exp_table[i] = fish_count + 1
    return fish_exp_table

def calculate_total_count(input_counter, fish_exp_table):
    fish_count = 0
    for start_fish in input_counter:
        fish_count += input_counter[start_fish] * fish_exp_table[DAYS + (REPR_CYCLE - start_fish + 1)]
    return fish_count

input_counter = Counter(parse_input('input'))
days = DAYS + (REPR_CYCLE)
fish_exp_table = build_dictionary(days)
solution = calculate_total_count(input_counter, fish_exp_table)
print(f'Answer: {solution}')
