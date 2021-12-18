from statistics import median, mean
from math import ceil

with open("./input", "r") as f:
    data = [int(n) for n in f.readline().split(",")]


# ---------------------------------- PART ONE ----------------------------------
print(f"Part One answer: {sum([abs(n - int(median(data))) for n in data])}")

# ---------------------------------- PART TWO ----------------------------------
# mean(data) value is very close to equilibrium position of crabs, so we scan ±3 from mean value and get the minimum
print(f"Part Two answer: {min([sum(abs(n-i)*(abs(n-i) + 1)//2 for n in data) for i in range(int(mean(data))-3, int(mean(data))+3)])}")
