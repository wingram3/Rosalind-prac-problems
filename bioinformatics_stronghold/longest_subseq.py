
def longest_inc_subseq(n, pi):
    LIS = [1] * n
    list = []

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if pi[i] < pi[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

                list.append(pi[j])

    return list


n = 5
pi = [5, 1, 4, 2, 3]
print(longest_inc_subseq(n, pi))