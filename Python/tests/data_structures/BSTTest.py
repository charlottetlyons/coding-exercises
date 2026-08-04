from exercises.data_structures.BST import *
from ..utils.test_utils import *
import random

class BSTTest:
    def __init__(self):
        # TODO: redo BST and rBST search tests
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_insert", self.test_insert],
            ["test_delete", self.test_delete],
            ["test_contains", self.test_contains],
            ["test_preorder_dfs", self.test_preorder_dfs],
            ["test_inorder_dfs", self.test_inorder_dfs],
            ["test_postorder_dfs", self.test_postorder_dfs],
            ["test_bfs", self.test_bfs],
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_bst(self, values=[]):
        length = len(values)
        if length > 0:
            bst = BST(values[0])
            for i in range(1, length, 1):
                bst.insert(values[i])
        else:
            return BST(5)
        return bst

    def test_constructor(self):
        bst = self.initialize_test_bst()
        return bst.root.value == 5

    def test_insert(self):
        bst = self.initialize_test_bst()
        bst.insert(10)
        return bst.inorder_dfs() == [5, 10]

    def test_delete(self):
        empty_tree = self.initialize_test_bst([])
        empty_tree.delete(5)
        one_element = self.initialize_test_bst([5])
        not_present = self.initialize_test_bst([5, 2, 3, 6])
        remove_leaf = self.initialize_test_bst([5, 2, 6, 4])
        remove_with_one_child = self.initialize_test_bst([6, 5, 4])
        remove_with_two_children = self.initialize_test_bst([3, 2, 6, 4, 8])
        remove_root = self.initialize_test_bst([4, 7, 8])

        return (
            (not empty_tree.delete(0) and empty_tree.inorder_dfs() == []) and
            (one_element.delete(5) and one_element.inorder_dfs() == ([])) and
            (not not_present.delete(0) and not_present.inorder_dfs() == ([2, 3, 5, 6])) and
            (remove_leaf.delete(4) and remove_leaf.inorder_dfs() == ([2, 5, 6])) and
            (remove_with_one_child.delete(5) and remove_with_one_child.inorder_dfs() == [4, 6]) and
            (remove_with_two_children.delete(6) and remove_with_two_children.inorder_dfs() == [2, 3, 4, 8]) and
            (remove_root.delete(7) and remove_root.inorder_dfs() == [4, 8] and remove_root.root.value == 4)
        )

    def test_contains(self):
        bst = self.initialize_test_bst()
        return bst.contains(5) and not bst.contains(1)

    def test_preorder_dfs(self):
        bst = self.initialize_test_bst([3, 2, 6, 4, 8])
        return bst.preorder_dfs() == [3, 2, 6, 4, 8]

    def test_inorder_dfs(self):
        bst = self.initialize_test_bst([3, 2, 6, 4, 8])
        return bst.inorder_dfs() == [2, 3, 4, 6, 8]

    def test_postorder_dfs(self):
        bst = self.initialize_test_bst([3, 2, 6, 4, 8])
        return bst.postorder_dfs() == [2, 4, 8, 6, 3]

    def test_bfs(self):
        bst = self.initialize_test_bst([3, 2, 6, 4, 8])
        return bst.bfs() == [3, 2, 6, 4, 8]
