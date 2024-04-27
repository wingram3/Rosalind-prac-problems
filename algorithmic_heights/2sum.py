
def parse_file(filename):
    arrays = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i >= 1:
                char_list = line.strip().split()
                arrays.append([int(char) for char in char_list])
    return arrays


def two_sum(arrays):
    two_sum_array = []
    for array in arrays:
        pair_found = False
        num_map = {}
        for i, num in enumerate(array):
            complement = 0 - num
            if complement in num_map:
                two_sum_array.append([num_map[complement]+1, i+1])
                pair_found = True
                break
            num_map[num] = i
        if not pair_found:
            two_sum_array.append([-1])
    return two_sum_array



arrays = parse_file('rosalind_2sum.txt')
two_sum_array = two_sum(arrays)
for sum in two_sum_array:
    print(' '.join(map(str, sum))) 