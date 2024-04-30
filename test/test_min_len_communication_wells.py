import unittest
from NulpAlgoLabs.src.min_len_communication_wells import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        graph = kruskal(read_input('resources/communication_wells.csv'))
        self.assertEqual(graph, 37)

    def test_multi_graph(self):
        graph = kruskal(read_input('resources/communication_wells_multi.csv'))
        self.assertEqual(graph, -1)

    def test_empty_graph(self):
        graph = kruskal(read_input('resources/communication_wells_empty.csv'))
        self.assertEqual(graph, 0)


if __name__ == '__main__':
    unittest.main()
