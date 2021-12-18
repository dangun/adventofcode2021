import re
from math import ceil
from itertools import permutations

def parse_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

def combine(strings):
    return '[' + strings[0] + ',' + strings[1] + ']'

def explode_nr(string):
    regex_pair = r"\[\d+,\d+\]"
    regex_nr = r"\d+"
    for match in re.finditer(regex_pair, string):
        substring = string[:match.start()]
        if substring.count('[') - substring.count(']') >= 4:
            addleft, addright = map(int, match.group()[1:-1].split(','))
            # Add to the first value to the right
            substring = string[match.end()+1:]
            if add := re.search(regex_nr, substring):
                string = string[:add.start()+match.end()+1] + str(int(add.group())+addright) + string[add.end()+match.end()+1:]
            # Replace pair with 0
            string = string[:match.start()] + '0' + string[match.end():]
            # Add to the first value to the left
            substring = string[:match.start()]
            if add := list(re.finditer(regex_nr, substring)):
                add = add[-1]
                string = string[:add.start()] + str(int(add.group())+addleft) + string[add.end():]
            return string
    return None

def split_nr(string):
    regex_large_nr = r"\d{2,}"
    if match := re.search(regex_large_nr, string):
        repl_string = '[' + str(int(match.group())//2) + ',' + str(ceil(int(match.group())/2)) + ']'
        return string[:match.start()] + repl_string + string[match.end():]
    return None

def addition(string1, string2):
    string = combine([string1, string2])
    new_string = ''
    while new_string is not None:
        new_string = None
        while new_string := explode_nr(string):
            string = new_string
        if new_string := split_nr(string):
            string = new_string
    return string

def score(string):
    matches = True
    while matches:
        matches = list(re.finditer(r"\[\d+,\d+\]", string))
        for match in reversed(matches):
            left, right = map(int, match.group()[1:-1].split(','))
            result = int(left) * 3 + int(right) * 2
            string = string[:match.start()] + str(result) + string[match.end():]
    return string

if __name__ == "__main__":
    numbers = parse_input('input')
    score_dict = {}
    for x, y in permutations(range(len(numbers)),2):
        score_dict[(x, y)] = int(score(addition(numbers[x], numbers[y])))

    print(f'Answer: {max(score_dict.values())}')