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
            ["test_remove", self.test_remove]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_doubly_linked_list(self):
        return DoublyLinkedList(5)
    
    def test_constructor(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.head.value == 5  and dll.tail.value == 5 and dll.length == 1

    def test_pop(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.pop().value == 5
    
    def test_pop_first(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.pop_first().value == 5

    def test_append(self):
        dll = self.initialize_test_doubly_linked_list()
        dll.append(10)
        dll.append(15)
        return dll.get(1).value == 10 and dll.get(2).value == 15

    def test_prepend(self):
        dll = self.initialize_test_doubly_linked_list()
        return dll.prepend(100) == True and dll.get(0).value == 100 and dll.length == 2

    def test_get(self):
        dll = self.initialize_test_doubly_linked_list()
        dll.append(10)
        dll.append(15)
        return dll.get(0).value == 5 and dll.get(1).value == 10 and dll.get(2).value == 15

    def test_remove(self):
        dll = self.initialize_test_doubly_linked_list()
        dll.append(10)
        dll.append(15)
        return dll.remove(1).value == 10 and dll.remove(1).value == 15 and dll.remove(0).value == 5