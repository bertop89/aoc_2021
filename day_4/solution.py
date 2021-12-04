import numpy as np

boards = list()
with open("input.txt") as f:
    numbers = [int(x) for x in f.readline().split(',')]
    current_board = list()
    line = f.readline()
    while line:
        line = f.readline()
        if line == '\n' or line == '':
            boards.append(np.array(current_board))
            current_board = list()
        else:
            current_board.append([int(x) for x in line.split()])

def bingo(boards, numbers):
    current_numbers = list()
    mask = [-1] * boards[0].shape[0]
    for number in numbers:
        current_numbers.append(number)

        for idx, board in enumerate(boards):
            temp_board = board.copy()
            for current_number in current_numbers:
                temp_board = np.where(temp_board == current_number, -1, temp_board)
            if (temp_board == mask).all(axis=1).any() or (temp_board == mask).all(axis=0).any():
                return number, idx, temp_board

number, idx, board = bingo(boards, numbers)
print(number * np.sum(board[board != -1]))

while len(boards) > 0:
    number, idx, board = bingo(boards, numbers)
    print(number * np.sum(board[board != -1]))
    boards.pop(idx)


