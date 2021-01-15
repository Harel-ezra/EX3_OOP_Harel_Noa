import heapq as priorityQueue
import json as json
import math as math
import random as random
from typing import List

import matplotlib.pyplot as plt

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.NodeData import NodeData



from encodings import undefined
from tokenize import Double
import numpy as np
import matplotlib.pyplot as plt
import json
from typing import List, Collection
from collections import deque
from src import GraphAlgoInterface, GraphInterface, DiGraph, NodeData
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from collections import defaultdict
from matplotlib.ticker import AutoLocator
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patches as mpatches
import matplotlib
import numpy as np
import math
from math import e
from math import pi
import copy

random.seed(1)


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=DiGraph()):
        self.graphAlgo = g

        """
             Return: the directed graph  which the algorithms works on
             """

    def get_graph(self) -> GraphInterface:
        return self.graphAlgo

    """
           Loads a graph from a json file.
           @param file_name: The path to the json file
           @returns True if the loading was successful, False o.w.
           """

    def load_from_json(self, file_name: str) -> bool:
        try:
            if file_name is not None:
                with open(file_name, 'r') as file:
                    dict = json.load(file)
                    listEdge = dict.get("Edges")
                    listNode = dict.get("Nodes")
                    self.graphAlgo = DiGraph()

                    for n in listNode:  # n is a dict like this -{"pos": "0, 0.0, 0", "id": 0}
                        loactionStr = n.get("pos")
                        if loactionStr is not None:
                            l = loactionStr.split(",")
                            x = (float)(l[0])
                            y = (float)(l[1])
                            z = (float)(l[2])
                            tup = (x, y, z)
                        else:
                            tup = None
                        key = n.get("id")
                        self.graphAlgo.add_node(key, tup)
                    for e in listEdge:  # e is a dict like this -{"src":0,"w":1.4004465106761335,"dest":1}
                        src = e.get("src")
                        dest = e.get("dest")
                        w = e.get("w")
                        self.graphAlgo.add_edge(src, dest, w)
                    return True
            return False
        except:
            print("can't read a graph from the file:" + file_name)

            """
                   Saves the graph in JSON format to a file
                   @param file_name: The path to the out file
                   @return: True if the save was successful, False o.w.
                   """

    def save_to_json(self, file_name: str) -> bool:
        dict = {}
        listEdge = []
        listNode = []
        for n in self.graphAlgo.get_all_v().values():  # n is NodeData
            if n.getLocation() is not None:
                s = "" + (str)(n.getLocation()[0]) + ", " + (str)(n.getLocation()[1]) + ", " + (str)(n.getLocation()[2])
                node = {"pos": s, "id": n.getKey()}
            else:
                node = {"id": n.getKey()}
            listNode.insert(len(listNode), node)

            for e in self.graphAlgo.all_out_edges_of_node(
                    n.getKey()).items():  # e is a tuple (nehigbor node id, weight)
                edge = {"src": n.getKey(), "w": e[1], "dest": e[0]}
                listEdge.insert(len(listEdge), edge)
        dict["Edges"] = listEdge
        dict["Nodes"] = listNode
        if file_name is not None:
            with open(file_name, 'w') as file:
                json.dump(dict, file)
                # json.dump(self.graphAlgo, file, default=lambda o: o.__dict__, indent=4)
                return True
        return False

    """
          Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
          @param id1: The start node id
          @param id2: The end node id
          @return: The distance of the path, a list of the nodes ids that the path goes through
          """

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list = []
        if id1 in self.graphAlgo.get_all_v() and id2 in self.graphAlgo.get_all_v():
            pathDict = self.Dijkstra(id1, self.graphAlgo)
            self.clearGraph()
            if pathDict.get(id2) != None or id1 == id2:
                i = id2
                list.insert(0, id2)
                while i != id1:
                    list.insert(0, pathDict.get(i)[2])
                    i = pathDict.get(i)[2]
                tup = (pathDict.get(id2)[0], list)
                return tup
        return (math.inf, list)

    """
          For a given source node in the graph, 
          the algorithm finds the shortest path between that node and every other
            """

    def Dijkstra(self, src: int, graph: GraphInterface) -> dict:
        # the tuple in dict is used to show whieght and fater kay (weight, sun key, fatter key)
        queue = []
        dict = {}
        dict[src] = (0, src, -1)
        priorityQueue.heappush(queue, (0, src, -1))

        while len(queue) != 0:
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

    """
             Reverses the edges of this graph and returns the new graph
             @Return GraphInterface
               """

    def rereverseGraph(self, g: DiGraph) -> GraphInterface:
        gr = DiGraph()
        for n in g.get_all_v().values():
            gr.add_node(n.getKey(), n.getLocation())
        for n in g.get_all_v().values():
            for e in g.all_out_edges_of_node(n.getKey()).items():  # return tuple of pair (other node id, weight))
                gr.add_edge(e[0], n.getKey(), e[1])
        return gr

    """
            Clears the graph to his default set up
            """

    def clearGraph(self):
        for node in self.graphAlgo.get_all_v().values():
            node.setInfo("x")
            node.setTag(-1)

    """
    The next methods check connected components
    """
    time = 0  # the starting and ending time of every node
    lastTime = []  # list of tuple for the last time every node is found, sorted by the ending time

    """
    Algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node 
    and explores as far as possible along each branch
    algorithm is used to find connected components
    @reurn : list
    """

    def dfs(self, node: NodeData) -> list:
        list = [node.getKey()]
        node.setInfo('w')  # 'x' is not yes start, 'w' is processing, and 'v' is done
        self.time += 1  ## reize time of finding
        for e in self.graphAlgo.all_out_edges_of_node(node.getKey()).items():  # e id edge(other node id, weight)
            n = self.graphAlgo.get_all_v()[e[0]]
            if n.getInfo() == 'x':
                list += self.dfs(n)
        self.time += 1  ## reize time of finding
        self.lastTime.insert(len(self.lastTime), (self.time, node.getKey()))
        node.setInfo('v')
        return list

    """
         Finds the Strongly Connected Component(SCC) that  the node id1 takes part of.
         @param id1: The node id
         @return: The list of nodes in the SCC

         If the graph is None or id1 is not in the graph, the function returns an empty list []
         """

    def connected_component(self, id1: int) -> list:
        list = self.connected_components()
        for l in list:
            if id1 in l:
                return l

            """
                  Finds all the Strongly Connected Component(SCC) in the graph.
                  @return: The list of all SCC
                  If the graph is None the function returns an empty list []
                  """

    def connected_components(self) -> List[list]:
        self.time = 0
        self.lastTime = []
        conectedList = []
        if self.graphAlgo.v_size() == 0:
            return conectedList
        for node in self.graphAlgo.get_all_v().values():  # is node data
            if node.getInfo() == 'x':  # mean not visited
                self.dfs(node)

        self.lastTime.sort()
        self.lastTime.reverse()
        tempG = self.graphAlgo
        self.graphAlgo = self.rereverseGraph(self.graphAlgo)
        self.time = 0
        l = self.lastTime.copy()
        self.lastTime = []
        compeList = []

        for key in l:  # key is tuple time and key is node
            node = self.graphAlgo.get_all_v().get(key[1])
            if node.getInfo() == 'x':
                conectedList.insert(len(compeList), self.dfs(node))
        self.graphAlgo = tempG
        self.clearGraph()
        return conectedList




    def get_node(self, node_id):
        try:
            return self.nodes[node_id]
        except:
            print("node does not exist")
            pass



    """
           Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
         @return: None
            """

    def plot_graph(self) -> None:
        # myGraph = self.graphAlgo

        x=[]
        y=[]
        z=[]

        ax = plt.gca()
        nodes = self.graphAlgo.get_all_v()
        for node in nodes.keys():
            if nodes.get(node).getLocation() is None:

                x1 = random.randrange(0, 100, 1)
                y1 = random.randrange(0, 100, 1)
                pos = (x1,y1)
                nodes.get(node).setLocation(pos)
            x.append(nodes.get(node).getLocation()[0])
            y.append(nodes.get(node).getLocation()[1])

        for key in nodes.keys():
            z.append(key)


        for index, txt in enumerate(z):
            ax.annotate(z[index], (nodes.get(z[index]).getLocation()[0], nodes.get(z[index]).getLocation()[1]), color='blue')
        for node in nodes.keys():
            arrowsO = self.graphAlgo.all_out_edges_of_node(node)
            for edge in arrowsO.keys():
                if len(arrowsO) != 0:
                    XO = nodes.get(edge).getLocation()[0]
                    YO = nodes.get(edge).getLocation()[1]
                    plt.annotate(text='', xy=(nodes.get(node).getLocation()[0], nodes.get(node).getLocation()[1]),
                                 xytext=(XO, YO),
                                 arrowprops=dict(arrowstyle="<|-"))

        plt.title("Graph")
        plt.plot(x,y,'bo')
        plt.show()



