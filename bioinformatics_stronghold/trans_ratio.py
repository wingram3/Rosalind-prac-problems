
def parse_fasta(data):
    sequences = {}
    current_seq = []
    current_id = None
    
    for line in data.split('\n'):
        if line.startswith('>'):
            if current_id is not None:
                sequences[current_id] = ''.join(current_seq)
            current_seq = []
            current_id = line[1:]
        else:
            current_seq.append(line.strip())

    if current_id is not None:
        sequences[current_id] = ''.join(current_seq)

    return list(sequences.values())[0], list(sequences.values())[1] 


def trans_ratio(s1, s2):
    transitions = 0
    transversions = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == 'A' and s2[i] == 'G' or s1[i] == 'G' and s2[i] == 'A':
                transitions += 1
            elif s1[i] == 'C' and s2[i] == 'T' or s1[i] == 'T' and s2[i] == 'C':
                transitions += 1
            else:
                transversions += 1
    
    return transitions / transversions


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()
    s1, s2 = parse_fasta(data)
    ratio = trans_ratio(s1, s2)
    return ratio


print(main('trans_ratio.txt'))