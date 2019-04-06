########
# Graphs

graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"])}

##########################
# Depth-first search (DFS)

def dfs(graph, start):
    """This primitive search just returns all vertices
    reachable in the graph from the start vertex."""
    visited = set()
    stack = [start]
    while len(stack) > 0:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            # stack.extend(graph[current] - visited)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

print(dfs(graph, "A"))

def dfs_rec(graph, start, visited=None):
    """Recursive implementation of depth-first
    search."""
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start] - visited:
        visited = dfs(graph, neighbor, visited)
    return visited

# if we want to return actual paths, we can also use dfs
def dfs_paths(graph, start, end):
    """DFS search for paths from start to end. We
    modify the above by letting the stack contain more data."""
    # the stack now contains pairs (vertex, [path: start ~> vertex])
    stack = [(start, [start])]
    while len(stack) > 0:
        current_vertex, current_path = stack.pop()
        for next_vertex in graph[current_vertex] - set(current_path):
            if next_vertex == end:
                return current_path + [next_vertex]
            else:
                stack.append((next_vertex, current_path + [next_vertex]))

print(dfs_paths(graph, "D", "C"))

def dfs_paths_rec(graph, start, end, path=None):
    """Recursive version of DFS path search."""
    if path is None:
        path = [start]
    if start == end:
        return path
    else:
        for neighbor in graph[start] - set(path):
            return dfs_paths_rec(graph, neighbor, end, path + [neighbor])

############################
# Breadth-first search (BFS)

def bfs(graph, start):
    """A breadth-first search for finding all such
    vertices connected to a given start vertex."""
    visited = set()
    queue = [start]
    while len(queue) > 0:
        current_vertex = queue.pop(0)
        if current_vertex not in visited:
            visited.add(current_vertex)
            for neighbor in graph[current_vertex] - visited:
                queue.append(neighbor)
    return visited

print(bfs(graph, "A"))

def bfs_paths(graph, start, end):
    """BFS search for paths from start to end. We
    modify the above by letting the stack contain more data."""
    # the queue now contains pairs (vertex, [path: start ~> vertex])
    queue = [(start, [start])]
    while len(queue) > 0:
        current_vertex, current_path = queue.pop(0)
        for next_vertex in graph[current_vertex] - set(current_path):
            if next_vertex == end:
                return current_path + [next_vertex]
            else:
                queue.append((next_vertex, current_path + [next_vertex]))

print(bfs_paths(graph, "D", "C"))

###############
# Shortest path

def shortest_path(graph, start, end):
    try:
        return bfs_paths(graph, start, end)
    except:
        return None