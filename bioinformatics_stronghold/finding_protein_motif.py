
def parse_fasta(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return ''.join(data.strip().split('\n')[1:])


def reverse_complement(dna_string):
    complements = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    reverse_comp = []
    for nucleotide in dna_string:
        reverse_comp.append(complements[nucleotide])
    return ''.join(map(str, list(reversed(reverse_comp))))


def find_reverse_palindromes(dna_string):
    results = []
    for i in range(len(dna_string)):
        for j in range(4, 13):
            substring = dna_string[i : i+j]
            if len(substring) < 4:
                continue
            if len(substring) <= 12:
                if substring == reverse_complement(substring):
                    results.append((i+1, len(substring)))

    return results
    


dna_string = parse_fasta('finding_protein_motif.txt')
results = find_reverse_palindromes(dna_string)
for tup in set(results):
    print(tup[0], tup[1])