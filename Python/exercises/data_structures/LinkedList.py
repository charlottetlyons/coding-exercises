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

        if temp.next:
            self.head = temp.next
            temp.next = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return temp

    def pop(self):
        temp = self.head

        while temp.next:
            prev = temp
            temp = temp.next
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev.next = None
            self.tail = prev
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
            fast = fast.next.next
            slow = slow.next
        return slow

    def kth_node_from_end(self, k):
        fast = slow = self.head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        return slow

    def reverse_between(self, m, n):
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
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head

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
        seen = []
        before = None
        current = self.head

        while current:
            if current.value in seen:
                before.next = current.next
                self.length -= 1
            else:
                seen.append(current.value)
                before = current
            current = current.next

    def bubble_sort(self):
        is_sorted = False

        while not is_sorted:
            is_sorted = True
            current = self.head
            compare = current.next

            while compare:
                if current.value > compare.value:
                    current.value, compare.value = compare.value, current.value
                    is_sorted = False
                current = compare
                compare = compare.next
