
from scipy.special import comb

def mendel_first(k, m, n):
    total_pop = k + m + n
    total_combos = comb(total_pop, 2)
    valid_combos = comb(k, 2) + k*m + k*n + 0.5*m*n + 0.75*comb(m, 2)
    prob = valid_combos / total_combos
    return prob

print(mendel_first(24, 26, 24))


