class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value):
        new_node = BSTNode(value)
        self.root = new_node