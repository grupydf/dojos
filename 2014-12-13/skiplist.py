import unittest
import random


class Node(object):
    def __init__(self, value):
        self.value = value
        self.level = self._generate_level()
        self.list = [None for i in xrange(self.level)]

    def _generate_level(self):
        i = 1
        while random.choice((True, False)):
            i += 1
        return i


class SkipList(object):
    def __init__(self):
        self.head = Node(0)


class TestCase(unittest.TestCase):
    def test_new_node(self):
        self.assertIsInstance(Node(1), Node)

    def test_level_will_never_be_zero(self):
        node = Node(5)
        self.assertGreater(node._generate_level(), 0)

    def test_node_value(self):
        value = 1
        node = Node(value)
        self.assertIs(node.value, value)

    def test_level(self):
        node = Node(2)
        self.assertGreater(node.level, 0)

    def test_generate_list(self):
        node = Node(10)
        self.assertIsInstance(node.list, list)
        self.assertEqual(node.level, len(node.list))

    def test_new_skiplist(self):
        skiplist = SkipList()
        self.assertIsInstance(skiplist, SkipList)

    def test_first_node(self):
        skiplist = SkipList()
        self.assertIsInstance(skiplist.head, Node)

    def test_skiplist_nodes(self):
        skiplist = SkipList()
        self.assertIsInstance(skiplist.nodes, list)
