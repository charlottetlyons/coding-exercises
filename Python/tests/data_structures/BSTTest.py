from exercises.data_structures.BST import *
from ..utils.test_utils import *
import random


class BSTTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_insert", self.test_insert],
            ["test_delete", self.test_delete],
            ["test_contains", self.test_contains],
            ["test_preorder_search", self.test_preorder_search],
            ["test_inorder_search", self.test_inorder_search],
            ["test_postorder_search", self.test_postorder_search],
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_bst(self, fill=False):
        bst = BST(8)

        if fill:
            values = [3, 10, 1, 6, 14, 4, 7, 13]
            for value in values:
                bst.insert(value)
        return bst

    def test_constructor(self):
        bst = self.initialize_test_bst()
        return bst.root.value == 8

    def test_insert(self):
        bst = self.initialize_test_bst()
        bst.insert(10)
        return bst.inorder_search() == [8, 10]

    def test_delete(self):
        bst = self.initialize_test_bst()
        bst.insert(10)
        bst.insert(11)
        bst.insert(12)
        bst.delete(10)
        return bst.inorder_search() == [8, 11, 12]

    def test_contains(self):
        bst = self.initialize_test_bst(fill=True)
        return bst.contains(10) and not bst.contains(100)

    def test_preorder_search(self):
        bst = self.initialize_test_bst(fill=True)
        return bst.preorder_search() == [8, 3, 1, 6, 4, 7, 10, 14, 13]

    def test_inorder_search(self):
        bst = self.initialize_test_bst(fill=True)
        return bst.inorder_search() == [1, 3, 4, 6, 7, 8, 10, 13, 14]

    def test_postorder_search(self):
        bst = self.initialize_test_bst(fill=True)
        return bst.postorder_search() == [1, 4, 7, 6, 3, 13, 14, 10, 8]
