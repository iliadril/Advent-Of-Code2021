with open("./input", "r") as f:
    data = [line.split(" ") for line in f]
    data = [(comm, int(n)) for comm, n in data]

# ---------------------------------- PART ONE ----------------------------------
horizontal = sum(x[1] for x in data if x[0] == 'forward')
vertical = sum(x[1] for x in data if x[0] == 'down')
vertical -= sum(x[1] for x in data if x[0] == 'up')

print(f'Horizontal distance: {horizontal}\nVertical distance: {vertical}\nProduct: {horizontal*vertical}\n')

# ---------------------------------- PART TWO ----------------------------------
horizontal, depth, aim = 0, 0, 0
for comm, n in data:
    match comm:
        case 'down':
            aim += n
        case 'up':
            aim -= n
        case 'forward':
            horizontal += n
            depth += n*aim

print(f'Horizontal distance: {horizontal}\nVertical distance: {depth}\nProduct: {horizontal*depth}')
