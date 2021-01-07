from typing import List
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
import heapq as priorityQueue
import math as math
import json as json

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=DiGraph()):
        self.graphAlgo = g

    def get_graph(self) -> GraphInterface:
        return self.graphAlgo

    def load_from_json(self, file_name: str) -> bool:
        try:
            if file_name is not None:
                with open(file_name, 'r') as file:
                    dict=json.load(file)
                    listEdge=dict.get("Edges")
                    listNode=dict.get("Nodes")

                    for n in listNode: # n is a dict like this -{"pos": "0, 0.0, 0", "id": 0}
                        loactionStr=n.get("pos")
                        if loactionStr is not None:
                            l=loactionStr.split(",")
                            tup = (l[0], l[1], l[2])
                        else:
                            tup=None
                        key=n.get("id")
                        self.graphAlgo.add_node(key,tup)
                    for e in listEdge: # e is a dict like this -{"src":0,"w":1.4004465106761335,"dest":1}
                        src=e.get("src")
                        dest=e.get("dest")
                        w=e.get("w")
                        self.graphAlgo.add_edge(src, dest, w)
                    return True
            return False
        except:
            print("can't read a graph from the file")

    def save_to_json(self, file_name: str) -> bool:
        dict={}
        listEdge=[]
        listNode=[]
        for n in self.graphAlgo.get_all_v().values(): # n is NodeData
            if n.getLocation() is not None:
                s=""+(str)(n.getLocation()[0])+", "+(str)(n.getLocation()[1])+", "+(str)(n.getLocation()[2])
                node={"pos": s, "id":n.getKey()}
            else:
                node={"id":n.getKey()}
            listNode.insert(len(listNode), node)

            for e in self.graphAlgo.all_out_edges_of_node(n.getKey()).values(): # e is a tuple (nehigbor node id, weight)
                edge={"src":n.getKey(), "w": e[1], "dest":e[0]}
                listEdge.insert(len(listEdge), edge)
        dict["Edges"]=listEdge
        dict["Nodes"]=listNode
        if file_name is not None:
            with open(file_name, 'w') as file:
                json.dump(dict, file)
                #json.dump(self.graphAlgo, file, default=lambda o: o.__dict__, indent=4)
                return True
        return False


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list = []
        if id1 in self.graphAlgo.get_all_v() and id2 in self.graphAlgo.get_all_v():
            pathDict = self.Dijkstra(id1, self.graphAlgo)
            if pathDict.get(id2) != None or id1 == id2:
                i = id2
                list.insert(0,id2)
                while i != id1:
                    list.insert(0, pathDict.get(i)[2])
                    i = pathDict.get(i)[2]
                self.clearGraph()
                tup=(pathDict.get(id2)[0], list)
                return tup
        return (math.inf, list)

    def Dijkstra(self, src: int, graph: GraphInterface) -> dict:
        # the tuple in dict is used to show whieght and fater kay (weight, sun key, fatter key)
        queue = []
        dict = {}
        dict[src] = (0, src, -1)
        priorityQueue.heappush(queue, (0, src, -1))

        while len(queue)!=0:
            node = priorityQueue.heappop(queue)
            if graph.get_all_v().get(node[1]).getInfo() == "x":
                for edge in graph.all_out_edges_of_node(node[1]).values():  # tuple of pair (neighbor node id, weight))
                    if graph.get_all_v().get(edge[0]).getInfo() == "x":
                        weight = node[0] + edge[1]
                        if edge[0] not in dict or dict.get(edge[0])[0] > weight:
                            priorityQueue.heappush(queue, (weight, edge[0], node[1]))
                            dict[edge[0]] = (weight, edge[0], node[1])
                graph.get_all_v().get(node[1]).setInfo("v")
        return dict

        # need it..??
    def rereverseGraph(self, g: DiGraph) -> GraphInterface:
        gr = DiGraph()
        for n in g.get_all_v().values():
            gr.add_node(n.getKey(), n.getLocation())
        for n in g.get_all_v().values():
            for e in g.all_out_edges_of_node(n.getKey()).values():  # return tuple of pair (other node id, weight))
                gr.add_edge(e[0], n.getKey(), e[1])
        return gr

    def clearGraph(self):
        for node in self.graphAlgo.get_all_v().values():
            node.setInfo("x")
            node.setTag(-1)

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
