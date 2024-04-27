from itertools import product

def lexicographic_strings_from_file(filename):
    with open(filename, 'r') as file:
        alphabet = file.readline().strip().split()  # Read the alphabet symbols from the first line
        n = int(file.readline())  # Read the length of strings from the second line

    # Generate all possible combinations of symbols of length n
    combinations = product(alphabet, repeat=n)
    # Sort the combinations lexicographically
    sorted_combinations = sorted(combinations)
    return sorted_combinations



combos = lexicographic_strings_from_file('enum_kmers.txt')
for combo in combos:
    print(''.join(map(str, combo)))