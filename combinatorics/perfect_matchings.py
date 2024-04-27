def parse_fasta(data):
    return ''.join(data.strip().split('\n')[1:])


def recurrence(n):
    if n == 1:
        return 1
    else:
        return (n - 1) * recurrence(n - 1)
    

def perfect_matchings(rna_string):
    AUs = rna_string.count('A')
    GCs = rna_string.count('G')
    return recurrence(AUs) * recurrence(GCs)


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()

    sequence = parse_fasta(data)
    matchings = perfect_matchings(sequence)
    return matchings


print(main('perfect_matchings.txt'))

