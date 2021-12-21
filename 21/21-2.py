from itertools import product
from collections import Counter

with open('input') as file:
    p1_pos = int(file.readline().split(': ')[1])
    p2_pos = int(file.readline().split(': ')[1])

die_results = Counter([sum(tup) for tup in product(range(1,4), repeat=3)])

def roll(p1, p2):
    if p2[1] >= 21:
        return 0, 1
    p1_wins = p2_wins = 0
    for die_result, occ in die_results.items():
        new_pos = (p1[0] + die_result - 1) % 10 + 1
        p2_temp_win, p1_temp_win = roll(p2,(new_pos,p1[1]+new_pos))
        p1_wins += occ * p1_temp_win
        p2_wins += occ * p2_temp_win
    return p1_wins, p2_wins

wins = roll((p1_pos,0),(p2_pos,0))

print(f'Answers: {max(wins)}')