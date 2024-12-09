#  TEST UTILITY FUNCTIONS
def format_test_result(result):
    return "\033[32mPass\033[0m" if result else "\033[31mFail\033[0m"

# FUNCTIONS
def access_index(some_list):
    for i in range(len(some_list)):
        print(i)

def max_value(some_list):
    max_value = 0
    for i in some_list:
        if i > max_value:
            max_value = i
    return max_value

# DATA STRUCTURES
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head

        while temp.next:
            prev = temp
            temp = temp.next

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = prev
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def print(self):
        if self.length == 0:
            return

        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def get_length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next
        return count

    def values(self):
        values = []
        temp = self.head
        while temp:
            values.append(temp.value)
            temp = temp.next
        return values

    def reverse(self):
        before = None
        current = self.head
        self.head = self.tail
        self.tail = current

        while current:
            after = current.next
            current.next = before

            before = current
            current = after

    def median_node(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def kth_node_from_tail(self, k):
        slow = fast = self.head
        for _ in range(k):
            if not fast:
                return None
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        return slow

    def reverse_between(self, m, n):
        if self.length == 0:
            return None

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(m):
            prev = prev.next

        current = prev.next

        for _ in range(n - m):
            after = current.next
            current.next = after.next
            after.next = prev.next
            prev.next = after
        self.head = dummy.next

    def partition_list(self, x):
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next

        prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next

    def remove_duplicates(self):
        prev = None
        temp = self.head
        seen = []

        while temp:
            if temp.value in seen:
                prev.next = temp.next
                self.length -= 1
            else:
                seen.append(temp.value)
                prev = temp
            temp = temp.next

    def bubble_sort(self):
        if self.length == 0:
            return None

        is_sorted = False

        while not is_sorted:
            is_sorted = True
            current = self.head
            compare = current.next

            while compare:
                if compare.value < current.value:
                    is_sorted = False
                    compare.value, current.value = current.value, compare.value
                current = compare
                compare = compare.next

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

# Test Cases
# TODO: make a DataStructureTest Interface if applicable, so the test running logic is reusable
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
            # TODO: move out of here vvv
            ["test_max_value", test_max_value],
            ["test_reverse", self.test_reverse],
            ["test_median_node", self.test_median_node],
            ["test_reverse", self.test_reverse],
            ["test_kth_node_from_tail", self.test_kth_node_from_tail],
            ["test_reverse_between", self.test_reverse_between],
            ["test_partition_list", self.test_partition_list],
            ["test_remove_duplicates", self.test_remove_duplicates],
            ["test_bubble_sort", self.test_bubble_sort],
        ]

    def run_all_tests(self):
        for test in self.test_configs:
            test_result = format_test_result(test[1]())
            print(f"{test[0]}: {test_result}")

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

    def test_kth_node_from_tail(self):
        ll = self.initialize_test_linked_list(num_of_values=5)
        return (
            ll.kth_node_from_tail(2).value == 4
            and ll.kth_node_from_tail(1).value == 5
            and ll.kth_node_from_tail(5).value == 1
            and ll.kth_node_from_tail(0) == None
            and ll.kth_node_from_tail(6) == None
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
        return ll.values() == [1, 2, 2, 3, 4, 5, 6]

class HashTableTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
        ]

    def run_all_tests(self):
        for test in self.test_configs:
            test_result = format_test_result(test[1]())
            print(f"{test[0]}: {test_result}")

    def initialize_test_hash_table(self):
        ht = HashTable()
        return ht

    def test_constructor(self):
        ht = self.initialize_test_hash_table()
        return len(ht.data_map) == 7

# Array Tests
def test_max_value():
    array = [1, 7, 6, 3, 4, 5, 2, 6]
    return max_value(array) == 7

# Test Execution
linked_list_test = LinkedListTest()
hash_table_test = HashTableTest()

print("Linked List Tests")
linked_list_test.run_all_tests()

print("Hash Table Tests")
hash_table_test.run_all_tests()
