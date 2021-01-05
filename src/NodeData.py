from src.GeoLocation import GeoLocation

class NodeData:

    def __init__(self, k,x=0,y=0,z=0):
        self.key=k
        self.tag=-1
        self.info='x'
        self.g=GeoLocation(x, y, z)

    def getKey(self) -> int:
        return self.key

    def getLocation(self) -> GeoLocation:
        return self.g

    def setLocation(self, l:GeoLocation) -> None:
        if l is not None:
            self.g=GeoLocation(l)

    def getInfo(self) ->str:
        return self.info

    def setInfo(self, i:str) ->None:
        self.info=i

    def setTag(self,t:int) ->None:
         self.tag=t

    def getTag(self) ->int:
        return self.tag
