def partial_permutations(n, k, mod=1000000):
    result = 1
    for i in range(n, n-k, -1):
        result = (result * i) % mod
    return result

print(partial_permutations(94, 8))