from exercises.data_structures.BST import *
from ..utils.test_utils import *
class BSTTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)
    
    def initialize_test_bst(self):
        return BST(1) 
    
    def test_constructor(self):
        bst = self.initialize_test_bst()
        return bst.root.value == 1
