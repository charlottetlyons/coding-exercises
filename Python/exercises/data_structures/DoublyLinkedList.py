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
        
        current = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            current.next = None
        self.length -= 1
        return current

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

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = DLLNode(value)
        prev = self.get(index-1)
        next = prev.next
        new_node.prev = prev
        new_node.next = next
        next.prev = new_node
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        current = self.get(index)
        current.next.prev = current.prev
        current.prev.next = current.next
        current.prev = None
        current.next = None
        self.length -= 1
        return current
    
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
            temp.next, temp.prev = temp.prev, temp.next
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
    
    def swap_values(self):
        temp = self.head
        while temp.next:
            temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next.next