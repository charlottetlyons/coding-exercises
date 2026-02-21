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
        if not self.root:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if temp.value == value:
                return False
            elif temp.value > value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    def delete(self, value):
        if not self.root:
            return False
        parent, current = None, self.root
        while current and current.value is not value:
            parent = current
            if current.value > value:
                current = current.left
            else:
                current = current.right

        if not current:
            return self.root

        if current.left and current.right:
            successor_parent, successor = current, current.right
            while successor.left:
                successor_parent, successor = successor, successor.left
            current.value = successor.value
            current, parent = successor, successor_parent

        if current.left:
            child = current.left
        else:
            child = current.right
        if not parent:
            return child

        if parent.left is current:
            parent.left = child
        else:
            parent.right = child

        return True

    def contains(self, value):
        if self.root:
            temp = self.root
            while True:
                if temp.value == value:
                    return temp
                elif temp.value > value:
                    if not temp.left:
                        return False
                    temp = temp.left
                else:
                    if not temp.right:
                        return False
                    temp = temp.right
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
        if not self.root:
            return []

        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def postorder_search(self):
        if not self.root:
            return []

        result = []
        stack = []
        prev = None
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack[-1]

            if current.right and current.right is not prev:
                current = current.right
            else:
                result.append(current.value)
                prev = current
                stack.pop()
                current = None
        return result

    def print_leaves(self):
        def __r_print_leaves(current):
            if current is None:
                return
            if current.left is None and current.right is None:
                print(current.value)
            __r_print_leaves(current.left)
            __r_print_leaves(current.right)
        __r_print_leaves(self.root)
