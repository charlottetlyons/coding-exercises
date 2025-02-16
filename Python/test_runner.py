from tests.numerics.IntTest import IntTest
from tests.collections.StringTest import StringTest
from tests.collections.StringTest import StringTest
from tests.collections.ListTest import ListTest
from tests.data_structures.LinkedListTest import LinkedListTest
from tests.data_structures.DoublyLinkedListTest import DoublyLinkedListTest
from tests.data_structures.QueueTest import QueueTest
from tests.data_structures.StackTest import StackTest
from tests.data_structures.StackListTest import StackListTest
from tests.data_structures.HashTableTest import HashTableTest
from tests.data_structures.MaxHeapTest import MaxHeapTest
from tests.data_structures.MinHeapTest import MinHeapTest
from tests.data_structures.GraphTest import GraphTest
from tests.data_structures.BSTTest import BSTTest
from tests.data_structures.rBSTTest import rBSTTest

# Test Cases
# TODO: make a DataStructureTest Interface/abstract if applicable, so the test running logic is reusable
# TODO: Test interface with name and test_function properties
# TODO: integrate a python testing library
int_test = IntTest()
string_test = StringTest()
list_test = ListTest()
linked_list_test = LinkedListTest()
doubly_linked_list_test = DoublyLinkedListTest()
hash_table_test = HashTableTest()
max_heap_test = MaxHeapTest()
min_heap_test = MinHeapTest()
queue_test = QueueTest()
stack_test = StackTest()
stack_list_test = StackListTest()
graph_test = GraphTest()
bst_test = BSTTest()
rbst_test = rBSTTest()

test_suites = [
    ["Integer", int_test],
    ["String", string_test],
    ["List", list_test],
    ["LinkedList", linked_list_test],
    ["DoublyLinkedListTest", doubly_linked_list_test],
    ["Hash Table", hash_table_test],
    ["Max Heap", max_heap_test],
    ["Min Heap", min_heap_test],
    ["Queue", queue_test],
    ["Stack (LinkedList)", stack_test],
    ["Stack (list)", stack_list_test],
    ["Graph", graph_test],
    ["Binary Search Tree", bst_test],
    ["Recursive Binary Search Tree", rbst_test]
]

for test_suite in test_suites:
    print(test_suite[0])
    test_suite[1].run_all_tests()
    print()
