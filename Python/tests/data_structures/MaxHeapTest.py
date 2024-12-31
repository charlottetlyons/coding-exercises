from exercises.data_structures.MaxHeap import *
from ..utils.test_utils import *

class MaxHeapTest:
    def __init__(self):
        self.test_configs = self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_left_child", self.test_left_child],
            ["test_right_child", self.test_right_child],
            ["test_parent", self.test_parent],
            ["test_insert_remove", self.test_insert_remove]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_max_heap(self):
        return MaxHeap()

    def test_constructor(self):
        mh = self.initialize_test_max_heap()
        return mh.heap == []

    def test_left_child(self):
        mh = self.initialize_test_max_heap()
        return mh._left_child(2) == 5
    
    def test_right_child(self):
        mh = self.initialize_test_max_heap()
        return mh._right_child(2) == 6
    
    def test_parent(self):
        mh = self.initialize_test_max_heap()
        return mh._parent(2) == 0

    def test_insert_remove(self):
        mh = self.initialize_test_max_heap()
        mh.insert(4)
        return mh.remove() == 4