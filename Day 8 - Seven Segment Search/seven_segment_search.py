with open("./input", "r") as f:
    data = []
    for line in f:
        nums, out = line.split(' | ')
        data += [(nums.split(), out.split())]

# ---------------------------------- PART ONE ----------------------------------
print(f"Part One answer: {sum([1 for line in data for val in line[1] if len(val) in (2, 3, 4, 7)])}")

# ---------------------------------- PART TWO ----------------------------------
out_sum = 0
for inp, outp in data:
    num_match = [set()] * 10
    num_match[1] = list(set(val) for val in inp if len(val) == 2)[0]
    num_match[4] = list(set(val) for val in inp if len(val) == 4)[0]
    num_match[7] = list(set(val) for val in inp if len(val) == 3)[0]
    num_match[8] = list(set(val) for val in inp if len(val) == 7)[0]

    fiveters = (set(val) for val in inp if len(val) == 5)
    for num in fiveters:
        if num_match[1].issubset(num):
            num_match[3] = num
        elif len(num & num_match[4]) == 3:
            num_match[5] = num
        else:
            num_match[2] = num

    sixters = (set(val) for val in inp if len(val) == 6)
    for num in sixters:
        if num_match[4].issubset(num):
            num_match[9] = num
        elif num_match[5].issubset(num):
            num_match[6] = num
        else:
            num_match[0] = num

    s = 0
    for o in outp:
        s = s * 10 + num_match.index(set(o))
    out_sum += s

print(f"Part Two answer: {out_sum}")
