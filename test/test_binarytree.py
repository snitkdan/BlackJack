import unittest
from src.BinaryTree import BinaryTree, BinaryTreeNode

class TestBinaryTree(unittest.TestCase):
    """
    This class tests the BinaryTree class
    """

    def test_constructor(self):
        """
        Tests the state of a binary tree's root after initialization
        """
        try:  # test invalid tree creation
            bt = BinaryTree(None)
            self.assertTrue(False)
        except ValueError:
            bt = BinaryTree(BinaryTreeNode(1))
            self.assertEqual(bt.root.val, 1)

    def test_equivalent(self):
        """
        Tests whether tree equivalence with both equivalent and non-equivalent trees
        """
        bt1 = BinaryTree(BinaryTreeNode(1, BinaryTreeNode(2), BinaryTreeNode(3)))
        bt2 = BinaryTree(BinaryTreeNode(1, BinaryTreeNode(2), BinaryTreeNode(3)))
        self.assertTrue(bt1.is_equivalent(bt2))
        bt3 = BinaryTree(BinaryTreeNode(1))
        self.assertFalse(bt1.is_equivalent(bt3))
        bt4 = BinaryTree(BinaryTreeNode(1, BinaryTreeNode(3), BinaryTreeNode(2)))
        self.assertFalse(bt1.is_equivalent(bt4))

    def test_leaves_just_root(self):
        """
        Tests the leaves returned from a singleton root tree
        """
        bt = BinaryTree(BinaryTreeNode(1))
        self.assertListEqual(list(bt.get_leaves()), [bt.root])

    def test_leaves_basic(self):
        """
        Tests the leaves returned from a tree with a root and two children
        """
        nodes = BinaryTreeNode(1, BinaryTreeNode(2), BinaryTreeNode(3))
        bt = BinaryTree(nodes)
        self.assertListEqual(list(bt.get_leaves()), [nodes.left, nodes.right])

    def test_leaves_complex(self):
        """
        Tests the leaves returned from a 3-generation tree with different configurations of children
        """
        leaf1, leaf2, leaf3 = BinaryTreeNode(10), BinaryTreeNode(20), BinaryTreeNode(30)
        parent1, parent2 = BinaryTreeNode(5, leaf1, leaf2), BinaryTreeNode(15, leaf3)
        root = BinaryTreeNode(0, parent1, parent2)
        bt = BinaryTree(root)
        self.assertListEqual(list(bt.get_leaves()), [leaf1, leaf2, leaf3])

    def test_preorder(self):
        """
        Tests the nodes returned by a pre-order traversal of a 3-generation tree
        """
        leaf1, leaf2, leaf3 = BinaryTreeNode(10), BinaryTreeNode(20), BinaryTreeNode(30)
        parent1, parent2 = BinaryTreeNode(5, leaf1, leaf2), BinaryTreeNode(15, leaf3)
        root = BinaryTreeNode(0, parent1, parent2)
        bt = BinaryTree(root)
        self.assertListEqual(list(bt.get_preorder()), [root, parent1, leaf1, leaf2, parent2, leaf3])