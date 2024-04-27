
def get_array(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == 2:
                return [int(num) for num in line.strip().split()]
    return []


def insertion_sort(arr):
    swaps = 0
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
    return swaps


A = get_array('insertion_sort.txt')
print(insertion_sort(A))
