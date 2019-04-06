import sys
sys.path.insert(0, "./implementations/")

from adjacency_list import Graph

def construct_graph(words):
    d = {}
    g = Graph()
    # form buckets of words that differ by one letter
    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # after creating buckets, store into a graph
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g

# to find the shortest path in this graph from one word to another, we use BFS

from collections import queue

