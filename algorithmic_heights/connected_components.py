
# build an edge list in edge list format out of the txt file
def parse_data(filename):
    edge_list = []  # first item is (n - num vertices, m - num edges)
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            num1, num2 = int(parts[0]), int(parts[1])
            edge_list.append((num1, num2))
    return edge_list


# depth first search
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# count the number of connected components in a graph using dfs
def count_cc(edge_list):
    num_nodes = edge_list[0][0]     # number of nodes in the graph

    # build adjacency list
    graph = {i: [] for i in range(1, num_nodes+1)}
    for edge in edge_list[1:]:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    num_components = 0
    for node in range(1, num_nodes+1):
        if node not in visited:
            dfs(graph, node, visited)
            num_components += 1

    return num_components




edge_list = parse_data('rosalind_cc.txt')
num_components = count_cc(edge_list)
print(num_components)