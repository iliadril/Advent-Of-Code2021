import numpy as np


with open("./input", "r") as f:
    data = np.array([[int(num) for num in line.strip()] for line in f])
    data = np.pad(data, pad_width=1, mode='constant', constant_values=9)


# ---------------------------------- PART ONE ----------------------------------
risk_level = 0
for line in range(1, len(data) - 1):
    for num in range(1, len(data[line]) - 1):
        if data[line][num] < min(data[line-1][num], data[line+1][num], data[line][num-1], data[line][num+1]):
            risk_level += data[line][num]+1
print(f"Part One answer: {risk_level}")

# ---------------------------------- PART TWO ----------------------------------
