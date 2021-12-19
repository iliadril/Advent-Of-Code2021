from collections import defaultdict

with open("./test_input", "r") as f:
    data = []
    for line in f:
        nums, out = line.split(' | ')
        data += [{'i': nums.split(), 'o': out.split()}]

# ---------------------------------- PART ONE ----------------------------------
print(f"Part One answer: {sum([1 for line in data for val in line['o'] if len(val) in (2, 3, 4, 7)])}")

# ---------------------------------- PART TWO ----------------------------------
display_dict = {0: ['a', 'b', 'c', 'e', 'f', 'g'],
                1: ['c', 'f'],
                2: ['a', 'c', 'd', 'e', 'g'],
                3: ['a', 'c', 'd', 'f', 'g'],
                4: ['b', 'c', 'd', 'f'],
                5: ['a', 'b', 'd', 'f', 'g'],
                6: ['a', 'b', 'd', 'e', 'f', 'g'],
                7: ['a', 'c', 'f'],
                8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                9: ['a', 'b', 'c', 'd', 'f', 'g']}


def decode_digit(l, d):
    for sequence in l:
        match_dict = {'a': [],
                      'b': [],
                      'c': [],
                      'd': [],
                      'e': [],
                      'f': [],
                      'g': []}

        # counting occurences
        occ_dict = defaultdict(int)
        for num in sequence['i']:
            for ch in num:
                occ_dict[ch] += 1

        match_dict['e'] = [ch for ch, val in occ_dict.items() if val == 4]
        match_dict['b'] = [ch for ch, val in occ_dict.items() if val == 6]
        match_dict['f'] = [ch for ch, val in occ_dict.items() if val == 9]

        # match which segments could be which
        for num in sequence['i']:
            for val in d.values():
                if len(num) == len(val) and len(num) in (2, 3, 4, 7):
                    if len(num) == 2:
                        print(list(num))
                        print(match_dict.values())
                    for ch in val:
                        if ch not in ('b', 'e', 'f'):
                            match_dict[ch] = [v for v in val if v not in (*match_dict['e'], *match_dict['b'], *match_dict['f'])]

        for num in sequence['i']:
            pass
        print(match_dict)


decode_digit(data, display_dict)
