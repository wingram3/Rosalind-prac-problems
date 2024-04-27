
def get_dna_strings(data):
    dna_strings = []
    current_string = ''

    for line in data.split('\n'):
        if line.startswith('>'):
            if current_string:  
                dna_strings.append(list(current_string))
                current_string = ''  
        else:
            current_string += line  

    if current_string:  
        dna_strings.append(list(current_string))

    return dna_strings


def get_profile(dna_strings):
    nucs = {'A': [], 'C': [], 'G': [], 'T': []}

    for nuc in nucs:
        for col in range(len(dna_strings[0])):
            count = 0
            for row in range(len(dna_strings)):
                if dna_strings[row][col] == nuc:
                    count += 1
            nucs[nuc].append(count)

    return nucs


def get_consensus(nucs):
    consensus = ''
    for col in range(len(nucs['A'])):
        counts = [nucs[nuc][col] for nuc in 'ACGT']
        max_count = max(counts)
        most_common_nucs = [nuc for nuc, count in zip('ACGT', counts) if count == max_count]
        consensus += min(most_common_nucs)
    return consensus 
          

def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None 
    

def main(filename):
    with open(filename, 'r') as file:
        data = file.read()

    dna_strings = get_dna_strings(data)
    nucs = get_profile(dna_strings)
    consensus = get_consensus(nucs)

    print(consensus)

    for nuc in 'ACGT':
        print(nuc + ':', ' '.join(map(str, nucs[nuc])))


main('consensus.txt')