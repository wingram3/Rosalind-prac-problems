from collections import deque

# build an edge list in edge list format out of the txt file
def parse_data(filename):
    edge_list = []  # first item is (n - num vertices, m - num edges)
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            num1, num2 = int(parts[0]), int(parts[1])
            edge_list.append((num1, num2))
    return edge_list 


# find the shortest path in an unweighted graph
def bfs(edge_list):
    n = edge_list[0][1]     # number of edges in the graph
    distances = [-1] * (n + 1)
    distances[1] = 0        # distance from node 1 to itself is zero

    # construct adjacency list representation of the graph - dict of each node and list of its resp. neighbor nodes
    graph = {i: [] for i in range(1, n+1)}
    for edge in edge_list[1:]:
        graph[edge[0]].append(edge[1])

    # perform bfs
    queue = deque([1])
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
    
    return distances[1: edge_list[0][0]+1]



edge_list = parse_data('rosalind_bfs.txt')
distances = bfs(edge_list)
print(' '.join(map(str, distances)))