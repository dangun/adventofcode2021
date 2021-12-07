with open('input') as file:
    input = sorted([int(i) for i in file.readline().split(',')])

# If the length is even, then there are two median values, check both and compare
if len(input) % 2 == 0:
    median_high = input[int(len(input)/2)]
    median_low = input[int(len(input)/2 - 1)]
    fuel = min(sum(abs(median_high - i) for i in input), sum(abs(median_low - i) for i in input))
else:
    median = input[int(len(input)/2)]
    fuel = sum(abs(median - i) for i in input)

print(f'Answer: {fuel}')