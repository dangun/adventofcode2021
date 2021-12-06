from typing import Counter
REPR_CYCLE = 7
DAYS = 256

def parse_input(filename):
    input = []
    with open(filename) as file:
        input = list(map(int, file.readline().split(',')))
    return input

def build_dictionary(days):
    # Table with the amount of fish spawned for each day, initialize negative to avoid check in loop
    fish_exp_table = {-2: 0, -1: 0}
    # For each day, add the amount of fish that will have spawned by that day, as well as itself
    for day in range(0, days + 1):
        count = 0
        # Range representing each day a fish will be spawned
        for spawn_day in range(day - REPR_CYCLE, -1, -REPR_CYCLE):
            count += fish_exp_table[spawn_day - 2] # Reduce by 2, to ignore 2 days in first cycle
        fish_exp_table[day] = count + 1
    return fish_exp_table

# Multiply the occurances of every starting fish with the amount of fish it will have spawned
# The day is offset depending on where in the reproduction cycle the fish is
def calculate_total_count(input_counter, fish_exp_table):
    count = 0
    for fish in input_counter:
        count += input_counter[fish] * fish_exp_table[DAYS + (REPR_CYCLE - fish + 1)]
    return count

input_counter = Counter(parse_input('input'))
days = DAYS + REPR_CYCLE
fish_exp_table = build_dictionary(days)
solution = calculate_total_count(input_counter, fish_exp_table)
print(f'Answer: {solution}')
