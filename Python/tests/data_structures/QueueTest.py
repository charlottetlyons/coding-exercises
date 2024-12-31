from exercises.data_structures.Queue import Queue
from ..utils.test_utils import *

class QueueTest:
    def __init__(self):
        self.test_configs = [["test_constructor", self.test_constructor]]
    
    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_queue(self):
        return Queue(0)

    def test_constructor(self):
        q = self.initialize_test_queue()
        return q.first.value == 0 and q.last.value == 0 and q.length == 1