from typing import Counter

with open('input') as file:
    c = Counter(len(j) for i in file.readlines() for j in i.split('|')[1].split())

answer = c[2] + c[4] + c[3] + c[7]

print(f'Answer: {answer}')