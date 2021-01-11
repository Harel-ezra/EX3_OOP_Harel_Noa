
class NodeData:

    """
    create  a new node data
    """
    def __init__(self, k:int,gl=None):
        self.key=k
        self.tag=-1
        self.info='x'
        self.pos=gl
    """
    both, repr and str function is for create a string that presenting node data
    """
    def __repr__(self):
        return self.__str__()

    def __str__(self) ->str:
        s="{key: " + (str)(self.key) +", " +"pos: " + (str)(self.pos) + "}"
        return s

    """
    need it???
    """
    def __copy__(self)->object:
        n=NodeData(self.key, self.pos)
        n.setInfo(self.getInfo())
        n.setTag(self.getTag())
        return n

    """
    return a key of the node data
    @return: node data key
    """
    def getKey(self) -> int:
        return self.key

    """
    return a location of the node
    @return: tuple of node location
    """
    def getLocation(self) -> tuple:
        return self.pos

    """
    set the location for the node
    @param: tuple that present a location
    """
    def setLocation(self, l:tuple) -> None:
        if l is not None:
            self.pos=l

    def getInfo(self) ->str:
        return self.info

    def setInfo(self, i:str) ->None:
        self.info=i

    def setTag(self,t:int) ->None:
         self.tag=t

    def getTag(self) ->int:
        return self.tag

    """
        compere between 2 node
        """
    def comper(self, n:object)-> bool:
        if self.__class__ ==n.__class__:
            if self.key ==n.getKey() and self.pos==n.getLocation():
                return True
        return False



