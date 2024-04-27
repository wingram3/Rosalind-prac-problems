
def parse_file(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i >= 1:
                char_list = line.strip().split()
    return [int(char) for char in char_list]


def partition(array, low, high):
    pivot = array[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i] 
            i += 1

    array[low], array[i-1] = array[i-1], array[low]
    return ' '.join(map(str, array))




array = parse_file('rosalind_par.txt')
array2 = partition(array, 0, len(array)-1)
with open('partition_answer.txt', 'w') as answer_file:
    answer_file.write(array2)
