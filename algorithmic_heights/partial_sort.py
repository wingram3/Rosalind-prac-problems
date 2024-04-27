
def get_array(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == 2:
                array = [int(num) for num in line.strip().split()]
            if i == 3:
                k = [int(num) for num in line.strip().split()]
    return array, k[0]


def partial_sort(array, k):
    array.sort()
    return ' '.join(map(str, array[:k]))


array, k = get_array('rosalind_ps.txt')  
sorted = partial_sort(array, k)
with open('partial_sort_ans.txt', 'w') as file:
    file.write(sorted)