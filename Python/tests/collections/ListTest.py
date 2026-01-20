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
            ["test_merge_sort", self.test_merge_sort],
            ["test_quick_sort", self.test_quick_sort],
            ["test_median_of_three_quick_sort", self.test_median_of_three_quick_sort],
            ["test_randomized_pivot_quick_sort", self.test_randomized_pivot_quick_sort],
            ["test_length_of_max_value", self.test_length_of_max_value],
            ["test_get_digit", self.test_get_digit],
            ["test_pairs_equal_to_n", self.test_pairs_equal_to_n],
            ["test_missing_of_n", self.test_missing_of_n],
            ["test_remove_duplicates", self.test_remove_duplicates],
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_list(self):
        return self.default_list.copy()

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

    def test_merge_sort(self):
        l = self.initialize_list()
        return merge_sort(l) == self.default_list_sorted

    def test_quick_sort(self):
        l = self.initialize_list()
        return quick_sort(l) == self.default_list_sorted

    def test_median_of_three_quick_sort(self):
        l = self.initialize_list()
        return median_of_three_quick_sort(l) == self.default_list_sorted

    def test_randomized_pivot_quick_sort(self):
        l = self.initialize_list()
        return randomized_pivot_quick_sort(l) == self.default_list_sorted

    # TODO
    def test_pivot(self):
        return True

    def test_length_of_max_value(self):
        l = self.initialize_list()
        return length_of_max_value(l) == 2

    # TODO
    def test_radix_sort(self):
        return True

    def test_get_digit(self):
        return (
            get_digit(100, 1) == 0
            and get_digit(1, 0) == 1
            and get_digit(2632, 3) == 2
            and get_digit(9, 1) == 0
        )

    def test_pairs_equal_to_n(self):
        l = [2, 1, 2, 3, 4, 0]
        expected = [(1, 3), (0, 4), (2, 2)]
        return expected == pairs_equal_to_n(l, 4)

    def test_missing_of_n(self):
        random_int = randint(1, 100)
        l = []
        for num in range(1, 101):
            if num != random_int:
                l.append(num)
        return missing_of_n(l, 100) == random_int

    def test_remove_duplicates(self):
        empty = []
        oneElement = [1]
        multipleNonAdjacentElements = [1, 2, 1, 3, 4, 4, 15, 15, 20]
        noDuplicates = [1, 2, 3, 4, 15, 20]
        onlyDuplicates = [1, 1, 2, 2, 3, 3, 4, 4, 15, 15, 20, 20]
        multipleDuplicates = [1, 1, 1, 2, 1, 3, 4, 4]
        return (
            remove_duplicates(empty) == []
            and remove_duplicates(oneElement) == [1]
            and remove_duplicates(multipleNonAdjacentElements) == [1, 2, 3, 4, 15, 20]
            and remove_duplicates(onlyDuplicates) == [1, 2, 3, 4, 15, 20]
            and remove_duplicates(noDuplicates) == [1, 2, 3, 4, 15, 20]
            and remove_duplicates(multipleDuplicates) == [1, 2, 3, 4]
        )
