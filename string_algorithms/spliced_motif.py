
def parse_fasta(data):
    sequences = {}
    current_id = None
    current_seq = []

    for line in data.split('\n'):
        if line.startswith('>'):
            if current_id is not None:
                sequences[current_id] = ''.join(current_seq)
            current_id = line[1:]
            current_seq = []
        else:
            current_seq.append(line.strip())

    if current_id is not None:
        sequences[current_id] = ''.join(current_seq)

    things = []
    for thing in sequences:
        things.append(sequences[thing])

    return things[0], things[1]


def spliced_motif(s, t):
    pos = 0
    indices = []
    for letter in t:
        pos = s.find(letter, pos) + 1
        indices.append(pos)
    return indices


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()

    seq, substring = parse_fasta(data)
    indices = spliced_motif(seq, substring)
    return indices
    

indices = main('spliced_motif.txt')
print(' '.join(map(str, indices)))