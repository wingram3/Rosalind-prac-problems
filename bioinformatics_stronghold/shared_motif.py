
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

    return [sequences[seq] for seq in sequences]


def find_longest_common_substring(sequences):
    def check_common_substring(length):
        # Take the first sequence as the reference sequence
        reference = sequences[0]
        for i in range(len(reference) - length + 1):
            # Get a candidate substring of the desired length
            candidate = reference[i:i + length]
            # Check if this candidate is in all other sequences
            if all(candidate in seq for seq in sequences[1:]):
                return candidate
        return None

    # Binary search on the length of the substring
    low, high = 0, min(len(seq) for seq in sequences)
    result = ""
    while low <= high:
        mid = (low + high) // 2
        candidate = check_common_substring(mid)
        if candidate:
            low = mid + 1
            result = candidate  # Update result with the latest, longest found substring
        else:
            high = mid - 1

    return result


with open('shared_motif.txt', 'r') as file:
    data = file.read()
sequences = parse_fasta(data)
print(find_longest_common_substring(sequences))