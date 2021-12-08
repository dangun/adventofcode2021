from multiprocessing import Pool

def solve_line(line) -> int:

    word_dict = {}
    word_dict_rev = {}
    input, value = line.split('|')
    word_sets = sorted((frozenset(word) for word in input.split()), key = len)
    
    def add_word(word, number):
        word_dict[number] = word
        word_dict_rev[word] = number

    add_word(word_sets[0], 1)
    add_word(word_sets[1], 7)
    add_word(word_sets[2], 4)
    add_word(word_sets[9], 8)

    for word in word_sets[3:6]:
        if len(word) == 5 and word > word_dict[1]:
            word_dict_rev[word] = 3
        elif len(word) == 5 and len(word - word_dict[4]) == 3:
            word_dict_rev[word] = 2
        else:
            word_dict_rev[word] = 5

    for word in word_sets[6:9]:
        if len(word) == 6 and word > word_dict[4]:
            word_dict_rev[word] = 9
        elif len(word) == 6 and len(word - word_dict[1]) == 5:
            word_dict_rev[word] = 6
        else:
            word_dict_rev[word] = 0

    result = ''
    for word in value.split():
        result += str(word_dict_rev[frozenset(word)])

    return int(result)

if __name__ == '__main__':
    
    with open('input') as file:
        input = file.readlines()

    pool = Pool()
    results = pool.map(solve_line, input)

    print(f'Answer: {sum(results)}')
