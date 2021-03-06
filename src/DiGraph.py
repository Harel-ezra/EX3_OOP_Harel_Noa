from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):

    """
        Init a new graph
        """
    def __init__(self):
        self.graph={}
        self.neighborsSrc={}
        self.neighborsDest={}  # all the nodes that this node is their dest
        self.edgeSize=0
        self.MC=0
    """
        Creats a string
        """
    def __repr__(self):
        return self.__str__()

    def __str__(self)->str:
        s="{Node:"
        for n in self.graph.values():
            s+=n.__str__()
            s+=" "
        s+="}"
        s+=" {Edge:"
        for n in self.neighborsSrc: # n is a key of node id
            for e in self.neighborsSrc.get(n).items(): # e is a tuple of (other node id, w)
                se="{src:"+(str)(n)+ ", dest:"+(str)(e[0])+", w:"+(str)(e[1])
                s+=se
        s+="}"
        return s
    """
    Return a copy of this graph
    """
    def __copy__(self)->GraphInterface:
        g=DiGraph()
        g.graph=self.graph.copy()
        g.neighborsSrc=self.neighborsSrc.copy()
        g.neighborsDest=self.neighborsDest.copy()
        g.edgeSize=self.e_size()
        g.mc=self.MC
        return g

    """
            Returns the number of vertices in this graph
            @return: The number of vertices in this graph
            """
    def v_size(self) -> int:
        return len(self.graph)

    """
            Returns the number of edges in this graph
            @return: The number of edges in this graph
            """

    def e_size(self) -> int:
        return self.edgeSize

    """return a dictionary of all the nodes in the Graph, 
    each node is represented using a pair (node_id, node_data)
            """
    def get_all_v(self) -> dict:
        return self.graph

    """return a dictionary of all the nodes connected to (into) node_id ,
            each node is represented using a pair (other_node_id, weight)
             """
    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.graph:
           return self.neighborsDest.get(id1)
        return {}

    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
            (other_node_id, weight)
            """
    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.graph:
           return self.neighborsSrc.get(id1)
        return {}

    """
           Returns the current version of this graph,
           on every change in the graph state the MC increases
           @return: The current version of this graph.
           """
    def get_mc(self) -> int:
        return self.MC

    """
            Adds an edge to the graph.
            @param id1: The start node of the edge
            @param id2: The end node of the edge
            @param weight: The weight of the edge
            @return: True if the edge was added successfully, False o.w.

            Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
            """
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.graph and id2 in self.graph and id1!= id2 and weight>=0:
            if id2 not in self.neighborsSrc.get(id1):
                self.neighborsSrc.get(id1)[id2]=weight
                self.neighborsDest.get(id2)[id1]=weight
                self.edgeSize+=1
                self.MC+=1
                return True
        return False

    """
            Adds a node to the graph.
            @param node_id: The node ID
            @param pos: The position of the node
            @return: True if the node was added successfully, False o.w.

            Note: if the node id already exists the node will not be added
            """
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.graph and node_id >=0:
            n=NodeData(node_id,pos)
            self.graph[node_id]=n
            self.neighborsSrc[node_id]={}
            self.neighborsDest[node_id]= {}
            self.MC+=1
            return True
        return False

    """
            Removes a node from the graph.
            @param node_id: The node ID
            @return: True if the node was removed successfully, False o.w.
            Note: if the node id does not exists the function will do nothing
            """
    def remove_node(self, node_id: int) -> bool:
        if node_id in self.graph:
            for key in self.neighborsDest.get(node_id):
               # if node_id in self.neighborsDest.get(key):
                    self.neighborsSrc.get(key).pop(node_id)
                    self.edgeSize-=1
                    self.MC+=1
            for key in self.neighborsSrc.get(node_id):
               # if node_id in self.neighborsSrc.get(key):
                    self.neighborsDest.get(key).pop(node_id)
                    self.edgeSize -= 1
                    self.MC += 1
            self.neighborsSrc.pop(node_id)
            self.neighborsDest.pop(node_id)
            self.graph.pop(node_id)
            self.MC=+1
            return True
        return False

    """
            Removes an edge from the graph.
            @param node_id1: The start node of the edge
            @param node_id2: The end node of the edge
            @return: True if the edge was removed successfully, False o.w.

            Note: If such an edge does not exists the function will do nothing
            """
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.graph and node_id2 in self.graph:
            if node_id2 in self.neighborsSrc.get(node_id1):
                    self.neighborsSrc.get(node_id1).pop(node_id2)
                    self.neighborsDest.get(node_id2).pop(node_id1)
                    self.edgeSize-=1
                    self.MC+=1
                    return True
        return False

    """
    compere between 2 graph
    """
    def comper(self, g:GraphInterface)->bool:
        if self.v_size()==g.v_size() and self.e_size() == g.e_size():
            for node in g.get_all_v().values():
                if node.getKey() not in self.graph:
                    return False
                else:
                    if not node.comper(self.graph.get(node.getKey())):
                        return False
                for e in g.all_in_edges_of_node(node.getKey()).items(): # e is tuple (other noe id, w)
                    if e[0] not in self.neighborsDest.get(node.getKey()):
                        return False
                    else:
                        if e[1] != self.neighborsDest.get(node.getKey()).get(e[0]):
                            return False
                for e in g.all_out_edges_of_node(node.getKey()).items(): # e is tuple (other noe id, w)
                    if e[0] not in self.neighborsSrc.get(node.getKey()):
                        return False
                    else:
                        if e[1] != self.neighborsSrc.get(node.getKey()).get(e[0]):
                            return False
            return True
        return False


