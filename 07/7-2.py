import math

with open('input') as file:
    input = [int(i) for i in file.readline().split(',')]

# Find mean, then find the two potentials for lowest fuel and compare them
mean = sum(i for i in input)/len(input)
mean_f = math.floor(mean)
fuel_f = sum((abs(mean_f - i) ** 2 + abs(mean_f - i)) / 2 for i in input)
mean_c = math.ceil(mean)
fuel_c = sum((abs(mean_c - i) ** 2 + abs(mean_c - i)) / 2 for i in input)
answer = int(min(fuel_f, fuel_c))

print(f'Answer: {answer}')