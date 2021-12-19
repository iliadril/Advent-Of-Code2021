from statistics import median


with open("./input", "r") as f:
    data = [[num for num in line.strip()] for line in f]


# ---------------------------------- PART ONE ----------------------------------
mirror_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}

corr_points_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
corr_points = 0
for line in data:
    braces_stack = []
    for ch in line:
        if ch in mirror_dict.keys():
            braces_stack += [ch]
        elif ch in mirror_dict.values():
            if ch == mirror_dict[braces_stack[-1]]:
                braces_stack = braces_stack[:-1]
            else:
                corr_points += corr_points_dict[ch]
                break

print(f"Part One answer: {corr_points}")
# ---------------------------------- PART TWO ----------------------------------
incp_points_dict = {')': 1, ']': 2, '}': 3, '>': 4}
incp_points = []
for line in data:
    braces_stack = []
    for ch in line:
        if ch in mirror_dict.keys():
            braces_stack += [ch]
        elif ch in mirror_dict.values():
            if ch == mirror_dict[braces_stack[-1]]:
                braces_stack = braces_stack[:-1]
            else:  # discard corrupted lines
                braces_stack = []
                break
    if braces_stack:
        missing_lines = [mirror_dict[ch] for ch in braces_stack[::-1]]
        score = 0
        for ch in missing_lines:
            score *= 5
            score += incp_points_dict[ch]
        incp_points += [score]

print(f"Part Two answer: {median(incp_points)}")
