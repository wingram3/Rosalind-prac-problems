import numpy as np

def random_strings(s, A):
    B = []
    for gc_cont in A:
        pAT = (1 - gc_cont) / 2
        pGC = gc_cont / 2

        prob = 0
        for letter in s:
            if letter == 'A' or letter == 'T':
                prob += np.log10(pAT)
            else:
                prob += np.log10(pGC)

        B.append(prob)

    return B


s = 'CCGCGTCGAGTTGCTGCATAGCTAGTGAGTGGTGATAGTATGTTTTGCAATTGGGTGGCCTATCTCCACCCAGAGCTTATAGGCCGCA' 
A = [0.079, 0.133, 0.207, 0.243, 0.278, 0.347, 0.407, 0.486, 0.543, 0.578, 0.666, 0.705, 0.752, 0.784, 0.884, 0.899]
print(random_strings(s, A))
