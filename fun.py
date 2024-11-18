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
            self.tail = None
            self.head = None
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
            prev.next = None
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
        temp = self.head
        if temp:
            print(temp.value)
            temp = temp.next
    
    def get(self, index):
        if index < 0 or index > self.length-1:
            return False
        
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
        if index < 0 or index > self.length - 1:
            return None
        elif index == 0:
            return self.prepend()
        elif index == self.length:
            return self.append()
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
        else:
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

# Test Cases
def test_linked_list():
    test_linked_list_constructor()
    test_linked_list_pop_first()
    test_linked_list_pop()
    test_linked_list_prepend()
    test_linked_list_append()
    test_linked_list_print()
    test_linked_list_get()
    test_linked_list_set()
    test_linked_list_insert()
    test_linked_list_remove()

# Linked List Tests
def test_linked_list_constructor():
    ll = LinkedList(1)
    print(f'test_linked_list: {ll.get(0).value == 1}')

def test_linked_list_pop_first():
    return

def test_linked_list_pop():
    return

def test_linked_list_prepend():
    return

def test_linked_list_append():
    return

def test_linked_list_print():
    return

def test_linked_list_get():
    return

def test_linked_list_set():
    return

def test_linked_list_insert():
    return

def test_linked_list_remove():
    return


# Test Execution
test_linked_list()