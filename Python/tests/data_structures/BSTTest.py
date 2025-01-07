from exercises.data_structures.BST import *
from ..utils.test_utils import *
class BSTTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_insert", self.test_insert],
            ["test_contains", self.test_contains],
            ["test_preorder_search", self.test_preorder_search],
            ["test_inorder_search", self.test_inorder_search],
            ["test_postorder_search", self.test_postorder_search]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)
    
    def initialize_test_bst(self, num_of_values=1):
        bst = BST(1)
        
        if num_of_values > 1:
            for i in range(2, num_of_values+1):
                bst.insert(i)
        return bst
    
    def test_constructor(self):
        bst = self.initialize_test_bst()
        return bst.root.value == 1

    def test_insert(self):
        bst = self.initialize_test_bst()
        bst.insert(10)
        return bst.preorder_search() == [1, 10]
    
    def test_contains(self):
        bst = self.initialize_test_bst(num_of_values=3)
        return bst.contains(2) and not bst.contains(5)

    def test_preorder_search(self):
        bst = self.initialize_test_bst(num_of_values=5)
        return bst.preorder_search() == [1, 2, 3, 4, 5]
    
    def test_inorder_search(self):
        bst = self.initialize_test_bst(num_of_values=5)
        return bst.preorder_search() == [1, 2, 3, 4, 5]
    
    def test_postorder_search(self):
        bst = self.initialize_test_bst(num_of_values=5)
        return bst.preorder_search() == [1, 2, 3, 4, 5]