from copy import deepcopy


with open("./input", "r") as f:
    data = f.read().splitlines()
    nums = data[0].split(',')
    boards = [[x.split() for x in data[board:board+5]] for board in range(2, len(data), 6)]


# ---------------------------------- PART ONE ----------------------------------
def mark_boards(d, drawn):
    for board in d:
        for line in board:
            for i, num in enumerate(line):
                if drawn == num:
                    line[i] = False


def check_boards(d):
    for board in d:
        for line in board:
            if all(x is False for x in line):
                return board
        for line in zip(*board):
            if all(x is False for x in line):
                return board


def sum_board(b, final_num):
    if b:
        return sum(int(n) for line in b for n in line) * int(final_num)


def part_one(nums, boards):
    for num in nums:
        mark_boards(boards, num)
        board = check_boards(boards)
        if board:
            print(f"Part One final score: {sum_board(board, num)}")
            break


nums1, boards1 = deepcopy(nums), deepcopy(boards)
part_one(nums1, boards1)
# ---------------------------------- PART TWO ----------------------------------


def check_boards2(d):
    for i, board in enumerate(d):
        if 'X' in board:
            return
        for line in board:
            if all(x is False for x in line):
                board_cpy = deepcopy(board)
                d[i].extend('X')
                return board_cpy
        for line in zip(*board):
            if all(x is False for x in line):
                board_cpy = deepcopy(board)
                d[i].extend('X')
                return board_cpy


def part_two(nums, boards):
    scores = []
    for num in nums:
        mark_boards(boards, num)
        board = check_boards2(boards)
        if board:
            print(board, num)
            if 'X' not in board:
                score = sum_board(board, num)
                if score:
                    scores += [score]
    print(f"Part Two final score: {scores}")


nums2, boards2 = deepcopy(nums), deepcopy(boards)
part_two(nums2, boards2)
