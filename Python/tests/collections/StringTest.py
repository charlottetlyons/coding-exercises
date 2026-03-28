from exercises.collections.string import *
from ..utils.test_utils import *


class StringTest:
    def __init__(self):
        self.test_configs = [
            ["test_count_occurrences_of_n", self.test_count_occurrences_of_n],
            ["test_count_occurrences", self.test_count_occurrences],
            ["test_first_unique_character", self.test_first_unique_character],
            ["test_is_anagrams", self.test_is_anagrams],
            ["test_max_char", self.test_max_char],
            ["test_only_digits", self.test_only_digits],
            ["test_recursive_reverse", self.test_recursive_reverse],
            ["test_vowels_and_consonants", self.test_vowels_and_consonants],
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def test_count_occurrences_of_n(self):
        test_no_occurrences = count_occurrences_of_n("adfg", "s") == 0
        test_one_occurrences = count_occurrences_of_n("asdf", "s") == 1
        test_multiple_occurrences = count_occurrences_of_n("asdsdfs", "s") == 3
        test_empty_string = count_occurrences_of_n("", "s") == 0
        return (
            test_no_occurrences
            and test_one_occurrences
            and test_multiple_occurrences
            and test_empty_string
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

    def test_max_char(self):
        return (
            max_char("") == None
            and max_char("x") == "x"
            and max_char("aabc") == "a"
            and max_char("abbc") == "b"
            and max_char("aabccc") == "c"
        )

    def test_only_digits(self):
        string1 = "53245"
        string2 = "14533s"
        string3 = "1e533"
        string4 = ""

        return (
            only_digits(string1) == True
            and only_digits(string2) == False
            and only_digits(string3) == False
            and only_digits(string4) == False
        )

    def test_recursive_reverse(self):
        return recursive_reverse("asdfg") == "gfdsa"

    def test_vowels_and_consonants(self):
        empty_string = ""
        no_vowels = "cdng"
        no_consonants = "aeuoi"
        mixed_string = "coding"
        capitalize_string = "ABeeb"
        return (
            vowels_and_consonants(empty_string) == [0, 0]
            and vowels_and_consonants(no_vowels) == [0, 4]
            and vowels_and_consonants(no_consonants) == [5, 0]
            and vowels_and_consonants(mixed_string) == [2, 4]
            and vowels_and_consonants(capitalize_string) == [3, 2]
        )
