from collections import Counter

def parse_file(filename):
    arrays = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i >= 1:
                char_list = line.strip().split()
                arrays.append([int(char) for char in char_list])
    return arrays


def find_majority(arrays):
    majority_element_list = []
    for array in arrays:
        freq = Counter(array)
        if max(freq.values()) > (len(array) / 2):
            majority_element_list.append(max(freq, key=freq.get))
        else:
            majority_element_list.append(-1)
    return majority_element_list



arrays = parse_file('rosalind_maj.txt')
majority_element_list = find_majority(arrays)
print(' '.join(map(str, majority_element_list)))