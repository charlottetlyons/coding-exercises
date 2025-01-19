from exercises.collections.string import *
from ..utils.test_utils import *

class StringTest:
    def __init__(self):
        self.test_configs = [
            ["test_first_unique_character", self.test_first_unique_character]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def test_first_unique_character(self):
        s1 = "oohhello world"
        s2 = "aabbcc"
        return first_unique_character(s1) == 'e' and first_unique_character(s2) == None