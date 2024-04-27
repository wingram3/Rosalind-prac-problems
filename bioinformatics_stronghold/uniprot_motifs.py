import requests

def find_motif_locations(sequence):
    motif = 'N{P}[ST]{P}'
    locations = []
    motif_length = len(motif)
    for i in range(len(sequence) - motif_length+1):
        if sequence[i] == 'N' and sequence[i+1] != 'P' and sequence[i+2] in ['S', 'T'] and sequence[i+3] != 'P':
            locations.append(i + 1)
    return locations


def get_protein_sequence(uniprot_id):
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.ok:
        fasta_data = response.text
        sequences = []
        for record in fasta_data.split('\n'):
            if record.startswith('>'):
                sequences.append('')
            else:
                sequences[-1] += record
        return sequences
    else:
        print(f'failed to retrieve sequence for uniprot ID: {uniprot_id}')
        return None
    

def main():
    uniprot_ids = ['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']
    for uniprot_id in uniprot_ids:
        sequence = get_protein_sequence(uniprot_id)
        if sequence:
            motif_locations = find_motif_locations(sequence)
            if motif_locations:
                print(f"{uniprot_id}: {' '.join(map(str, motif_locations))}")
            else:
                print(f"{uniprot_id}: No N-glycosylation motif found")


if __name__ == '__main__':
    main()

