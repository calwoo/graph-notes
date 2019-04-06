"""Binary trees are a simple type of graph."""

class BinTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinTree:
    def __init__(self):
        self.root = None
