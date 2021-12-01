counter = 0

with open('input') as file:
    prev = int(file.readline())
    for line in file:
        depth = int(line)
        if depth > prev:
            counter += 1
        prev = depth

print(counter)