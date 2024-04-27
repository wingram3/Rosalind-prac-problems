
def parse_file(input_file):
    with open(input_file, 'r') as file:
        arrays = []
        for i, line in enumerate(file):
            if i > 0:
                arrays.append([int(num) for num in line.split()])
    return arrays


def three_sum_indices(array):
    n = len(array)
    array_sorted = sorted((val, idx + 1) for idx, val in enumerate(array))  # Pair values with 1-based indices
    
    for i in range(n - 2):
        if i > 0 and array_sorted[i][0] == array_sorted[i - 1][0]:  # Skip duplicate values
            continue
        left, right = i + 1, n - 1
        while left < right:
            current_sum = array_sorted[i][0] + array_sorted[left][0] + array_sorted[right][0]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                # Ensure indices are distinct and in increasing order
                if array_sorted[i][1] < array_sorted[left][1] < array_sorted[right][1]:
                    return [array_sorted[i][1], array_sorted[left][1], array_sorted[right][1]]
                # Adjust pointers to continue search
                left += 1
                right -= 1

    return -1


arrays = parse_file('3sum.txt')
results = [three_sum_indices(arr) for arr in arrays]
for result in results:
    if isinstance(result, list):
        print(' '.join(map(str, result)))
    else:
        print(result)

