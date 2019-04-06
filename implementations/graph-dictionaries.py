"""Graphs can be represented as dictionaries. In this representation, keys are vertices and
values are lists or arrays giving the adjacent neighbors to the key-vertex.

Example) Consider the graph dictionary:"""

graph = {
    "a": ["c"],
    "b": ["c", "e"],
    "c": ["a", "b", "d", "e"],
    "d": ["c"],
    "e": ["c", "b"],
    "f": []}

# An edge is given by a 2-tuple with nodes as elements.

def generate_edges(graph):
    """Creates list of edges from a graph-dictionary."""
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edge = (node, neighbor)
            edges.append(edge)
    return edges

print(generate_edges(graph))

"""We could use dictionaries (hash maps) as a way to implement the graph data structure."""

class Graph:
    def __init__(self, graph_dict=None):
        """graph_dict is an initial graph that we can choose to
        expand on by edge addition/deletion."""
        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def vertices(self):
        """gets list of vertices"""
        return list(self._graph_dict.keys())
    
    def edges(self):
        """gets list of edges"""
        edges = []
        for node in self._graph_dict:
            for neighbor in self._graph_dict[node]:
                edge = (node, neighbor)
                edges.append(edge)
        return edges

    def add_vertex(self, vertex):
        """add a vertex to graph_dict unless it is already in it"""
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []
    
    def add_edge(self, edge):
        """add an edge to graph_dict"""
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self._graph_dict:
            self._graph_dict[vertex1].append(vertex2)
        else:
            self._graph_dict[vertex1] = [vertex2]