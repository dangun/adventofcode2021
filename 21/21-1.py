with open('input') as file:
    p1_pos = int(file.readline().split(': ')[1])
    p2_pos = int(file.readline().split(': ')[1])

class player:
    def __init__(self, position):
        self.pos = position
        self.score = 0

p1 = player(p1_pos)
p2 = player(p2_pos)
die = list(range(1,100+1))
counter = 0
curr = p1

while True:
    for _ in range(3):
        curr.pos += die[counter%100]
        counter += 1
    curr.pos = (curr.pos - 1) % 10 +1
    curr.score += curr.pos
    if curr.score >= 1000:
        break
    curr = p2 if curr is p1 else p1

print(f'Answer: {min(p1.score, p2.score) * counter}')