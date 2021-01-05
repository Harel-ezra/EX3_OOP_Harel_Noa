from src.EdgeData import EdgeData
class EdgeList:

"""
this is used for all in/out neigborh
"""
    def __init__(self):
        self.nodeNi={}

    def addNi(self, e:EdgeData) ->None:
        if e is not None:
            self.nodeNi[e.getDest().getKey()]= e.getWeight()

    def getWeight(self, k:int)->EdgeData:
        if self.hasEdge(k):
            return self.nodeNi.get(k)
        return None

    def hasEdge(self, k:int) -> bool:
        if k in self.nodeNi:
            return True
        return False

    def removeEdge(self, k:int) ->None:
        if self.hasEdge(k):
            self.nodeNi.pop(k)

    def getNiNode(self) -> dict:
        return self.nodeNi


