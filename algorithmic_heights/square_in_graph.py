import numpy as np

def parse_graph_file(filename):
    graphs = []  # List to store graphs

    with open(filename, 'r') as file:
        k = None  
        for line in file:
            line = line.strip()  

            if not line:
                continue
            
            if k is None:
                k = int(line)
                continue

            vertices, edges = map(int, line.split())
            graph = [(vertices, edges)]

            for _ in range(edges):
                edge = tuple(map(int, file.readline().strip().split())) 
                graph.append(edge)

            graphs.append(graph)

    return graphs


def build_adj_matrix(graphs):
    adj_matrices = []
    for graph in graphs:
        n = graph[0][0]
        adj_matrix = np.zeros((n, n), dtype=int)

        for edge in graph[1:]:
            u, v = edge
            adj_matrix[u-1][v-1] = 1
            adj_matrix[v-1][u-1] = 1
        adj_matrices.append(adj_matrix)

    # list of numpy arrays
    return adj_matrices


def find_squares(adj_matrices):
    cycle_present = []
    for matrix in adj_matrices:
        n = matrix.shape[0]
        cycle_found = False

        for u in range(n):
            for v in range(u + 1, n):
                if matrix[u][v] == 1:
                    for w in range(n):
                        if matrix[v][w] == 1 and matrix[u][w] == 0:
                            cycle_found = True
                            break
                    if cycle_found:
                        break
            if cycle_found:
                break

        if cycle_found:
            cycle_present.append(1)
        else:
            cycle_present.append(-1)

    return cycle_present



graphs = parse_graph_file('square_in_graph.txt')
adj_matrices = build_adj_matrix(graphs)
square_present = find_squares(adj_matrices)
print(graphs)
print(adj_matrices)
print(square_present)