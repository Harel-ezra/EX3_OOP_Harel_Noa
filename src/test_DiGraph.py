from unittest import TestCase
from src.DiGraph import DiGraph
import random as random
random.seed(1)

class TestDiGraph(TestCase):


    def test_v_size(self):
        g=TestDiGraph.GraphCreator1(self,20,20)
        assert 20==g.v_size()
        assert False == g.add_node(8)
        assert 20 == g.v_size()
        g.add_node(100)
        assert 21==g.v_size()
        g.remove_node(25)
        assert 21 == g.v_size()
        g.remove_node(2)
        assert 20 == g.v_size()

    def test_e_size(self):
        g=self.GraphCreator1(20,20)
        e=20
        assert e == g.e_size()
        if g.add_edge(0,7,4):
            e+=1
            assert e == g.e_size()
        else:
            assert e == g.e_size()
        if g.add_edge(0,1,0.5):
            e+=1
            assert e == g.e_size()
        else:
            assert e == g.e_size()



    def test_get_all_v(self):
        g=self.GraphCreator(20)

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        g= self.GraphCreator(20)
        for i in range(0,10):
            g.add_edge(0,i,i/2)
        assert 7 in g.all_out_edges_of_node(0)
        assert 11 not in g.all_out_edges_of_node(0)
        assert g.all_out_edges_of_node(0).get(7) ==3.5

    def test_get_mc(self):
        g= self.GraphCreator(20)
        assert g.get_mc() ==20


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
        assert False == g.add_edge(1,2,2)

        g=self.GraphCreator1(20,20)
        e=20
        if g.add_edge(4,5, 15):
            e+=1
            assert g.e_size() == e
            g.all_out_edges_of_node(4).get(5) ==15
            g.all_in_edges_of_node(5).get(4)==15
            print("done")
        if g.add_edge(4, 6, 9.5):
            e += 1
            assert g.e_size() == e
            assert g.all_out_edges_of_node(4).get(6) == 9.5
            g.all_in_edges_of_node(6).get(4)==9.5
            print("done")

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
        g.add_node(18)
        assert 20 ==g.v_size()
        g.add_node(22)
        assert 21 ==g.v_size()
        assert 22 == g.get_all_v().get(22).getKey()


    def test_remove_node(self):
        g=self.GraphCreator(20)
        assert g.remove_node(0) ==True
        g.add_node(0)
        for i in range (0,15):
            g.add_edge(0,i,i/7)
        assert g.e_size() == 14
        g.remove_node(0)
        assert g.e_size() ==0
        assert False == g.remove_node(0)
        assert False == g.add_edge(0,7,1)
        for i in range (0,15):
            g.add_edge(1,i,i/6)
        assert g.e_size() == 13
        g.remove_node(8)
        assert g.all_out_edges_of_node(1).get(8) == None
        assert g.e_size() == 12


    def test_remove_edge(self):
        g=self.GraphCreator(20)
        for i in range (0,20):
            g.add_edge(i,i+1,(i/3))
        assert g.e_size()==19
        assert g.all_in_edges_of_node(7).get(6) ==2
        assert g.remove_edge(6,7) ==True
        assert g.all_out_edges_of_node(6).get(7) == None
        assert g.remove_edge(6,7) ==False
        assert g.all_in_edges_of_node(7).get(6) ==None
        assert g.e_size()==18

    def GraphCreator(self, n:int)->DiGraph:
        g = DiGraph()
        for i in range(0,n):
            g.add_node(i, (i,i+i/2, i**3+i-10))
        return g

    def GraphCreator1(self, n:int, e:int)->DiGraph:
        g = DiGraph()
        for i in range(0,n):
            g.add_node(i, (i,i+i/2, i**3+i-10*i))
            i=0
        while i<e:
            k=random.randrange(0,n)
            j=random.randrange(0,n)
            if g.add_edge(k,j,k/(j+1)):
                i+=1
        return g