
def parse_file(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == 2:
                return [int(num) for num in line.strip().split()]
            

def heapify(A, n, i):
    largest = i
    L = 2 * i + 1
    R = 2 * i + 2

    if L < n and A[L] > A[largest]:
        largest = L

    if R < n and A[R] > A[largest]:
        largest = R

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)


def build_max_heap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)


def heap_sort(array):
    build_max_heap(array)
    n = len(array)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)



array = parse_file('rosalind_hs.txt')
heap_sort(array)
with open('heap_sort_ans.txt', 'w') as file:
    file.write(' '.join(map(str, array)))