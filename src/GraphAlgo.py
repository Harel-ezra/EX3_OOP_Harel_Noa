from typing import List
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.NodeData import NodeData
import heapq as priorityQueue
import math as math
import json as json
import matplotlib.pyplot as plt
import random as random
random.seed(1)

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
                    self.graphAlgo=DiGraph()

                    for n in listNode: # n is a dict like this -{"pos": "0, 0.0, 0", "id": 0}
                        loactionStr=n.get("pos")
                        if loactionStr is not None:
                            l=loactionStr.split(",")
                            x = (float)(l[0])
                            y = (float)(l[1])
                            z = (float)(l[2])
                            tup = (x, y, z)
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
            print("can't read a graph from the file:"+file_name)

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

            for e in self.graphAlgo.all_out_edges_of_node(n.getKey()).items(): # e is a tuple (nehigbor node id, weight)
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
            self.clearGraph()
            if pathDict.get(id2) != None or id1 == id2:
                i = id2
                list.insert(0,id2)
                while i != id1:
                    list.insert(0, pathDict.get(i)[2])
                    i = pathDict.get(i)[2]
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
                for edge in graph.all_out_edges_of_node(node[1]).items():  # tuple of pair (neighbor node id, weight))
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
            for e in g.all_out_edges_of_node(n.getKey()).items():  # return tuple of pair (other node id, weight))
                gr.add_edge(e[0], n.getKey(), e[1])
        return gr

    def clearGraph(self):
        for node in self.graphAlgo.get_all_v().values():
            node.setInfo("x")
            node.setTag(-1)

    """
    the next method it for checking connected compennets
    """
    time=0 # for start time and end time for every node
    lastTime=[] # list of tuple for the last time every node is found, sorted by the time ending

    def dfs(self, node : NodeData) -> list:
        list=[node.getKey()]
        node.setInfo('w') # 'x' is not yes start, 'w' is processing, and 'v' is done
        self.time+=1 ## reize time of finding
        for e in self.graphAlgo.all_out_edges_of_node(node.getKey()).items(): # e id edge(other node id, weight)
            n=self.graphAlgo.get_all_v()[e[0]]
            if n.getInfo() =='x':
                list+=self.dfs(n)
        self.time+=1 ## reize time of finding
        self.lastTime.insert(len(self.lastTime), (self.time, node.getKey()))
        node.setInfo('v')
        return list

    def connected_component(self, id1: int) -> list:
        list=self.connected_components()
        for l in list:
            if id1 in l:
                return l

    def connected_components(self) -> List[list]:
        self.time=0
        self.lastTime=[]
        conectedList=[]
        if self.graphAlgo.v_size()==0:
            return conectedList
        for node in self.graphAlgo.get_all_v().values(): # is node data
            if node.getInfo()=='x': # mean not visited
                self.dfs(node)

        self.lastTime.sort()
        self.lastTime.reverse()
        tempG=self.graphAlgo
        self.graphAlgo=self.rereverseGraph(self.graphAlgo)
        self.time=0
        l=self.lastTime.copy()
        self.lastTime=[]
        compeList = []

        for key in l: # key is tuple time and key is node
            node=self.graphAlgo.get_all_v().get(key[1])
            if node.getInfo()=='x':
                #if len(compeList) > 0:
                 #   conectedList.insert(len(conectedList), compeList)
                #compeList=[]
                conectedList.insert(len(compeList),self.dfs(node))
            #else:
             #   compeList.insert(len(compeList), node.getKey())
        #conectedList.insert(len(conectedList), compeList)
        self.graphAlgo=tempG
        self.clearGraph()
        return conectedList


    def plot_graph(self) -> None:
        for node in self.graphAlgo.get_all_v().values():
            if node.getLocation() is None:
                plt.plot(random.randrange(0,100,1),random.randrange(0,100,1),'ro')
            else:
                g=node.getLocation()

                plt.plot(g[0],g[1], 'ro')

        plt.show()
 

