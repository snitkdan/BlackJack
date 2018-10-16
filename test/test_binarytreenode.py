import unittest
from src.BinaryTree import BinaryTreeNode

class TestBinaryTreeNode(unittest.TestCase):
    """
    This class tests the BinaryTreeNode class
    """

    def test_no_children(self):
        """
        Tests the state of a singelton node
        """
        node = BinaryTreeNode(1)
        # Test value
        self.assertEqual(node.val, 1)
        # Test children
        self.assertFalse(node.has_children())
        self.assertListEqual(list(node.get_children()), [])

    def test_one_child(self):
        """
        Tests the state of different configurations of a node with 1 child (left or right)
        """
        node1 = BinaryTreeNode(2, BinaryTreeNode(3))
        node2 = BinaryTreeNode(4, None, BinaryTreeNode(5))
        # Test value
        self.assertEqual(node1.val, 2)
        self.assertEqual(node2.val, 4)
        # Test children
        self.assertTrue(node1.has_children())
        self.assertTrue(node2.has_children())
        self.assertListEqual(list(node1.get_children()), [node1.left])
        self.assertListEqual(list(node2.get_children()), [node2.right])
        self.assertEqual(node1.left.val, 3)
        self.assertEqual(node2.right.val, 5)

    def test_two_children(self):
        """
        Tests the state of a complete node (one w/ 2 children, left and right)
        """
        node = BinaryTreeNode(1, BinaryTreeNode(2), BinaryTreeNode(3))
        # Test value
        self.assertEqual(node.val, 1)
        # Test children
        self.assertTrue(node.has_children())
        self.assertEqual(node.left.val, 2)
        self.assertEqual(node.right.val, 3)
        self.assertListEqual(list(node.get_children()), [node.left, node.right])



