#  TEST UTILITY FUNCTIONS
def format_test_result(result):
    return '\033[32mPass\033[0m' if result else '\033[31mFail\033[0m'

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
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
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
        for _ in range(n-m):
            after = current.next
            current.next = after.next
            after.next = prev.next
            prev.next = after
        self.head = dummy.next

    def partition_list(self, x):
        current = self.head
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = prev1.next
            else:
                prev2.next = current
                prev2 = prev2.next
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

# Test Cases
def run_all_tests():
    test_configs = [
        ["test_linked_list_constructor", test_linked_list_constructor],
        ["test_linked_list_pop_first", test_linked_list_pop_first],
        ["test_linked_list_pop", test_linked_list_pop],
        ["test_linked_list_prepend", test_linked_list_prepend],
        ["test_linked_list_append", test_linked_list_append],
        ["test_linked_list_print", test_linked_list_print],
        ["test_linked_list_get", test_linked_list_get],
        ["test_linked_list_set", test_linked_list_set],
        ["test_linked_list_insert", test_linked_list_insert],
        ["test_linked_list_remove", test_linked_list_remove],
        ["test_linked_list_get_length", test_linked_list_get_length],
        ["test_linked_list_functions_out_of_bounds", test_linked_list_functions_out_of_bounds],
        ["test_max_value", test_max_value],
        ["test_linked_list_reverse", test_linked_list_reverse],
        ["test_linked_list_median_node", test_linked_list_median_node],
        ["test_linked_list_reverse", test_linked_list_reverse],
        ["test_linked_list_kth_node_from_tail", test_linked_list_kth_node_from_tail],
        ["test_linked_list_reverse_between", test_linked_list_reverse_between],
        ["test_linked_list_partition_list", test_linked_list_partition_list],
        ["test_linked_list_remove_duplicates", test_linked_list_remove_duplicates]
    ]

    for test in test_configs:
        test_result = format_test_result(test[1]())
        print(f'{test[0]}: {test_result}')

# Linked List Tests
def initialize_test_linked_list(num_of_values=3, is_sorted=True, custom_list=None):
    ll = LinkedList(1)
    if custom_list:
        ll.pop_first()
        for value in custom_list:
            ll.append(value)
    else:
        if is_sorted:
            for value in range(2, num_of_values+1):
                ll.append(value)
        else:
            for value in range(num_of_values+1, 2):
                ll.append(value)
        
    return ll 

def test_linked_list_constructor():
    ll = LinkedList(1)
    return ll.get(0).value == 1 and ll.length == 1

def test_linked_list_pop_first():
    ll = initialize_test_linked_list()
    return ll.pop_first().value == 1 and ll.length == 2

def test_linked_list_pop():
    ll = initialize_test_linked_list()
    return ll.pop().value == 3 and ll.length == 2

def test_linked_list_prepend():
    ll = initialize_test_linked_list()
    ll.prepend(4)
    return ll.get(0).value == 4 and ll.length == 4

def test_linked_list_append():
    ll = initialize_test_linked_list()
    ll.append(4)
    return ll.get(3).value == 4 and ll.length == 4

# TODO: this seems annoying, do later
def test_linked_list_print():
    return True

def test_linked_list_get():
    ll = initialize_test_linked_list()
    return ll.get(1).value == 2

def test_linked_list_functions_out_of_bounds():
    ll = initialize_test_linked_list()
    pre_index = -1
    post_index = 4
    test_value = 5
    test_configs = [
        dict(
            test_name="test_linked_list_get_out_of_bounds", 
            linked_list_function=ll.get, 
            expected_result=None,
            needs_value=False
        ),
        dict(
            test_name="test_linked_list_set_out_of_bounds",
            linked_list_function=ll.set, 
            expected_result=False,
            needs_value=True
        ),
        dict(
            test_name="test_linked_list_insert_out_of_bounds",
            linked_list_function=ll.insert,
            expected_result=False,
            needs_value=True
        ),
        dict(
            test_name="test_linked_list_remove_out_of_bounds", 
            linked_list_function=ll.remove, 
            expected_result=None,
            needs_value=False    
        )
    ]

    for test in test_configs:
        if test["needs_value"]:
            test_result = test["linked_list_function"](pre_index, test_value) == test["expected_result"] and test["linked_list_function"](post_index, test_value) == test["expected_result"]
        else:
            test_result = test["linked_list_function"](pre_index) == test["expected_result"] and test["linked_list_function"](post_index) == test["expected_result"]
        print(f'{test["test_name"]}: {format_test_result(test_result)}')
        if not test_result:
            return False
    return True

def test_linked_list_set():
    ll = initialize_test_linked_list()
    ll.set(2, 5)
    return ll.get(2).value == 5

# TODO: Test first and last insertion cases
def test_linked_list_insert():
    ll = initialize_test_linked_list()
    ll.insert(1, 5)
    return ll.get(1).value == 5 and ll.length == 4

def test_linked_list_remove():
    ll = initialize_test_linked_list()
    return ll.remove(1).value == 2 and ll.length == 2

def test_linked_list_get_length():
    ll = initialize_test_linked_list()
    return ll.get_length() == 3

def test_linked_list_reverse():
    ll = LinkedList(7)
    for num in [3, 6, 2, 6, 1, 4]:
        ll.append(num)
    expected_order = [4, 1, 6, 2, 6, 3, 7]
    ll.reverse()
    return ll.values() == expected_order

def test_linked_list_sort():
    # TODO: needed later
    return

    # ll = LinkedList(7)
    # for num in [3, 6, 2, 6, 1, 4]:
    #     ll.append(num)
    # expected_order = [1, 2, 3, 4, 6, 6, 7]
    # ll.sort()
    # print(ll.values())
    # print(expected_order)
    # return ll.values() == expected_order

def test_linked_list_median_node():
    ll = initialize_test_linked_list()
    return ll.median_node().value == 2

def test_linked_list_kth_node_from_tail():
    ll = initialize_test_linked_list(num_of_values=5)
    return (
        ll.kth_node_from_tail(2).value == 4 
        and ll.kth_node_from_tail(1).value == 5 
        and ll.kth_node_from_tail(5).value == 1 
        and ll.kth_node_from_tail(0) == None 
        and ll.kth_node_from_tail(6) == None
    )

def test_linked_list_reverse_between():
    ll = initialize_test_linked_list(num_of_values=5)
    ll.reverse_between(1, 3)
    return ll.values() == [1,4,3,2,5] 

def test_linked_list_partition_list():
    ll = initialize_test_linked_list(custom_list=[1,3,2,3,1,14])
    ll.partition_list(3)
    return ll.values() == [1,2,1,3,3,14]
    
def test_linked_list_values():
    return initialize_test_linked_list().values() == [1, 2, 3, 4, 5]

def test_linked_list_remove_duplicates():
    ll = initialize_test_linked_list(custom_list=[1, 1, 2, 3, 3, 3])
    ll.remove_duplicates()
    return ll.values() == [1, 2, 3]

# Array Tests
def test_max_value():
    array = [1, 7, 6, 3, 4, 5, 2, 6]
    return max_value(array) == 7

# Test Execution
run_all_tests()