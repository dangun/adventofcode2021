import numpy as np

BOARD_COL = 5
BOARD_ROW = 5

def parse_input(filename):
    bingo_boards = []
    bingo_numbers = None
    with open(filename) as file:
        bingo_numbers = [int(i) for i in file.readline().split(',')]
        arr_gen = (arr for arr in file.read().split('\n\n'))
        # Read each board by itself, reshape it and append a transposed copy at the end
        # The result is a list where each element is a list representing a single row or column
        for arr in np.loadtxt(arr_gen, dtype = int):
            board_arr = arr.reshape(BOARD_ROW, BOARD_COL)
            board_arr = np.append(board_arr, board_arr.transpose(), axis = 0)
            bingo_boards.append(board_arr.tolist())
    return bingo_numbers, bingo_boards

def find_loser(bingo_numbers, bingo_boards):
    for i in range(len(bingo_numbers)-1, min(BOARD_ROW, BOARD_COL)-1, -1):
        test_set = set(bingo_numbers[:i])
        for bingo_board in bingo_boards:
            win = False
            for line in bingo_board:
                if test_set.issuperset(line):
                    win = True
            if not win:
                return bingo_numbers[:i+1], bingo_board
    return None

bingo_numbers, bingo_boards = parse_input('input')
winning_numbers, winning_board = find_loser(bingo_numbers, bingo_boards)

solution = 0
winner_board_numbers = [nr for row in winning_board[:BOARD_ROW] for nr in row]
solution += sum(set(winner_board_numbers).difference(winning_numbers))
solution *= winning_numbers[-1]

print(f'Answer: {solution}')