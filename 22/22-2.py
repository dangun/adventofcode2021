from collections import defaultdict

onoff = []
with open('input') as file:
    for line in file:
        op, coords = line.split(' ')
        xyz = tuple(tuple(map(int, coord[2:].split('..'))) for coord in coords.split(','))
        onoff.append((xyz, 1 if op == 'on' else -1))

# Returns the intersection of two cuboids, may not be valid coordinates if there is no intersection
inters_cuboid = lambda xyz1, xyz2: tuple(((max(xyz1[i][0], xyz2[i][0]), min(xyz1[i][1], xyz2[i][1])) for i in range(3)))
# Checks if the coordinates are valid to describe a cuboid
valid_cuboid = lambda xyz: xyz[0][0] <= xyz[0][1] and xyz[1][0] <= xyz[1][1] and xyz[2][0] <= xyz[2][1]

# Dict to keep track of all cuboids in the space, counting -+ for negative and positive space
space_dict = defaultdict(int)

for cuboid, op in onoff:
    collision_dict = defaultdict(int)
    # If 'On', then add the positive space
    if op == 1:
        collision_dict[cuboid] += 1
    # Check for every intersection and add a cuboid that is the reverse of the intersected cuboid
    # E.g. Positive ∩ positive = negative, positive ∩ negative = positive
    #      Negative ∩ positive = negative, negative ∩ negative = positive
    # This is to cancel out overlaps so that we don't double count space
    for k, v in space_dict.items():
        new_cuboid = inters_cuboid(k, cuboid)
        if valid_cuboid(new_cuboid):
            collision_dict[new_cuboid] -= v
    # Add all collisions to the space to participate in the next comparison
    for k, v in collision_dict.items():
        space_dict[k] += v

volume = 0
for k, v in space_dict.items():
    volume += (1 + k[0][1] - k[0][0]) * (1 + k[1][1] - k[1][0]) * (1 + k[2][1] - k[2][0]) * v

print(f'Answer: {volume}')
