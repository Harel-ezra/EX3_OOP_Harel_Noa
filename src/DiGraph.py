from src.GraphInterface import GraphInterface
import EdgeList as EdgeList
from src.NodeData import NodeData


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
           return self.neighborsSrc.get(id1)
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.graph:
           return self.neighborsDest.get(id1)
        return {}

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.graph and id2 in self.graph and weight>=0:
            if id2 not in self.neighborsSrc.get(id1):
                self.neighborsSrc.get(id1)[id2]=weight
                self.neighborsDest.get(id2)[id1]=weight
                self.edgeSize+=1
                self.MC+=1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.graph and node_id >=0:
            n=NodeData(node_id,pos)
            self.graph[node_id]=n
            self.neighborsSrc[node_id]={}
            self.neighborsDest[node_id]= {}
            self.MC+=1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.graph:
            for key in self.neighborsDest:
                if node_id in self.neighborsDest.get(key):
                    self.neighborsDest.get(key).pop(node_id)
                    self.edgeSize-=1
                    self.MC+=1
            for key in self.neighborsSrc.get(node_id):
                self.neighborsDest.get(key).pop(node_id)
                self.edgeSize -= 1
                self.MC += 1
            self.neighborsSrc.pop(node_id)
            self.graph.pop(node_id)
            self.MC=+1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.graph and node_id2 in self.graph:
            if node_id2 in self.neighborsSrc.get(node_id1):
                    self.neighborsSrc.get(node_id1).pop(node_id2)
                    self.neighborsDest.get(node_id2).pop(node_id1)
                    self.edgeSize-=1
                    self.MC+=1
                    return True
        return False


