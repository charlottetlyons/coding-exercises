class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, value):
        new_node = BSTNode(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is not None:
            temp = self.root
            while True:
                if value == temp.value:
                    return temp
                elif value < temp.value:
                    if temp.left == None:
                        return False
                    temp = temp.left
                else:
                    if temp.right == None:
                        return False
                    temp = temp.right
        else:
            return False

    def preorder_search(self):
        result = []
        if not self.root:
            return result

        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

    def inorder_search(self):
        result = []
        if not self.root:
            return result

        stack = [self.root]

        while stack:
            current = stack.pop()

            if current.right:
                stack.append(current.right)
            result.append(current.value)
            if current.left:
                stack.append(current.left)

        return result

    def postorder_search(self):
        result = []
        if not self.root:
            return result

        stack = [self.root]

        while stack:
            current = stack.pop()

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            result.append(current.value)

        return result
