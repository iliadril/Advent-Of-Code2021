with open("./input", "r") as f:
    data = [line.split(" ") for line in f]
    data = [(comm, int(n)) for comm, n in data]

horizontal = sum(x[1] for x in data if x[0] == 'forward')
vertical = sum(x[1] for x in data if x[0] == 'down')
vertical -= sum(x[1] for x in data if x[0] == 'up')

print(f'Horizontal distance: {horizontal}\nVertical distance: {vertical}\nProduct: {horizontal*vertical}')
