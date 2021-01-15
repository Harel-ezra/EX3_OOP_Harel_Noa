Read ME - assignment number 3 OOP

NodeData
This class represents a node in a graph. Each node has a unique key.
Parameters:
key - unique key of a node
tag - will be used in algorithms on a graph
info - will be used in algorithms on a graph
pos - location of the node

Methods:

def __init__(self, k:int,gl=None): init a new node
def __repr__(self): Creates a string that represents a node
def __str__(self): Creates a string that represents a node
@Return string
def getKey(self): Return the key of a given node
@Return int
def getLocation(self):  Return the location of a node
@ Return a tuple of location
def setLocation(self, l:tuple): Allows changing the location of a node
def getInfo(self): Return info of a node
@Return string
def setInfo(self, i:str): Allows changing the info of a node
def setTag(self,t:int): Allows changing the info of a node
def getTag(self): Return tag of a node
@Return int
def comper(self, n:object): Comperes between two nodes
@Return true iff the nodes are similar 



DiGraph

This class represents a graph.

Parameters:

graph - a graph
neighborsSrc - all the nodes that this node is their src
neighborsDest -  all the nodes that this node is their dest
edgeSize - number of edges in the graph
MC - counts changes in the graph


Methods:

def __repr__(self): Creates a string that represents a graph
def __str__(self): Creates a string that represents a graph
@Return string
def __copy__(self): Return a copy of this graph 
@Return GraphInterface
def v_size(self): Return the number of vertices in this graph
@Return int
def e_size(self): Return the number of edges in this graph
@Return int
def get_all_v(self): Return a dictionary of all the nodes in the Graph, 
each node is represented by a pair (node_id, node_data)
@Return dictionary
def all_in_edges_of_node(self, id1: int): Return a dictionary of all the nodes connected to a given node_id , each node is represented using a pair (other_node_id, weight)
@Return dictionary
def all_out_edges_of_node(self, id1: int): return a dictionary of all the nodes connected from node_id , each node is represented by a pair (other_node_id, weight)
@Return dictionary
def get_mc(self): Returns the current version of this graph, on every change in the graph state the MC increases
@Return the current version of this graph
def add_edge(self, id1: int, id2: int, weight: float): Adds an edge to this graph
@Return true iff the edge was successfully added
def add_node(self, node_id: int, pos: tuple = None): Adds a node to this graph
@Return true iff the node was successfully added
def remove_node(self, node_id: int) : Removes a node to this graph
@Return true iff the edge was successfully removed
def remove_edge(self, node_id1: int, node_id2: int): Removes an edge to this graph
@Return true iff the edge was successfully removed
def comper(self, g:GraphInterface): Comperes between two graphs 
@Return true if they are similar


GraphAlgo

This class represents algorithms done on a graph.

Parameters:

graphAlgo – The graph we use for the algorithms





Methods:

def __init__(self, g=DiGraph()): init a new graph
def get_graph(self): Return the directed graph which the algorithms works on
@Return GraphInterface
def load_from_json(self, file_name: str) : Loads a graph from json file
@Return true iff loading was successfull
def save_to_json(self, file_name: str) : Save graph in JSON format to a file
@Return true iff saving was successfull
def shortest_path(self, id1: int, id2: int) :Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
@Return the distance of the path, a list of the nodes ids that the path goes through
def Dijkstra(self, src: int, graph: GraphInterface): For a given source node in the graph, the algorithm finds the shortest path between that node and every other
@Return dictionary
def rereverseGraph(self, g: DiGraph):Reverses the edges of this graph and returns the new graph
@Return GraphInterface
def clearGraph(self):Clears a graph to his default set up

The next methods check connected components

Parameters:

time - the starting and ending time of every node
lastTime - list of tuple for the last time every node is found, sorted by the ending time

Methods:

def dfs(self, node : NodeData): Algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node 
and explores as far as possible along each branch. algorithm is used to find connected components
@Returns list
def connected_component(self, id1: int): Finds the Strongly Connected Component(SCC) that  the node id1 takes part of.
@Return The list of nodes in the SCC
If the graph is None or id1 is not in the graph, the function returns an empty list []
def connected_components(self):  Finds all the Strongly Connected Component(SCC) in the graph 
@Return The list of all SCC
If the graph is None the function returns an empty list
def plot_graph(self): Plots the graph. If the nodes have a position, the nodes will be placed there. Otherwise, they will be placed in a random but elegant manner.

