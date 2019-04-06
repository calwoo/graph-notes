"""When sparsity of the graph is a concern, a space-efficient way to store
the graph is via adjacency lists. Here we only keep an array for all the vertices
in the graph, and then maintain lists of all adjacent vertices connected to it."""

################
# Implementation

# we will implement an adjacency list via dictionaries

class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        if neighbor in self.connected_to:
            raise ValueError("already in graph!")
        else:
            self.connected_to[neighbor] = weight

    def get_adjacent_vertices(self):
        return self.connected_to.keys()

    def get_key(self):
        return self.key

    def get_weight_to(self, neighbor):
        return self.connected_to[neighbor]

    def __str__(self):
        return str(self.key) + " connected to: " + str([x.key for x in self.connected_to])

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        new_vert = Vertex(key)
        self.vertices[key] = new_vert
        self.num_vertices += 1
        return new_vert

    def add_edge(self, f, t, weight=0):
        if f not in self.vertices:
            new_vert = self.add_vertex(f)
        if t not in self.vertices:
            new_vert = self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], cost)

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def get_vertices(self):
        return self.vertices.keys()

    def __contains__(self, n):
        return n in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())