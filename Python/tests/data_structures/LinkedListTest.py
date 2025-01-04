from exercises.data_structures.LinkedList import *
from ..utils.test_utils import *

class LinkedListTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_pop_first", self.test_pop_first],
            ["test_pop", self.test_pop],
            ["test_prepend", self.test_prepend],
            ["test_append", self.test_append],
            ["test_print", self.test_print],
            ["test_get", self.test_get],
            ["test_set", self.test_set],
            ["test_insert", self.test_insert],
            ["test_remove", self.test_remove],
            ["test_get_length", self.test_get_length],
            ["test_functions_out_of_bounds", self.test_functions_out_of_bounds],
            ["test_reverse", self.test_reverse],
            ["test_median_node", self.test_median_node],
            ["test_kth_node_from_end", self.test_kth_node_from_end],
            ["test_reverse_between", self.test_reverse_between],
            ["test_partition_list", self.test_partition_list],
            ["test_remove_duplicates", self.test_remove_duplicates],
            ["test_bubble_sort", self.test_bubble_sort],
            ["test_selection_sort", self.test_selection_sort],
            ["test_insertion_sort", self.test_insertion_sort]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_linked_list(
        self, num_of_values=3, is_sorted=True, custom_list=None
    ):
        ll = LinkedList(1)
        if custom_list:
            ll.pop_first()
            for value in custom_list:
                ll.append(value)
        else:
            if is_sorted:
                for value in range(2, num_of_values + 1):
                    ll.append(value)
            else:
                for value in range(num_of_values + 1, 2):
                    ll.append(value)
        return ll

    def test_constructor(self):
        ll = LinkedList(1)
        return ll.get(0).value == 1 and ll.length == 1

    def test_pop_first(self):
        ll = self.initialize_test_linked_list()
        return ll.pop_first().value == 1 and ll.length == 2

    def test_pop(self):
        ll = self.initialize_test_linked_list()
        return ll.pop().value == 3 and ll.length == 2

    def test_prepend(self):
        ll = self.initialize_test_linked_list()
        ll.prepend(4)
        return ll.get(0).value == 4 and ll.length == 4

    def test_append(self):
        ll = self.initialize_test_linked_list()
        ll.append(4)
        return ll.get(3).value == 4 and ll.length == 4

    # TODO: this seems annoying, do later
    def test_print(self):
        return True

    def test_get(self):
        ll = self.initialize_test_linked_list()
        return ll.get(1).value == 2

    def test_functions_out_of_bounds(self):
        ll = self.initialize_test_linked_list()
        pre_index = -1
        post_index = 4
        test_value = 5
        test_configs = [
            dict(
                test_name="test_linked_list_get_out_of_bounds",
                linked_list_function=ll.get,
                expected_result=None,
                needs_value=False,
            ),
            dict(
                test_name="test_linked_list_set_out_of_bounds",
                linked_list_function=ll.set,
                expected_result=False,
                needs_value=True,
            ),
            dict(
                test_name="test_linked_list_insert_out_of_bounds",
                linked_list_function=ll.insert,
                expected_result=False,
                needs_value=True,
            ),
            dict(
                test_name="test_linked_list_remove_out_of_bounds",
                linked_list_function=ll.remove,
                expected_result=None,
                needs_value=False,
            ),
        ]

        for test in test_configs:
            if test["needs_value"]:
                test_result = (
                    test["linked_list_function"](pre_index, test_value)
                    == test["expected_result"]
                    and test["linked_list_function"](post_index, test_value)
                    == test["expected_result"]
                )
            else:
                test_result = (
                    test["linked_list_function"](pre_index) == test["expected_result"]
                    and test["linked_list_function"](post_index)
                    == test["expected_result"]
                )
            print(f'{test["test_name"]}: {format_test_result(test_result)}')
            if not test_result:
                return False
        return True

    def test_set(self):
        ll = self.initialize_test_linked_list()
        ll.set(2, 5)
        return ll.get(2).value == 5

    # TODO: Test first and last insertion cases
    def test_insert(self):
        ll = self.initialize_test_linked_list()
        ll.insert(1, 5)
        return ll.get(1).value == 5 and ll.length == 4

    def test_remove(self):
        ll = self.initialize_test_linked_list()
        return ll.remove(1).value == 2 and ll.length == 2

    def test_get_length(self):
        ll = self.initialize_test_linked_list()
        return ll.get_length() == 3

    def test_reverse(self):
        ll = LinkedList(7)
        for num in [3, 6, 2, 6, 1, 4]:
            ll.append(num)
        expected_order = [4, 1, 6, 2, 6, 3, 7]
        ll.reverse()
        return ll.values() == expected_order

    def test_median_node(self):
        ll = self.initialize_test_linked_list()
        return ll.median_node().value == 2

    def test_kth_node_from_end(self):
        ll = self.initialize_test_linked_list(num_of_values=5)
        return (
            ll.kth_node_from_end(2).value == 4
            and ll.kth_node_from_end(1).value == 5
            and ll.kth_node_from_end(5).value == 1
            and ll.kth_node_from_end(0) == None
            and ll.kth_node_from_end(6) == None
        )

    def test_reverse_between(self):
        ll = self.initialize_test_linked_list(num_of_values=5)
        ll.reverse_between(1, 3)
        return ll.values() == [1, 4, 3, 2, 5]

    def test_partition_list(self):
        ll = self.initialize_test_linked_list(custom_list=[1, 3, 2, 3, 1, 14])
        ll.partition_list(3)
        return ll.values() == [1, 2, 1, 3, 3, 14]

    def test_values(self):
        return self.initialize_test_linked_list().values() == [1, 2, 3, 4, 5]

    def test_remove_duplicates(self):
        ll = self.initialize_test_linked_list(custom_list=[1, 1, 2, 3, 3, 3])
        ll.remove_duplicates()
        return ll.values() == [1, 2, 3]

    def test_bubble_sort(self):
        ll = self.initialize_test_linked_list(custom_list=[4, 2, 5, 3, 1, 6, 2])
        ll.bubble_sort()
        return ll.values() == [1, 2, 2, 3, 4, 5, 6] and ll.head.value == 1 and ll.tail.value == 6
    
    def test_selection_sort(self):
        ll = self.initialize_test_linked_list(custom_list=[4, 2, 5, 3, 1, 6, 2])
        ll.selection_sort()
        return ll.values() == [1, 2, 2, 3, 4, 5, 6] and ll.head.value == 1 and ll.tail.value == 6

    def test_insertion_sort(self):
        ll = self.initialize_test_linked_list(custom_list=[4, 2, 5, 3, 1, 6, 2])
        ll.insertion_sort()
        return ll.values() == [1, 2, 2, 3, 4, 5, 6] and ll.head.value == 1 and ll.tail.value == 6