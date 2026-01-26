from exercises.numerics.Int import *
from ..utils.test_utils import *

class IntTest:
    def __init__(self):
        self.test_configs = [
            ["test_square_root", self.test_square_root],
            ["test_is_armstrong_number", self.test_is_armstrong_number],
            ["test_swap_without_third", self.test_swap_without_third],
            ["test_factorial", self.test_factorial],
            ["test_odd_or_even", self.test_odd_or_even],
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def test_square_root(self):
        return square_root(4) == 2

    def test_is_armstrong_number(self):
        return is_armstrong_number(153) == True and is_armstrong_number(152) == False

    def test_swap_without_third(self):
        return swap_without_third(1, 2) == 2, 1

    def test_factorial(self):
        return factorial(8) == 40320

    def test_odd_or_even(self):
        testOdd = is_odd_even(3) == "odd"
        testEven = is_odd_even(2) == "even"
        testNonInteger = is_odd_even("string") == "non-integer"
        testBoolean = is_odd_even(True) == "non-integer"
        return testOdd and testEven and testNonInteger and testBoolean