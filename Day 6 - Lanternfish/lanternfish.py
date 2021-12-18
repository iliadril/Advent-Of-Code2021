from collections import defaultdict


with open("./input", "r") as f:
    data = [int(n) for n in f.readline().split(",")]
    fish_dict = defaultdict(int)
    for fish in data:
        fish_dict[fish] += 1


# ---------------------------------- PART ONE & TWO ----------------------------------
def next_day(lanternfish):
    for i in range(9):
        if i == 0:
            store_n = lanternfish[i]
            lanternfish[i] = 0
        else:
            lanternfish[i-1] += lanternfish[i]
            lanternfish[i] = 0
    lanternfish[6] += store_n
    lanternfish[8] += store_n


for day in range(256):  # change range to change simulation time
    next_day(fish_dict)
    print(f"After:{day+1:3}\tSum: {sum(fish_dict.values())}")
