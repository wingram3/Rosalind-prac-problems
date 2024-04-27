
def mortal_rabbits(n, m):
    pairs = [0, 1, 1]

    for i in range(3, n+1):
        if i <= m:
            total = pairs[i-1] + pairs[i-2]
        elif i == m + 1:
            total = pairs[i-1] + pairs[i-2] - 1
        else:
            total = pairs[i-1] + pairs[i-2] - pairs[i - m-1]

        pairs.append(total)

    return pairs[n]


print(mortal_rabbits(83, 17))