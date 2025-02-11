from exercises.collections.string import *
from ..utils.test_utils import *

class StringTest:
    def __init__(self):
        self.test_configs = [
            ["test_first_unique_character", self.test_first_unique_character],
            ["test_is_anagrams", self.test_is_anagrams]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def test_first_unique_character(self):
        s1 = "oohhello world"
        s2 = "aabbcc"
        return first_unique_character(s1) == 'e' and first_unique_character(s2) == None
    
    def test_is_anagrams(self):
        return is_anagrams("cat", 'tac') and is_anagrams("dumamarke", 'marmaduke') and not is_anagrams("asdf", "abcde") and not is_anagrams('aabb', 'ab')