from exercises.collections.list import *
from ..utils.test_utils import *

class ListTest:
    def __init__(self):
        self.test_configs = [
            ["test_access_indices", self.test_access_indices],
            ["test_max_value", self.test_max_value]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def test_access_indices(self):
        l = [23, 26, 11, 76, 24, 23]
        return access_indices(l) == [0, 1, 2, 3, 4, 5]

    def test_max_value(self):
        l = [1, 7, 6, 3, 4, 5, 2, 6]
        return max_value(l) == 7