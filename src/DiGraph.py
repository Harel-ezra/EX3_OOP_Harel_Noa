from src.GraphInterface import GraphInterface
import EdgeData as EdgeData

class DiGraph(GraphInterface):

    def __init__(self):
        self.graph={}
        self.neighborsSrc={}
        self.neighborsDest={}  # all is node that this node is there dest
        self.edgeSize=0
        self.MC=0

    def v_size(self) -> int:
        return len(self.graph)

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.graph:
           return self.neighborsSrc.pop(id1)
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.graph:
           return self.neighborsDest.pop(id1)
        return {}

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.graph and id2 in self.graph and weight>=0:
            e=EdgeData(id1, id2, weight)
            self.neighborsSrc[]=

            return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        pass

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass

