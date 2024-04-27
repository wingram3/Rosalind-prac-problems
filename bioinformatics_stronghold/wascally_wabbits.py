
def rabbit_pairs(n, k):
    pairs = [0] * (n + 1)
    pairs[0] = 1

    for month in range(1, n):
        if month == 1:
            pairs[month] = 1
        else:
            pairs[month] = pairs[month - 1] + k*pairs[month - 2]

    return pairs[n-1]

print(rabbit_pairs(31, 3))