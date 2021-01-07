from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        ga=GraphAlgo()
        ga.load_from_json("test1")
        print(ga.get_graph().v_size())
        print(ga.get_graph().e_size())


    def test_save_to_json(self):
        g= self.GraphCreator(20)
        g.add_edge(0,1,4.5)
        ga=GraphAlgo(g)

        ga.save_to_json("test1")

    def test_shortest_path(self):
        g=DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0,1,5)
        ga=GraphAlgo(g)
        print(ga.shortest_path(0,1))

    def test_dijkstra(self):
        self.fail()

    def test_rereverse_graphver(self):
        self.fail()

    def test_clear_graph(self):
        self.fail()

    def test_connected_component(self):
        self.fail()

    def test_connected_components(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()

    def GraphCreator(self, n: int) -> DiGraph:
        g = DiGraph()
        for i in range(0, n):
            g.add_node(i, (i, i + i / 2, i ** 3 + i - 10 * i))
        return g