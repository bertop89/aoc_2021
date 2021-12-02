input = [int(x) for x in open('input.txt', 'r').read().splitlines()]


def compute_sum_diffs(input_list):
    diffs = [current > previous for previous, current in zip(input_list, input_list[1:])]
    return sum(diffs)


print(compute_sum_diffs(input))

three_sums = [a+b+c for a, b, c in zip(input, input[1:], input[2:])]
print(compute_sum_diffs(three_sums))
