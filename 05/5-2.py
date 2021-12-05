def parse_input(filename):
    clouds = []
    with open(filename) as file:
        for line in file:
            cloud = line.split('->')
            x1, y1 = cloud[0].strip().split(',')
            x2, y2 = cloud[1].strip().split(',')
            clouds.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return clouds

def get_range(p1, p2):
    direction = 1 if p2-p1 > 0 else -1
    return range(p1, p2 + direction, direction)

def count_overlap(clouds):
    cloud_counter = {}
    for cloud in clouds:
        x1, y1 = cloud[0]
        x2, y2 = cloud[1]
        r1 = r2 = None
        # Case 1: Horizontal
        if  y1 == y2:
            r1 = get_range(x1, x2) 
            r2 = [y1] * len(r1)
        # Case 2: Vertical 
        elif x1 == x2:
            r2 = get_range(y1, y2) 
            r1 = [x1] * len(r2)
        # Case 3: Diagonal
        else: 
            r1 = get_range(x1, x2)         
            r2 = get_range(y1, y2)
        # Create a list of tuples representing each position, count them in the dictionary
        for cloud_pos in zip(r1, r2):
            if cloud_pos in cloud_counter:
                cloud_counter[cloud_pos] += 1
            else:
                cloud_counter[cloud_pos] = 1
    return cloud_counter

clouds = parse_input('input')
cloud_counter = count_overlap(clouds)
# Check how many positions have two or more occurrences
solution = len([i for i in cloud_counter.values() if i >= 2])
print(f'Answer: {solution}')