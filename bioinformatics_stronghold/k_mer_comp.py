from itertools import product

def parse_fasta(filename):
    with open(filename, 'r') as file:
        lines = []
        for i, line in enumerate(file):
            if i > 0:
                lines.append(line.strip())
        return ''.join(lines)


# get all possible 4-mers
def get_four_mers():
    alphabet = 'ACGT'
    return [''.join(mer) for mer in product(alphabet, repeat=4)]


# count occurrences of each 4-mer in the dna sequence
def count_four_mers(sequecne, k_mers):
    kmer_count = {kmer: 0 for kmer in k_mers}
    k = len(k_mers[0])
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i : i+k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
    return kmer_count



sequence = parse_fasta('k_mer_comp.txt')
kmers = get_four_mers()
kmer_count = count_four_mers(sequence, kmers)
kmer_vals = kmer_count.values()
print(' '.join(map(str, kmer_vals)))
