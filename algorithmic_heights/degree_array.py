
def parse_data(filename):
    edge_list = []  # first item is (n - num vertices, m - num edges)
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            num1, num2 = int(parts[0]), int(parts[1])
            edge_list.append((num1, num2))
    return edge_list     


def find_degrees(edge_list):
    nodes = {}  # dict of nodes and their resp. degrees
    for item in edge_list[1:]:
        for num in item:
            if num not in nodes:
                nodes[num] = 0

    for item in edge_list[1:]:
        for num in item:
            nodes[num] += 1

    # return degrees in order of their resp. nodes
    return list({key: nodes[key] for key in sorted(nodes)}.values())

    

edge_list = parse_data('rosalind_ddeg.txt')
degrees_list = find_degrees(edge_list)
print(' '.join(map(str, degrees_list))) 
