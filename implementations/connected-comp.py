"""Our model for a graph will be an adjacency list."""

class Graph:
    def __init__(self, graph_dict=None):
        """initializes a graph"""
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        """returns list of vertices"""
        return list(self.graph_dict.keys())
    
    def edges(self):
        """returns list of edges"""
        edges = []
        for vertex in self.graph_dict.keys():
            for neighbor, weight in self.graph_dict[vertex].iteritems():
                if (neighbor, vertex, weight) not in edges:
                    edges.append([vertex, neighbor, weight])
        return edges

    def add_vertex(self, vertex):
        """add a vertex"""
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = {}
    
    def add_edge(self, edge, weight=1):
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1][vertex2] = weight
        else:
            self.graph_dict[vertex1] = {vertex2: weight}
        if vertex2 in self.graph_dict:
            self.graph_dict[vertex2][vertex1] = weight
        else:
            self.graph_dict[vertex2] = {vertex1: weight}

"""We can use breadth-first search to look for the minimum moves
to go from one node to another (assume unweighted graph)."""

def bfs(graph, start):
    visited = set()
    visited.add(start)
    paths = {start: ":"}
    queue = [start]
    while len(queue) > 0:
        vertex = queue.pop(0)
        for neighbor, _ in graph[vertex].iteritems():
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                paths[neighbor] = paths[vertex] + "->" + vertex
    return paths

def bfs_connected_components(graph):
    connected_components = []
    num_cc = 0
    vertices = graph.keys()
    while len(vertices) > 0:
        vertex = vertices.pop()
        queue = [vertex]
        visited = set()
        while len(queue) > 0:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                num_cc += 1
            for neighbor, _ in graph[v].iteritems():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    vertices.remove(neighbor)
        connected_components.append(visited)
    return connected_components, num_cc

