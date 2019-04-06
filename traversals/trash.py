########
# Graphs

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

#####
# DFS

def dfs(node, target):
    visited = set()
    stack = [node]
    while len(stack) > 0:
        current = stack.pop()
        if node not in visited:
            visited.add(node)
            if node.value == target:
                return True
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
    return False

#####
# BFS

from collections import deque

def bfs(node, target):
    visited = set()
    queue = deque([node])
    while len(queue) > 0:
        current = queue.pop()
        if node not in visited:
            visited.add(node)
            if node.value == target:
                return True
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.appendleft(neighbor)
    return False