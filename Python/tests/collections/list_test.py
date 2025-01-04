from exercises.collections.list import *
from ..utils.test_utils import *

class ListTest:
    def __init__(self):
        self.default_list = [2, 3, 5, 6, 8, 10, 1, 4, 9, 7]
        self.default_list_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.test_configs = [
            ["test_access_indices", self.test_access_indices],
            ["test_max_value", self.test_max_value],
            ["test_bubble_sort", self.test_bubble_sort],
            ["test_selection_sort", self.test_selection_sort],
            ["test_insertion_sort", self.test_insertion_sort],
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_list(self):
        return self.default_list

    def test_access_indices(self):
        l = self.initialize_list()
        return access_indices(l) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_max_value(self):
        l = self.initialize_list()
        return max_value(l) == 10
    
    def test_bubble_sort(self):
        l = self.initialize_list()
        return bubble_sort(l) == self.default_list_sorted
    
    def test_selection_sort(self):
        l = self.initialize_list()
        return selection_sort(l) == self.default_list_sorted

    def test_insertion_sort(self):
        l = self.initialize_list()
        return insertion_sort(l) == self.default_list_sorted
