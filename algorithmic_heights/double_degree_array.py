
def parse_data(filename):
    edge_list = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            num1, num2 = int(parts[0]), int(parts[1])
            edge_list.append((num1, num2))
    return edge_list  


def build_adj_list(edge_list):
    adj_list = {}
    for u, v in edge_list[1:]:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []

        adj_list[u].append(v)
        adj_list[v].append(u)

    # if a node has no neighbors, add the node to adj_list with an empty list as its value
    if edge_list[0][0] > len(adj_list):
        for i in range(1, edge_list[0][0]+1):
            if i not in adj_list:
                adj_list[i] = []
    return adj_list


def sum_of_degrees(adj_list):
    degrees = {vertex: len(neighbors) for vertex, neighbors in adj_list.items()}
    D = [0] * (len(adj_list)+1)

    for vertex in adj_list:
        D[vertex] = sum(degrees[neighbor] for neighbor in adj_list[vertex])

    return D[1:]



edge_list = parse_data('rosalind_ddeg.txt')
adj_list = build_adj_list(edge_list)
D = sum_of_degrees(adj_list)
print(' '.join(map(str, D)))