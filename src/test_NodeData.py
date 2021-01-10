from unittest import TestCase

from src.NodeData import NodeData


class TestNodeData(TestCase):
    def test_get_key(self):
        n1=NodeData(0,(1,2,3))
        n2=NodeData(1)
        assert 0 == n1.getKey(), "n1 key is 0"
        assert 1 == n2.getKey(), "n2 key is 1"
        assert n1.__str__() == "{key: 0, pos: (1, 2, 3)}"


    def test_get_location(self):
        n1=NodeData(0,(1,2,3))
        n2=NodeData(1)
        assert (1,2,3) == n1.getLocation()
        assert None == n2.getLocation()

    def test_set_location(self):
        n1=NodeData(0,(1,2,3))
        assert (1,2,3) == n1.getLocation()
        n1.setLocation((4,2,4))
        assert (4,2,4) == n1.getLocation()
        n1.setLocation(None)
        assert (4,2,4) == n1.getLocation()


    def test_get_info(self):
        n1=NodeData(0,(1,2,3))
        n1.setInfo("v")
        assert "v"==n1.getInfo()

    def test_set_info(self):
        n1 = NodeData(0, (1, 2, 3))
        n1.setInfo("v")
        assert "v" == n1.getInfo()

    def test_set_tag(self):
        n1 = NodeData(0, (1, 2, 3))
        n1.setTag(5)
        assert 5 == n1.getTag()
    def test_get_tag(self):
        n1 = NodeData(0, (1, 2, 3))
        n1.setTag(5)
        assert 5 == n1.getTag()

