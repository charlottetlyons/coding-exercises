from exercises.collections.string import *
from ..utils.test_utils import *

class StringTest:
    def __init__(self):
        self.test_configs = [
            ["test_first_unique_character", self.test_first_unique_character],
            ["test_is_anagrams", self.test_is_anagrams],
            ["test_count_occurrences", self.test_count_occurrences],
            ["test_max_char", self.test_max_char],
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def test_first_unique_character(self):
        s1 = "oohhello world"
        s2 = "aabbcc"
        return first_unique_character(s1) == "e" and first_unique_character(s2) == None

    def test_is_anagrams(self):
        return (
            is_anagrams("cat", "tac")
            and is_anagrams("dumamarke", "marmaduke")
            and not is_anagrams("asdf", "abcde")
            and not is_anagrams("aabb", "ab")
        )

    def test_count_occurrences(self):
        return (
            count_occurrences("") == {}
            and count_occurrences("x") == {"x": 1}
            and count_occurrences("aabc")
            == {
                "a": 2,
                "b": 1,
                "c": 1,
            }
            and count_occurrences("abbc")
            == {
                "a": 1,
                "b": 2,
                "c": 1,
            }
            and count_occurrences("aabccc")
            == {
                "a": 2,
                "b": 1,
                "c": 3,
            }
        )

    def test_max_char(self):
        return (
            max_char("") == None
            and max_char("x") == "x"
            and max_char("aabc") == "a"
            and max_char("abbc") == "b"
            and max_char("aabccc") == "c"
        )
