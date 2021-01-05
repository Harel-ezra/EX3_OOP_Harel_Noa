import math as math

class GeoLocation():

    def __init__(self, x:int, y:int, z:int):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self) ->str:
        string = self.x + "," + self.y + "," + self.z
        return string

    def x(self) ->int:
        return self.x

    def y(self) ->int:
        return self.y

    def z(self) ->int:
        return self.z

    def distance(self, g:GeoLocation) ->float:
        if g is not None:
            d=math.pow(self.x-g.x(),2)+(self.y-g.y(),2)+(self.z-g.z(),2)
            return math.sqrt(d)
        return -1