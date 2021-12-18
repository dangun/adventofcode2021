from math import sqrt, ceil

with open('input') as file:
    x, y = file.read().strip().split(':')[1].split(',')
    x_bound = tuple(map(int, x.split('=')[1].split('..')))
    y_bound = tuple(map(int, y.split('=')[1].split('..')))

x_low = ceil((sqrt(1 + (x_bound[0] * 8)) - 1) / 2)
x_high = x_bound[1]
y_low = y_bound[0]
y_high = -y_bound[0]

probe_dict = {}
x_skip = set(range((ceil(x_bound[1] / 2)) + 1, x_bound[0]))
for x in range(x_low, x_high + 1):
    if x in x_skip: continue
    for y in range(y_low, y_high):
        x_pos = y_pos = y_highest = 0
        x_vel = x
        y_vel = y
        target_hit = False
        passed_target = False
        while not passed_target:
            x_pos += x_vel
            x_vel -= (1 if x_vel > 0 else (-1 if x_vel < 0 else 0))
            y_pos += y_vel
            y_vel -= 1
            y_highest = max(y_highest, y_pos)
            if not target_hit:
                passed_target = (x_pos > x_bound[1]) or (y_pos < y_bound[0] and y_vel < 0)
                target_hit = (x_bound[0] <= x_pos <= x_bound[1]) and (y_bound[0] <= y_pos <= y_bound[1])
            else:
                if (y_pos < y_bound[0] and y_vel < 0) or (x_pos > x_bound[1] and y_vel < 0):
                    probe_dict[(x, y)] = y_highest
                    passed_target = True

print(f'Answer: {len(probe_dict)}')
