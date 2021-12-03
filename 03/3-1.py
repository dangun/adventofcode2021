common_bits = [0]*12

with open('input') as file:
    for line in file:
        for i, bit in enumerate(line.rstrip()):
            if bit == '0':
                common_bits[i] -= 1
            elif bit == '1':
                common_bits[i] += 1

# Equal amount of 0s and 1s treated as 0 being most common
gamma_rate = ''.join(['1' if bit > 0 else '0' for bit in common_bits])
epsilon_rate = ''.join(['0' if bit >= 0 else '1' for bit in common_bits])

print(f'Answer: {int(gamma_rate, 2)*int(epsilon_rate, 2)}')