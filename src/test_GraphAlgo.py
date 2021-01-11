import math
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import matplotlib.pyplot as plt
from src.test_DiGraph import TestDiGraph
class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        g=DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0,1,2)
        ga=GraphAlgo(g)
        assert g.comper(ga.get_graph())

        g=TestDiGraph.graphCreator(self,20)
        ga=GraphAlgo(g)
        assert g.comper(ga.get_graph())

        g = TestDiGraph.graphCreator1(self, 20,50)
        ga = GraphAlgo(g)
        assert g.comper(ga.get_graph())

    def test_save_load_json(self):
        g=DiGraph()
        ga=GraphAlgo(g)
        ga.save_to_json("test1")
        ga.load_from_json("test1")
        assert ga.get_graph().comper(g)


        g= TestDiGraph.graphCreator(self,20)
        g.add_edge(0,1,4.5)
        ga=GraphAlgo(g)

        ga.save_to_json("test2")
        ga.load_from_json("test1")
        print(ga.get_graph().__str__())
        print(g.__str__())
        assert not g.comper(ga.get_graph())
        ga.load_from_json("test2")
        assert g.comper(ga.get_graph())

        g= TestDiGraph.graphCreator1(self,20,50)
        ga=GraphAlgo(g)
        ga.save_to_json("test3")
        ga.load_from_json("test3")
        assert g.comper(ga.get_graph())


    def test_shortest_path(self):
        g=DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0,1,5)
        ga=GraphAlgo(g)
        assert (5, [0, 1]) == ga.shortest_path(0,1)

        g=DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(0,1,1)
        g.add_edge(1,2,4)
        ga=GraphAlgo(g)
        assert ga.shortest_path(0,1) == (1, [0, 1])
        assert ga.shortest_path(0,2) == (5, [0, 1, 2])

        g=self.graphForTest()
        ga=GraphAlgo(g)
        assert ga.shortest_path(0,0) == (0, [0])
        assert ga.shortest_path(0,-1) == (math.inf, [])
        assert ga.shortest_path(0,5)[0]== 1
        ga.get_graph().remove_edge(0,5)
        assert ga.shortest_path(0, 5)[0] == 7.7
        assert ga.shortest_path(0, 5)[1] == [0,2,5]

        assert ga.shortest_path(0, 6)[0] == math.inf
        ga.get_graph().add_edge(7,6,0.5)
        assert ga.shortest_path(0, 6)[0] == 2.35

        assert ga.shortest_path(5, 4)[0] == 2
        assert ga.shortest_path(4, 5)[0] == math.inf

        assert ga.shortest_path(1, 4)[0] == 4.275
        assert ga.shortest_path(1, 4)[1] == [1,2,0,4]

        ga.get_graph().remove_edge(0,4)
        assert ga.shortest_path(1, 4)[0] == 5.825
        assert ga.shortest_path(1, 4)[1] == [1,2,5,4]
        ga.get_graph().remove_node(5)
        assert ga.shortest_path(1, 4)[0] == math.inf

        assert ga.shortest_path(2, 9)[0] == 1.05
        ga.get_graph().remove_edge(2,9)
        assert ga.shortest_path(2, 9)[0] == 3.16
        assert ga.shortest_path(9, 2)[1] == []

    def test_rereverse_graphver(self):
        g=TestDiGraph.graphCreator1(self,20,20)
        ga=GraphAlgo(g)
        g1=ga.rereverseGraph(g)
        ga1=GraphAlgo(g1)
        assert g.comper(ga1.rereverseGraph(g1))

    def test_connected_component(self):
        self.fail()

    def test_connected_components(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        assert []==ga.connected_components()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0,1,5)
        g.add_edge(1,0,5)
        ga=GraphAlgo(g)
        assert [[0, 1]]==ga.connected_components()
        g.add_node(2)
        g.add_edge(0,2,1)
        print(ga.connected_components())

        g=self.graphForTest1()
        ga=GraphAlgo(g)
        print(ga.connected_components())




    def test_plot_graph(self):
        plt.plot(1,1,"ro")
        plt.show()

    def graphForTest(self)->DiGraph:
            g = DiGraph()
            for i in range(0,10):
                g.add_node(i,(i-1,0.4*(1/(i+1)),5*math.sqrt(i)))
            g.add_edge(0, 5, 1)
            g.add_edge(0, 2, 4.7)
            g.add_edge(0, 4, 1.75)
            g.add_edge(4, 7, 0.1)
            g.add_edge(5, 4, 2)
            g.add_edge(1, 2, 0.825)
            g.add_edge(1, 7, 0.5)
            g.add_edge(2, 1, 7.05)
            g.add_edge(2, 5, 3)
            g.add_edge(5, 2, 4.05)
            g.add_edge(5, 8, 4.02)
            g.add_edge(2, 8, 2.08)
            g.add_edge(8, 9, 1.08)
            g.add_edge(2, 9, 1.05)
            g.add_edge(5, 7, 2.07)
            g.add_edge(2, 0, 1.7)
            return g

    def graphForTest1(self)->DiGraph:
        g=DiGraph()
        for i in range(0,10):
            g.add_node(i)
        g.add_edge(0,1,1)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 0, 1)
        g.add_edge(0, 3, 1)
        g.add_edge(4, 3, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 5, 1)
        g.add_edge(5, 6, 1)
        g.add_edge(6, 5, 1)
        g.add_edge(7, 6, 1)
        g.add_edge(7, 9, 1)
        g.add_edge(9, 8, 1)
        g.add_edge(8, 7, 1)
        return g



