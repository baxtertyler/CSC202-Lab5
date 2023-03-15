import unittest
from binary_search_tree import *


class TestLab5(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.inorder_list(), [])
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_is_empty(self):
        b = BinarySearchTree()
        # empty tree
        self.assertTrue(b.is_empty())
        b.insert(1, "X")
        # tree with at least 1 item
        self.assertFalse(b.is_empty())

    def test_search(self):
        b = BinarySearchTree()
        b.insert(10, "root")
        b.insert(5, "L")
        b.insert(15, "R")
        # in tree
        self.assertTrue(b.search(10))
        # not in tree
        self.assertFalse(b.search(0))
        # right side
        self.assertTrue(b.search(15))

    def test_insert(self):
        b = BinarySearchTree()
        b.insert(10, "root")
        b.insert(5, "L")
        b.insert(7, "LR")
        b.insert(15, "R")
        b.insert(12, "RL")
        b.insert(0, "LL")
        b.insert(20, "RR")
        self.assertEqual(b.root.key, 10)
        self.assertEqual(b.root.left.key, 5)
        self.assertEqual(b.root.left.left.key, 0)
        self.assertEqual(b.root.left.right.key, 7)
        self.assertEqual(b.root.right.key, 15)
        self.assertEqual(b.root.right.right.key, 20)
        self.assertEqual(b.root.right.left.key, 12)

    def test_find_min(self):
        b = BinarySearchTree()
        self.assertEqual(b.find_min(), None)
        b.insert(10, "root")
        self.assertEqual(b.find_min(), (10, "root"))
        b.insert(5, "L")
        self.assertEqual(b.find_min(), (5, "L"))
        b.insert(7, "LR")
        b.insert(15, "R")
        b.insert(12, "RL")
        b.insert(0, "LL")
        self.assertEqual(b.find_min(), (0, "LL"))
        b.insert(20, "RR")

    def test_find_max(self):
        b = BinarySearchTree()
        self.assertEqual(b.find_max(), None)
        b.insert(10, "root")
        self.assertEqual(b.find_max(), (10, "root"))
        b.insert(5, "L")
        b.insert(7, "LR")
        b.insert(15, "R")
        self.assertEqual(b.find_max(), (15, "R"))
        b.insert(12, "RL")
        b.insert(0, "LL")
        b.insert(20, "RR")
        self.assertEqual(b.find_max(), (20, "RR"))

    def test_tree_height(self):
        b = BinarySearchTree()
        self.assertEqual(b.tree_height(), None)
        b.insert(10, "root")
        # height of root
        self.assertEqual(b.tree_height(), 0)
        b.insert(11, "R")
        # height with 1 entry
        self.assertEqual(b.tree_height(), 1)
        b.insert(12, "RR")
        # height with 2 entries
        self.assertEqual(b.tree_height(), 2)
        # added to shorter leg, should not change
        b.insert(9, "L")
        self.assertEqual(b.tree_height(), 2)
        b.insert(8, "LL")
        self.assertEqual(b.tree_height(), 2)
        # other leg should be longer now
        b.insert(7, "LLL")
        self.assertEqual(b.tree_height(), 3)

    def test_inorder_list(self):
        b = BinarySearchTree()
        b.insert(10, "root")
        b.insert(5, "L")
        b.insert(7, "LR")
        b.insert(15, "R")
        b.insert(12, "RL")
        b.insert(0, "LL")
        b.insert(20, "RR")
        self.assertEqual(b.inorder_list(), [0, 5, 7, 10, 12, 15, 20])
        b2 = BinarySearchTree()
        b2.insert(0, "a")
        b2.insert(1, "b")
        b2.insert(2, "c")
        b2.insert(3, "d")
        b2.insert(4, "e")
        b2.insert(5, "f")
        b2.insert(6, "g")
        self.assertEqual(b2.inorder_list(), [0, 1, 2, 3, 4, 5, 6])
        b3 = BinarySearchTree()
        b3.insert(0, "a")
        b3.insert(-1, "b")
        b3.insert(-2, "c")
        self.assertEqual(b3.inorder_list(), [-2, -1, 0])

    def test_preorder_list(self):
        b = BinarySearchTree()
        b.insert(10, "root")
        b.insert(5, "L")
        b.insert(7, "LR")
        b.insert(15, "R")
        b.insert(12, "RL")
        b.insert(0, "LL")
        b.insert(20, "RR")
        self.assertEqual(b.preorder_list(), [10, 5, 0, 7, 15, 12, 20])
        b2 = BinarySearchTree()
        b2.insert(0, "a")
        b2.insert(1, "b")
        b2.insert(2, "c")
        b2.insert(3, "d")
        b2.insert(4, "e")
        b2.insert(5, "f")
        b2.insert(6, "g")
        self.assertEqual(b2.preorder_list(), [0, 1, 2, 3, 4, 5, 6])
        b3 = BinarySearchTree()
        b3.insert(0, "a")
        b3.insert(-1, "b")
        b3.insert(-2, "c")
        self.assertEqual(b3.preorder_list(), [0, -1, -2])

    def test_level_order_list(self):
        b = BinarySearchTree()
        b.insert(10, "root")
        b.insert(5, "L")
        b.insert(7, "LR")
        b.insert(15, "R")
        b.insert(12, "RL")
        b.insert(0, "LL")
        b.insert(20, "RR")
        self.assertEqual(b.level_order_list(), [10, 5, 15, 0, 7, 12, 20])
        b2 = BinarySearchTree()
        b2.insert(0, "a")
        b2.insert(1, "b")
        b2.insert(2, "c")
        b2.insert(3, "d")
        b2.insert(4, "e")
        b2.insert(5, "f")
        b2.insert(6, "g")
        self.assertEqual(b2.level_order_list(), [0, 1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
