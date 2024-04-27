
def parse_fasta(data):
    complements = {"A": "T", "G": "C", "C": "G", "T": "A"}
    sequence = ''.join(data.strip().split('\n')[1:])
    reverse_comp = ''.join(complements[nuc] for nuc in reversed(sequence))
    return sequence, reverse_comp


def translate_codons(codon):
    codon_dict = {
    "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
    "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
    "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
    "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
    "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
    "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
    "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "TAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "TAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
    "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "TGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
    return codon_dict.get(codon, '')


def find_orfs(dna):
    def extract_proteins(seq):
        proteins = set()
        for i in range(len(seq) - 2):
            if seq[i : i+3] == 'ATG':
                protein = ''
                for j in range(i, len(seq) - 2, 3):
                    amino_acid = translate_codons(seq[j : j+3])
                    if amino_acid == 'Stop':
                        proteins.add(protein)
                        break
                    protein += amino_acid
        return proteins
    
    strand, reverse_comp = parse_fasta(dna)

    proteins = set()
    for i in range(3):
        proteins.update(extract_proteins(strand[i:]))
    for i in range(3):
        proteins.update(extract_proteins(reverse_comp[i:]))

    return proteins


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()
    proteins = find_orfs(data)

    for prot in proteins:
        print(prot)


main('open_reading_frames.txt')