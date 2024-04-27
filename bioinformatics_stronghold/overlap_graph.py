
def get_dna_strings(data):
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


def build_edges(sequences):
    edge_pairs = []

    for id1, seq1 in sequences.items():
        for id2, seq2 in sequences.items():
            if id1 != id2 and seq1[-3:] == seq2[:3]:
                edge_pairs.append((id1, id2))

    return edge_pairs


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()
        
    sequences = get_dna_strings(data)
    edge_pairs = build_edges(sequences)

    for pair in edge_pairs:
        print(pair[0], pair[1])


main('overlap_graph.txt')