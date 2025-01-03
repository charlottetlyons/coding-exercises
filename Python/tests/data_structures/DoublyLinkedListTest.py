from exercises.data_structures.DoublyLinkedList import *
from ..utils.test_utils import *

class DoublyLinkedListTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_pop", self.test_pop],
            ["test_pop_first", self.test_pop_first],
            ["test_append", self.test_append],
            ["test_prepend", self.test_prepend],
            ["test_get", self.test_get],
            ["test_insert", self.test_insert],
            ["test_remove", self.test_remove],
            ["test_swap_head_tail", self.test_swap_head_tail],
            ["test_reverse", self.test_reverse],
            ["test_is_palindrome", self.test_is_palindrome],
            ["test_swap_pairs", self.test_swap_pairs]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_doubly_linked_list(self):
        dll = DoublyLinkedList(5)
        dll.append(10)
        dll.append(15)
        return dll
    
    def test_constructor(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.head.value == 5  and dll.tail.value == 15 and dll.length == 3

    def test_pop(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.pop().value == 15
    
    def test_pop_first(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.pop_first().value == 5

    def test_append(self):
        dll = self.initialize_test_doubly_linked_list()
        dll.append(15)
        return dll.get(3).value == 15

    def test_prepend(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.prepend(100) == True and dll.get(0).value == 100 and dll.length == 4

    def test_get(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.get(0).value == 5 and dll.get(1).value == 10 and dll.get(2).value == 15

    def test_insert(self):
        dll = self.initialize_test_doubly_linked_list()
        result1 = dll.insert(-1, 20)
        result2 = dll.insert(10, 20)
        result3 = dll.insert(1, 20)
        result4 = dll.get(1).value == 20 and dll.get(0).value == 5
        return not result1 and not result2 and result3 and result4

    def test_remove(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.remove(1).value == 10 and dll.remove(1).value == 15 and dll.remove(0).value == 5
    
    def test_swap_head_tail(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.swap_head_tail() and dll.get(2).value == 5 and dll.get(0).value == 15

    def test_reverse(self):
        dll = self.initialize_test_doubly_linked_list()
        dll.reverse()
        return dll.values() == [15, 10, 5]

    def test_is_palindrome(self):
        dll = DoublyLinkedList(5)
        test_one_or_less_result = dll.is_palindrome()
        dll.append(10)
        dll.append(15)
        test_false = not dll.is_palindrome()
        dll.append(10)
        dll.append(5)
        test_true = dll.is_palindrome()
        return test_false and test_one_or_less_result and test_true

    def test_swap_pairs(self):
        dll = self.initialize_test_doubly_linked_list()
        dll.append(20)
        dll.append(25)
        dll.swap_values()
        return dll.values() == [10, 5, 20, 15, 25]