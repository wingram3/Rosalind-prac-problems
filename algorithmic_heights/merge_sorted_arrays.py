
def parse_file(filename):
    with open(filename, 'r') as file:
        line1 = int(file.readline().strip())
        line2 = list(map(int, file.readline().strip().split()))
        line3 = int(file.readline().strip())
        line4 = list(map(int, file.readline().strip().split()))
    return line1, line2, line3, line4


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


n, A, m, B = parse_file('merge_sorted_arrays.txt')
merged_list = merge_lists(A, B)
print(' '.join(map(str, merged_list)))