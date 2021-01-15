
class NodeData:

    """
    Create  a new node data
    """
    def __init__(self, k:int,gl=None):
        self.key=k
        self.tag=-1
        self.info='x'
        self.pos=gl
    """
    Repr and str function is to create a string that represents a node data
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
    return the key a node data
    @return: node data key
    """
    def getKey(self) -> int:
        return self.key

    """
    return location of the node
    @return: tuple of node location
    """
    def getLocation(self) -> tuple:
        return self.pos

    """
    set location of a node
    @param: tuple that present a location
    """
    def setLocation(self, l:tuple) -> None:
        if l is not None:
            self.pos=l

            """
               return info of the node
            
               """

    def getInfo(self) ->str:
        return self.info


    """
    Allows changing the info of a node
    @param: string of the new info

    """

    def setInfo(self, i:str) ->None:
        self.info=i

    """
       Allows changing the tag of a node
       @param: int of the new tag

       """

    def setTag(self,t:int) ->None:
         self.tag=t


    """
              return tag of the node
              """

    def getTag(self) ->int:
        return self.tag

    """
        compere between 2 nodes
        """
    def comper(self, n:object)-> bool:
        if self.__class__ ==n.__class__:
            if self.key ==n.getKey() and self.pos==n.getLocation():
                return True
        return False

    """
    
    """

    def getStart(self):
      return self.start_of_edge






