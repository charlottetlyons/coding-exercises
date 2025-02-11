class DLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = DLLNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = DLLNode(value)

        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = DLLNode(value)

        if self.length == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

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

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None

        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
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
        new_node = DLLNode(value)
        prev = self.get(index - 1)
        next = prev.next
        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def values(self):
        values = []
        temp = self.head

        while temp:
            values.append(temp.value)
            temp = temp.next
        return values

    def swap_head_tail(self):
        if self.head is not self.tail:
            self.head.value, self.tail.value = self.tail.value, self.head.value
            return True
        return False

    def reverse(self):
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

    def is_palindrome(self):
        if self.length <= 1:
            return True

        front = self.head
        back = self.tail

        for _ in range(self.length//2):
            if front.value is not back.value:
                return False
            front = front.next
            back = back.prev
        return True

    def swap_pairs(self):
        temp = self.head
        while temp and temp.next:
            temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next.next

    def swap_head_tail(self):
        if self.head is not self.tail:
            self.head.value, self.tail.value = self.tail.value, self.head.value
            return True
        return False