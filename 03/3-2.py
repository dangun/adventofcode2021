RATING_OXYGEN = 1
RATING_CO2 = 2

def bit_counter(bit_strings, pos):
    counter = 0
    for bit_string in bit_strings:
        if bit_string[pos] == '1':
            counter +=1
        elif bit_string[pos] == '0':
            counter -= 1
    return counter

def find_rating(bit_strings, pos, mode):
    # Stop condition for recursion
    if len(bit_strings) == 1:
        return bit_strings[0]
    # Find most common bit in current pool of bit strings for pos, negative is 0, positive is 1, zero is equal
    bit_count = bit_counter(bit_strings, pos)
    # Eliminate bit strings based on which rating we are calculating
    if mode == RATING_OXYGEN:
        if bit_count >= 0:
            bit_strings = [i for i in bit_strings if i[pos] == '1']
        elif bit_count < 0:
            bit_strings = [i for i in bit_strings if i[pos] == '0']
    elif mode == RATING_CO2:
        if bit_count < 0:
            bit_strings = [i for i in bit_strings if i[pos] == '1']
        elif bit_count >= 0:
            bit_strings = [i for i in bit_strings if i[pos] == '0']
    # Proceed with the recursion, moving up one position
    return find_rating(bit_strings, pos+1, mode)

bit_strings = [i.rstrip() for i in open('input').readlines()]
oxygen_rating = find_rating(bit_strings, 0, RATING_OXYGEN)
co2_rating = find_rating(bit_strings, 0, RATING_CO2)

print(f'Answer: {int(oxygen_rating,2)*int(co2_rating,2)}')