
with open('input') as file:
    input = file.read().strip()

binlen = len(input)*4
input = bin(int(input, 16))[2:].zfill(binlen)

def read(p, x, input):
    output = input[p:p+x]
    p += x
    return p, output

def read_packet(input, p, max_read = -1):
    vers_count = 0
    sub_read = 0
    while len(input) - 10 > p and not max_read == sub_read:
        p, version = read(p, 3, input)
        version = int('0b' + version, base = 0)
        vers_count += version
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
        elif packet_type != 4:
            p, length_type_id = read(p, 1, input)
            if length_type_id == '0':
                p, length = read(p, 15, input)
                length = int('0b' + length, base = 0)
                p_add, vers_add = read_packet(input[p:p+length], 0)
                vers_count += vers_add
                p += length
            else:
                p, num_sub = read(p, 11, input)
                num_sub = int('0b' + num_sub, base = 0)
                p_add, vers_add = read_packet(input[p:], 0, max_read=num_sub)
                vers_count += vers_add
                p += p_add
        sub_read += 1
    return p, vers_count

vers_count = read_packet(input, 0)[1]
print(f'Answer: {vers_count}')