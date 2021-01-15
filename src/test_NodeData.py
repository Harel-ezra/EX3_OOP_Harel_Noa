from unittest import TestCase

from src.NodeData import NodeData


class TestNodeData(TestCase):
    """
               Tests on all methods in NodeData
                """

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

    def test_comper(self):
        node1=NodeData(0)
        node2=NodeData(0)
        assert node1.comper(node2)
        assert not node1.comper({123})
        node1.setLocation((0,1,2))
        assert not node1.comper(node2)
        node2.setLocation((0, 1, 2))
        assert node1.comper(node2)
        node2.setLocation((0, 1, 3))
        assert not node1.comper(node2)

    def test__copy__(self):
        n1=NodeData(0)
        n2=n1.__copy__()
        assert n1.comper(n2)
        n1=NodeData(0,(0,1,2))
        n2 = n1.__copy__()
        assert n1.comper(n2)