from collections import deque

def parse_file(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == 2:
                return [[int(num)] for num in line.strip().split()]


def merge_lists(A, B):
    merged_list = []
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged_list.append(A[i])
            i += 1
        else:
            merged_list.append(B[j])
            j += 1

    merged_list.extend(A[i:])
    merged_list.extend(B[j:])

    return merged_list


def merge_sort(arr):
    arr = deque(arr)
    while arr:
        list1 = arr.popleft()
        list2 = arr.popleft()
        merged = merge_lists(list1, list2)
        
        if len(arr) > 0:
            arr.append(merged)
        else:
            return merged



array = parse_file('rosalind_ms.txt')
sorted = merge_sort(array)
with open('merge_sort_ans.txt', 'w') as file:
    file.write(' '.join(map(str, sorted)))