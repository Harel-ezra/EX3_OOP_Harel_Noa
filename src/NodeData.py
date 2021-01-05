
class NodeData:

    def __init__(self, k:int,gl=(0,0,0)):
        self.key=k
        self.tag=-1
        self.info='x'
        self.g=gl

    def getKey(self) -> int:
        return self.key

    def getLocation(self) -> tuple:
        return self.g

    def setLocation(self, l:tuple) -> None:
        if l is not None:
            self.g=l

    def getInfo(self) ->str:
        return self.info

    def setInfo(self, i:str) ->None:
        self.info=i

    def setTag(self,t:int) ->None:
         self.tag=t

    def getTag(self) ->int:
        return self.tag
