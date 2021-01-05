from src.EdgeData import EdgeData
class EdgeList:


#this is used for all in/out neighbor

    def __init__(self):
        self.nodeNi={}

    def addNi(self, key:int, w:float) ->None:
        if e is not None:
            self.nodeNi[key]= w

    def getWeight(self, k:int)->float:
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


