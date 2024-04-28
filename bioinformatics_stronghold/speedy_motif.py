
def parse_fasta(filename):
    with open(filename, 'r') as file:
        lines = []
        for i, line in enumerate(file):
            if i > 0:
                lines.append(line.strip())
    return ''.join(lines)


def find_failure_array(pattern):
    pi = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while (j > 0 and pattern[i] != pattern[j]):
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi


sequence = parse_fasta('speedy_motif.txt')
pi = find_failure_array(sequence)
with open('speedy_motif_out.txt', 'w') as file:
    file.write(' '.join(map(str, pi)))
