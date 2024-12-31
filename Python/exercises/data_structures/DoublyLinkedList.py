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
        
        current = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
        self.length -= 1
        return current
    
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
            current.prev.next = current.next
            current.next.prev = current.prev
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