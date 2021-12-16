from math import prod

with open('input') as file:
    input = file.read().strip()

greater_than = lambda values: 1 if values[0] > values[1] else 0
less_than = lambda values: 1 if values[0] < values[1] else 0
equal_to = lambda values: 1 if values[0] == values[1] else 0

op_dict = {0: sum, 1: prod, 2: min, 3: max, 5: greater_than, 6: less_than, 7: equal_to }

binlen = len(input)*4
input = bin(int(input, 16))[2:].zfill(binlen)

def read(p, x, input):
    output = input[p:p+x]
    p += x
    return p, output

def read_packet(input, p, max_read = -1):
    sub_read = 0
    values = []
    values_to_op = []
    while len(input) - 10 > p and not max_read == sub_read:
        p, version = read(p, 3, input)
        version = int('0b' + version, base = 0)
        p, packet_type = read(p, 3, input)
        packet_type = int('0b' + packet_type, base = 0)
        if packet_type == 4:
            literals = []
            last = False
            while not last:
                p, last = read(p, 1, input)
                last = last == '0'
                p, literal = read(p, 4, input)
                literals.append(literal)
            values.append(int("0b" +"".join(literals), base = 0))
                
        elif packet_type != 4:
            p, length_type_id = read(p, 1, input)
            if length_type_id == '0':
                p, length = read(p, 15, input)
                length = int('0b' + length, base = 0)
                p_add, new_values = read_packet(input[p:p+length], 0)
                values_to_op.extend(new_values)
                p += length
            else:
                p, num_sub = read(p, 11, input)
                num_sub = int('0b' + num_sub, base = 0)
                p_add, new_values = read_packet(input[p:], 0, max_read = num_sub)
                values_to_op.extend(new_values)
                p += p_add

            values += [op_dict[packet_type](values_to_op)]
            values_to_op = []
        sub_read += 1
    return p, values

result = read_packet(input, 0)[1][0]
print(f'Answer: {result}')