from exercises.data_structures.Stack import Stack
from ..utils.test_utils import *

class StackTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
        ]
    
    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_queue(self):
        return Stack(0)

    def test_constructor(self):
        s = self.initialize_test_queue()
        return s.top.value == 0 and s.height == 1