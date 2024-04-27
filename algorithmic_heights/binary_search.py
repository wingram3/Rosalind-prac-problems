def parse_file(filename):
    A = []
    list = []

    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == 3:
                A = line.strip().split()
            elif i == 4:
                list = line.strip().split()
            elif i > 4:
                break

    return A, list


def binary_search(arr, target):
    left, right = 0, len(arr)-1
    result = -1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            result = middle + 1
            right = middle - 1
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return result
    

# return a list of the first index of the target num for each target num in list
def find_indices(A, list):
    indices = []
    A = [int(x) for x in A]
    list = [int(x) for x in list]
    A.sort()
    for num in list:
        indices.append(binary_search(A, num))
    return ' '.join(map(str, indices))



A, list = parse_file('binary_search.txt')
indices = find_indices(A, list)
with open('bs_asnwer.txt', 'w') as answer_file:
    answer_file.write(indices)                