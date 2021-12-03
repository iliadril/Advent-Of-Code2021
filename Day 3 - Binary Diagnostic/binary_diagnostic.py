with open("./input", "r") as f:
    data = [list(n.strip()) for n in f]

# ---------------------------------- PART ONE ----------------------------------
gamma_rate, epsilon_rate = zip(*[(max(set(col), key=col.count), min(set(col), key=col.count)) for col in zip(*data)])
print("Part one solution:", int("".join(gamma_rate), 2)*int("".join(epsilon_rate), 2))

# ---------------------------------- PART TWO ----------------------------------
oxygen_generator, i = data, 0
while len(oxygen_generator) > 1:
    criterion = '0' if list(zip(*oxygen_generator))[i].count('0') > len(list(zip(*oxygen_generator))[i]) / 2 else '1'
    oxygen_generator = list(filter(lambda x: x[i] == criterion, oxygen_generator))
    i += 1

co2_scrubber, i = data, 0
while len(co2_scrubber) > 1:
    criterion = '1' if list(zip(*co2_scrubber))[i].count('0') > len(list(zip(*co2_scrubber))[i]) / 2 else '0'
    co2_scrubber = list(filter(lambda x: x[i] == criterion, co2_scrubber))
    i += 1

print("Part two solution:", int("".join(*oxygen_generator), 2)*int("".join(*co2_scrubber), 2))
