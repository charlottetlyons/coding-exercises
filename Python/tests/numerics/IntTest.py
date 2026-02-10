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
            ["test_is_prime", self.test_is_prime],
            ["test_is_palindrome", self.test_is_palindrome],
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
    
    def test_is_prime(self):
        test_zero = is_prime(0) 
        test_one = is_prime(1)
        test_even = is_prime(2)
        test_prime3 = is_prime(3)
        test_prime7 = is_prime(7)
        test_prime13 = is_prime(13)
        test_not_prime = is_prime(24)
        return test_zero == False and test_one == False and test_even == True and test_prime3 == True and test_prime7 == True and test_prime13 == True and test_not_prime == False

    def test_is_palindrome(self):
        test_not_palindrome = is_palindrome(234)
        test_is_palindrome_even = is_palindrome(121)
        test_is_palindrome_odd = is_palindrome(12321)
        return not test_not_palindrome and test_is_palindrome_even and test_is_palindrome_odd