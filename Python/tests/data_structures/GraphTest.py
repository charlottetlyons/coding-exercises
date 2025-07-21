from exercises.data_structures.Graph import *
from ..utils.test_utils import *

class GraphTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_add_vertex", self.test_add_vertex],
            ["test_add_edge", self.test_add_edge],
            ["test_add_vertex", self.test_remove_vertex],
            ["test_add_edge", self.test_remove_edge]
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
        g = self.initialize_test_graph()
        emptyResult = g.add_vertex(1)
        errorResult = g.add_vertex(1)
        return len(g.adj_list[1]) == 0 and emptyResult == True and errorResult == False

    # TODO
    def test_add_edge(self):
        g = self.initialize_test_graph()
        g.add_vertex(1)
        g.add_vertex(2)
        emptyResult = g.add_edge(1, 2)
        errorResult = g.add_edge(1, 3)
        return len(g.adj_list[1]) == 1 and len(g.adj_list[2]) == 1 and emptyResult == True and errorResult == False


    # TODO
    def test_remove_vertex(self):
        g = self.initialize_test_graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_edge(1, 2)
        g.remove_vertex(1)
        result1 = len(g.adj_list) == 1
        result2 = len(g.adj_list[2]) == 0
        return result1 and result2

    # TODO
    def test_remove_edge(self):
        g = self.initialize_test_graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_edge(1, 2)
        g.remove_edge(1, 2)
        result1 = len(g.adj_list[1]) == 0
        result2 = len(g.adj_list[2]) == 0
        return result1 and result2
