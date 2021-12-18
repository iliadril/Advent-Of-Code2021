with open("./input", "r") as f:
    lines = []
    for line in f.readlines():
        p1, p2 = line.strip().split(" -> ")
        (x1, y1), (x2, y2) = p1.split(","), p2.split(",")
        lines += [{'x1': int(x1), 'y1': int(y1), 'x2': int(x2), 'y2': int(y2)}]

x_max, y_max = 0, 0
for line in lines:
    x_max = max(x_max, max(line['x1'], line['x2']))
    y_max = max(y_max, max(line['y1'], line['y2']))

board1 = [[0 for _ in range(x_max+1)] for _ in range(y_max+1)]
board2 = [[0 for _ in range(x_max+1)] for _ in range(y_max+1)]


# ---------------------------------- PART ONE ----------------------------------
def paint_lines(board, lines, ignore_diagonal=True):
    for line in lines:
        if line['x1'] == line['x2'] or line['y1'] == line['y2']:
            for y in range(min(line['y1'], line['y2']), max(line['y1'], line['y2'])+1):
                for x in range(min(line['x1'], line['x2']), max(line['x1'], line['x2'])+1):
                    board[y][x] += 1
        elif not ignore_diagonal and abs(line['x1'] - line['x2']) == abs(line['y1'] - line['y2']):
            dx = 1 if line['x1'] < line['x2'] else -1
            dy = 1 if line['y1'] < line['y2'] else -1
            for p in range(abs(line['x1'] - line['x2']) + 1):
                board[line['y1'] + p * dy][line['x1'] + p * dx] += 1


def count_overlapping(board):
    return len([e for l in board for e in l if int(e) >= 2])


paint_lines(board1, lines)
print(f"Answer to part one: {count_overlapping(board1)}")

# ---------------------------------- PART ONE ----------------------------------
paint_lines(board2, lines, False)
print(f"Answer to part one: {count_overlapping(board2)}")
