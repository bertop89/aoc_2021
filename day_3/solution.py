input = open('input.txt', 'r').read().splitlines()

print(input)

total = list()
current = list()
for pos in range(len(input[0])):
    for number in input:
        current.append(number[pos])
    total.append(max(current, key=current.count))
    current = list()

gamma_rate = int(''.join(total), 2)
epsilon_rate = int(''.join(['0' if x == '1' else '1' for x in total]), 2)

print(gamma_rate*epsilon_rate)



from collections import Counter
import re


def filter_numbers(input, mask, pos, is_max=True):
    current = list()
    for number in input:
        current.append(number[pos])
    common = Counter(current).most_common(2)
    if len(common) == 1:
        return input, mask+common[0][0]
    if common[0][1] == common[1][1]:
        mask += '1' if is_max else '0'
    else:
        mask += common[0][0] if is_max else common[1][0]
    return [x for x in input if x.startswith(mask)], mask


oxygen_mask = scrubber_mask = ''
oxygen = [x for x in input]
scrubber = [x for x in input]
for pos in range(len(input[0])):
    if len(oxygen) > 1:
        oxygen, oxygen_mask = filter_numbers(oxygen, oxygen_mask, pos, is_max=True)
    if len(scrubber) > 1:
        scrubber, scrubber_mask = filter_numbers(scrubber, scrubber_mask, pos, is_max=False)

print(int(oxygen[0], 2) * int(scrubber[0], 2))
