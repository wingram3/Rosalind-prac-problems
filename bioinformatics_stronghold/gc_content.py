
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

    return sequences


def calculate_gc(dna):
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100


def find_highest_gc(sequences):
    max_gc_content = 0
    max_gc_id = None

    for seq_id, seq in sequences.items():
        gc_content = calculate_gc(seq)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = seq_id

    return max_gc_id, max_gc_content


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()

    sequences = parse_fasta(data)
    max_gc_id, max_gc_content = find_highest_gc(sequences)
    return max_gc_id, max_gc_content


# run it with the file
print(main('gc_content.txt'))
