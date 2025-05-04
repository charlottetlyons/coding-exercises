from exercises.data_structures.Stack import Stack
from ..utils.test_utils import *

class StackTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_push", self.test_push],
            ["test_pop", self.test_pop],
        ]
    
    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_stack(self):
        return Stack(0)

    def test_constructor(self):
        s = self.initialize_test_stack()
        return s.top.value == 0 and s.height == 1

    def test_push(self):
        s = self.initialize_test_stack()
        return s.push(1) == True and s.height == 2

    def test_pop(self):
        s = self.initialize_test_stack()
        popOneResult = s.pop().value == 0 and s.height == 0
        popNoneResult = s.pop() == None and s.height == 0
        s.push(2)
        s.push(3)
        popTwoResult = s.pop().value == 3 and s.pop().value == 2 and s.height == 0
        return popOneResult and popNoneResult and popTwoResult
