graph = [[1,1,0,0,0],
         [0,1,0,0,1],
         [1,0,0,1,1],
         [0,0,0,0,0]]

# the problem is to count how many islands are in the graph

def island_count(graph):
    if graph is None:
        return 0
    visited = set()
    # dimensions of graph
    n = len(graph)
    m = len(graph[0])
    count = 0
    sizes = []
    # iterate through graph
    for i in range(n):
        for j in range(m):
            # if we haven't visited a node yet, start DFS search
            # otherwise, skip it
            if (i,j) not in visited:
                visited.add((i,j))
                if graph[i][j] == 1:
                    # begin a dfs
                    stack = [(i,j)]
                    island_size = 0
                    while len(stack) > 0:
                        x, y = stack.pop()
                        island_size += 1
                        neighbors = get_neighbors(x,y,graph)
                        for neighbor in neighbors:
                            a, b = neighbor
                            if neighbor not in visited and graph[a][b] == 1:
                                stack.append(neighbor)
                                visited.add(neighbor)
                    count += 1
                    sizes.append(island_size)
    return sizes, count
                     
def get_neighbors(x, y, graph):
    neighbors = []
    n = len(graph)
    m = len(graph[0])
    if x > 0:
        neighbors.append((x-1,y))
    if x < n - 1:
        neighbors.append((x+1,y))
    if y > 0:
        neighbors.append((x,y-1))
    if y < m - 1:
        neighbors.append((x,y+1))
    return neighbors


print(island_count(graph)) 