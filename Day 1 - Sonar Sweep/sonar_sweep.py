with open("input", "r") as f:
    data = [int(n) for n in f]

print(sum(x < y for x, y in zip(data, data[1:])))
# we can skip counting sums in-between as those numbers are in both "windows" [A=(199, 200, 208), B=(200, 208, 210)]
#                                                                                       ^    ^        ^    ^
print(sum(x < y for x, y in zip(data, data[3:])))
