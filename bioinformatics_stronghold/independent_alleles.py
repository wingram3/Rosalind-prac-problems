from scipy.stats import binom

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        

def binomial_probability(k, N):
    p = 0.25
    total_offspring = 2**k
    probability = 0

    for i in range(N, total_offspring + 1):
        probability += binom.pmf(i, total_offspring, p)
    return probability


k = 5
N = 9
result = binomial_probability(k, N)
print(result) 