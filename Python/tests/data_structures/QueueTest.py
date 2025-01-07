from exercises.data_structures.Queue import Queue
from ..utils.test_utils import *

class QueueTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_enqueue", self.test_enqueue],
            ["test_dequeue", self.test_dequeue]
        ]
    
    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_queue(self):
        return Queue(0)

    def test_constructor(self):
        q = self.initialize_test_queue()
        return q.first.value == 0 and q.last.value == 0 and q.length == 1
    
    def test_enqueue(self):
        q = self.initialize_test_queue()
        q.enqueue(100)
        return q.last.value == 100 and q.length == 2
    
    def test_dequeue(self):
        q = self.initialize_test_queue()
        q.enqueue(1)
        result1 = q.dequeue()
        result2 = q.dequeue()
        return result1.value == 0 and result2.value == 1 and q.first == None and q.last == None and q.length == 0