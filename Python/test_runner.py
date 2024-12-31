from tests.collections.list_test import ListTest
from tests.data_structures.LinkedListTest import LinkedListTest
from tests.data_structures.DoublyLinkedListTest import DoublyLinkedListTest
from tests.data_structures.QueueTest import QueueTest
from tests.data_structures.HashTableTest import HashTableTest
from tests.data_structures.MaxHeapTest import MaxHeapTest 

# Test Cases
# TODO: make a DataStructureTest Interface/abstract if applicable, so the test running logic is reusable
# TODO: Test interface with name and test_function properties
list_test = ListTest()
linked_list_test = LinkedListTest()
doubly_linked_list_test = DoublyLinkedListTest()
hash_table_test = HashTableTest()
max_heap_test = MaxHeapTest()
queue_test = QueueTest()

test_suites = [
    ["List", list_test],
    ["LinkedList", linked_list_test],
    ["DoublyLinkedListTest", doubly_linked_list_test],
    ["Hash Table", hash_table_test],
    ["Max Heap", max_heap_test],
    ["Queue", queue_test]
]

for test_suite in test_suites:
    print(test_suite[0])
    test_suite[1].run_all_tests()
    print("\n")