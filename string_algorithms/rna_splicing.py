
def parse_fasta(data):
    strings = {}
    current_id = None
    current_string = []

    # for each line in the file
    for line in data.split('\n'):
        if line.startswith('>'):

            # if we have already processed a string(s)
            if current_id is not None:

                # join the strings corresponding to the current id into one string and save it in the strings dict under the current id
                strings[current_id] = ''.join(current_string)

            # set the new current id and reset the current string to an empty list
            current_id = line[1:]
            current_string = []

        # we are in the middle of a sequence - add each line to the current_string list
        else:
            current_string.append(line.strip())

    # for the last sequence in the file
    if current_id is not None:
        strings[current_id] = ''.join(current_string)

    # return the dna sequence and the list of introns separately
    dna_sequence = list(strings.values())[0]
    introns = list(strings.values())[1:]

    return dna_sequence, introns


def translate_into_rna(dna, introns):
    # remove the introns from the dna sequence
    for intron in introns:
        dna = dna.replace(intron, '')

    # replace every T with a U
    dna = dna.replace('T', 'U')

    return dna


def translate(rna):
    rna_codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    # sliding window pointers
    left = 0
    right = left + 3

    # translate the rna into protein one codon at a time
    protein = []
    while right < len(rna):
        protein.append(rna_codon_table[rna[left : right]])
        left += 3
        right += 3

    # return the protein string
    return ''.join(protein)


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()

    dna, introns = parse_fasta(data)
    rna = translate_into_rna(dna, introns)
    protein = translate(rna)

    return protein


protein = main('rna_splicing.txt')
print(protein)