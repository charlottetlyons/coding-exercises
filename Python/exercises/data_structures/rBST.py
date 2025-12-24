from exercises.data_structures.BST import BSTNode

class rBST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def __r_insert(self, current_node, value):
        if current_node == None: 
            return BSTNode(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = BSTNode(value)
        self.__r_insert(self.root, value)  

    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def delete_node(self, value):
        return self.__delete_node(self.root, value)

    def __delete_node(self, current, value):
        if current is None:
            return None
        elif value < current.value:
            current.left = self.__delete_node(current.left, value)
        elif value > current.value:
            current.right = self.__delete_node(current.right, value) 
        else:
            if current.left is None and current.right is None:
                return None
            elif current.left is None:
                current = current.right
            elif current.right is None:
                current = current.left
            else:
                sub_tree_min = self.min_value(current.right)
                current.value = sub_tree_min
                current.right = self.__delete_node(current.right, sub_tree_min)
        return current

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_contains(self, current, value):
        if not current:
            return False
        elif current.value == value:
            return True
        elif current.value > value:
            return self.__r_contains(current.left, value)
        else:
            return self.__r_contains(current.right, value)

    def pre_order_dfs(self):
        results = []

        def traverse(current):
            results.append(current.value)
            if current.left is not None:
                traverse(current.left)
            if current.right is not None:
                traverse(current.right)

        traverse(self.root)
        return results

    def in_order_dfs(self):
        results = []

        def traverse(current):
            if current.left is not None:
                traverse(current.left)
            results.append(current.value)
            if current.right is not None:
                traverse(current.right)

        traverse(self.root)
        return results

    def post_order_dfs(self):
        results = []

        def traverse(current):
            if current.left is not None:
                traverse(current.left)
            if current.right is not None:
                traverse(current.right)
            results.append(current.value)

        traverse(self.root)
        return results
