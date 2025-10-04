from exercises.data_structures.LinkedList import *

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        temp = self.first
        if temp.next:
            self.first = temp.next
        else:
            self.first = None
            self.last = None
        self.length -= 1
        return temp
