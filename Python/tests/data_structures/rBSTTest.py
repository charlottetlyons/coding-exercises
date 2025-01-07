
from exercises.data_structures.rBST import rBST
from ..utils.test_utils import *

class rBSTTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_insert", self.test_insert],
            ["test_delete", self.test_delete],
            ["test_contains", self.test_contains],
            ["test_preorder_search", self.test_preorder_search],
            ["test_inorder_search", self.test_inorder_search],
            ["test_postorder_search", self.test_postorder_search]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)
    
    def initialize_test_bst(self, num_of_values=1):
        bst = rBST(1)
        if num_of_values > 1:
            for i in range(2, num_of_values+1):
                bst.r_insert(i)
        return bst
    
    def test_constructor(self):
        bst = self.initialize_test_bst()
        return bst.root.value == 1

    def test_insert(self):
        bst = self.initialize_test_bst()
        bst.r_insert(10)
        return bst.pre_order_dfs() == [1, 10]
    
    def test_delete(self):
        bst = self.initialize_test_bst(num_of_values=2)
        result1 = bst.delete_node(0)
        result2 = bst.delete_node(1)
        return result1.value == 1 and result2.value == 2

    def test_contains(self):
        bst = self.initialize_test_bst(num_of_values=3)
        return bst.r_contains(1) and bst.r_contains(2) and bst.r_contains(3) and not bst.r_contains(4)

    
    def test_preorder_search(self):
        bst = self.initialize_test_bst(num_of_values=5)
        return bst.pre_order_dfs() == [1, 2, 3, 4, 5]
    
    def test_inorder_search(self):
        bst = self.initialize_test_bst(num_of_values=5)
        return bst.in_order_dfs() == [1, 2, 3, 4, 5]
    
    def test_postorder_search(self):
        bst = self.initialize_test_bst(num_of_values=5)
        return bst.post_order_dfs() == [5, 4, 3, 2, 1]