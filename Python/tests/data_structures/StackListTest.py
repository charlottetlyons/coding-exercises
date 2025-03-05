from exercises.data_structures.StackList import StackList
from ..utils.test_utils import *


class StackListTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_push", self.test_push],
            ["test_pop", self.test_pop],
            ["test_peek", self.test_peek]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_stack(self):
        return StackList(0)

    def test_constructor(self):
        s = self.initialize_test_stack()
        return len(s.stack) == 1 and s.stack.pop() == 0

    def test_push(self):
        s = self.initialize_test_stack()
        s.push(3)
        return s.stack[1] == 3

    def test_pop(self):
        s = self.initialize_test_stack()
        return s.pop() == 0 and s.pop() == None

    def test_peek(self):
        s = self.initialize_test_stack()
        return s.peek() == 0 and s.pop() == 0
