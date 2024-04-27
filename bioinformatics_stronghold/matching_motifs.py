import math

def matching_motifs(N, x, s):
    # Calculate P(s) where s is the given motif
    p_s = 1.0
    for nucleotide in s:
        if nucleotide in "GC":
            p_s *= x  # Probability that this nucleotide is G or C
        elif nucleotide in "AT":
            p_s *= (1 - x)  # Probability that this nucleotide is A or T

    # Using logarithms to avoid underflow
    # Calculate the log probability that none of N strings matches the motif s
    if p_s == 1:  # Edge case where every nucleotide probability is exactly as expected
        probability_none_match = 0
    else:
        log_prob_none_match = N * math.log(1 - p_s)
        probability_none_match = math.exp(log_prob_none_match)

    # Calculate the probability that at least one matches
    probability_at_least_one_matches = 1 - probability_none_match

    return probability_at_least_one_matches


prob = matching_motifs(N=90000, x=0.6, s='ATAGCCGA')
print(prob)


