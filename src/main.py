import unittest

from DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo




def test_shortestPathCompare1(self):
    """Runs the shortestPath method from this project's algo, and runs it also through
    netWorkX, to compare results and performance. runs on graph: G_10_80_1.json """

    print("reading from file...", self.algo.load_from_json("G_10_80_1.json"))
    print("shortestPath is ", self.algo.shortest_path(0, 4))




if __name__ == '__main__':
    unittest.main()

