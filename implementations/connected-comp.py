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