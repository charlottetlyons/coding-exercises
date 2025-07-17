from exercises.data_structures.Graph import *
from ..utils.test_utils import *

class GraphTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_graph(self):
        g = Graph()
        return g

    def test_constructor(self):
        return self.initialize_test_graph().adj_list == {}
    
    # TODO
    def test_add_vertex(self):
        return True

    # TODO
    def test_add_edge(self):
        return True

    # TODO
    def test_remove_vertex(self):
        return True

    # TODO
    def test_remove_edge(self):
        return True
