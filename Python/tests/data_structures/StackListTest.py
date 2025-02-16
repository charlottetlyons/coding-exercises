
from exercises.data_structures.StackList import StackList
from ..utils.test_utils import *

class StackListTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
        ]
    
    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_stack(self):
        return StackList(0)

    def test_constructor(self):
        s = self.initialize_test_stack()
        return len(s.stack) == 1 and s.stack.pop() == 0