
def get_array(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == 2:
                return [int(num) for num in line.strip().split()]
    return []


def heapify(A, n, i):
    largest = i
    L = 2 * i
    R = 2 * i + 1

    if L <= n and A[L-1] > A[largest-1]:
        largest = L

    if R <= n and A[R-1] > A[largest-1]:
        largest = R

    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        heapify(A, n, largest)


def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, 0, -1):
        heapify(A, n, i)


A = get_array('rosalind_hea.txt')
build_max_heap(A)
with open('heap_answer.txt', 'w') as file:
    file.write(' '.join(map(str, A)))