from unittest import TestCase
from src.DiGraph import DiGraph
import random as random
random.seed(1)

class TestDiGraph(TestCase):

    def test_v_size(self):
        self.fail()

    def test_e_size(self):
        self.fail()

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
        g= self.GraphCreator(20)
        assert g.get_mc() ==20
        g.a

    def test_add_edge(self):
        g= self.GraphCreator(20)
        assert 20 ==g.v_size()
        g.add_edge(0,1,5)
        assert g.all_in_edges_of_node(1).get(0) == 5
        g.add_edge(0,1,2)
        assert g.all_in_edges_of_node(1).get(0) == 5
        g.add_edge(0,2,2)
        g.add_edge(0, 3, 7)
        g.add_edge(1, 2, 4.23)
        assert False ==g.add_edge(1,4,-15)



    def test_add_node(self):
        g=DiGraph()
        assert True == g.add_node(0,(0,0,1))
        assert False == g.add_node(0,(0,0,1))
        assert True == g.add_node(1,(-2,0,1))
        assert True == g.add_node(2)
        assert 0 == g.get_all_v().get(0).getKey()
        assert 1 == g.get_all_v().get(1).getKey()
        assert 2 == g.get_all_v().get(2).getKey()
        assert (0,0,1) == g.get_all_v().get(0).getLocation()
        assert (-2,0,1) == g.get_all_v().get(1).getLocation()
        assert None == g.get_all_v().get(2).getLocation()
        assert 3 == g.v_size()
        g= self.GraphCreator(20)
        assert 20 ==g.v_size()
        print(g.get_all_v())

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()

    def GraphCreator(self, n:int)->DiGraph:
        g = DiGraph()
        for i in range(0,n):
            g.add_node(i, (i,i+i/2, i**3+i-10))
        return g

    def GraphCreator1(self, n:int, e:int)->DiGraph:
        g = DiGraph()
        for i in range(0,n):
            g.add_node(i, (i,i+i/2, i**3+i-10*i))
        for i in range(0,e):
            k=random.random()
            j=random.random()
            g.add_edge(k,j,k/(j+1) )
        return g