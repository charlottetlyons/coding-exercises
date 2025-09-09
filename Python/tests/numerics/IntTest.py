from exercises.numerics.int import *
from ..utils.test_utils import *


class IntTest:
    def __init__(self):
        self.test_configs = [
            ["test_square_root", self.test_square_root],
            ["test_is_armstrong_number", self.test_is_armstrong_number],
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def test_square_root(self):
        return square_root(4) == 2

    def test_is_armstrong_number(self):
        return is_armstrong_number(153) == True and is_armstrong_number(152) == False
