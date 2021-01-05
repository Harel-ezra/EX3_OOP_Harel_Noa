from src.NodeData import NodeData

class EdgeData:

    def __init__(self, s:NodeData, d:NodeData, w:float):
        self.src=s
        self.dest=d
        self.weight=w
        self.info="x"
        self.tag=-1

    def getSrc(self) ->NodeData:
        return self.src

    def getDest(self) ->NodeData:
        return self.dest

    def getWeight(self) ->float:
        return self.weight

    def getInfo(self) ->str:
        return self.info

    def setInfo(self, s:str) -> None:
        self.info=s

    def getTag(self) -> int:
        return self.tag

    def setTag(self, t:int) -> None:
        self.tag=t

    #def __eq__(self, e):

