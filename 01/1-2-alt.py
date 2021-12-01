# Alternative solution that avoids reading in the entire file at once.
# Only keeps the past 3 values only in a small simulated queue.

counter = 0
window_size = 3

with open('input') as file:
    depths = []
    for i in range(window_size):
        depths.append(int(file.readline()))
    for line in file:
        depth = int(line)
        if depth > depths.pop(0):
            counter += 1
        depths.append(depth)

print(counter)