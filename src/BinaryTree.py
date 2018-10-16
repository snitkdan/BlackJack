from collections import deque

class BinaryTreeNode(object):
    """
    This class represents a single Node w/ a value within a BinaryTree that can have
    at most 2 children (left and right)
    """

    def __init__(self, val, left=None, right=None):
        """
        Constructs a BinaryTreeNode

        :param val: the value within this node
        :param left: BinaryTreeNode representing the left child
        :param right: BinaryTreeNode representing the right child
        """
        self.val = val
        self.left = left
        self.right = right

    def get_children(self):
        """
        :return: a collection of children, starting with the left child (if not None),
        and then followed by the right child (if not None)
        """
        children = deque()
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children

    def has_children(self):
        """
        :return: True if the left child or the right child of this node is not None
        """
        return self.left or self.right


class BinaryTree(object):
    """
    This class represents a BinaryTree, which is a Directed Acyclic Graph in which each node can have at most
    1 parent and at most 2 children, culminating in a single root that is common ancestor of all other nodes.
    """
    def __init__(self, root: BinaryTreeNode):
        """
        Constructs a BinaryTree with a single root node

        :param root: the "top" of the BinaryTree (raises ValueError if None)
        """
        self.__ensureroot(root)
        self.root = root

    def __ensureroot(self, root: BinaryTreeNode):
        """
        Ensures rep-invariant that the root of a BinaryTree may not be None

        :param root: the "top" of a BinaryTree (raises ValueError if None)
        """
        if not root:
            raise ValueError('Root cannot be None')

    def get_preorder(self, justleaves=False):
        """
        :param justleaves: if True, only returns the leaves (nodes without children)
        :return: a collection of nodes resulting in a pre-order traversal of the tree
        """
        self.__ensureroot(self.root)
        to_explore = deque([self.root])  # collection of nodes to explore
        nodes = deque()  # collection of nodes to return
        while len(to_explore) > 0:
            curr = to_explore.popleft()
            if curr.has_children():  # non-leaf
                if not justleaves:
                    nodes.append(curr)
                # add the children to the front of the exploration collection
                children = curr.get_children()
                children.reverse()
                to_explore.extendleft(children)
            else:  # leaf
                nodes.append(curr)
        return nodes

    def get_leaves(self):
        """
        :return: the leaves (nodes without children) of the tree resulting in a pre-order traversal
        """
        return self.get_preorder(True)

    def is_equivalent(self, other):
        """
        :param other: BinaryTree to be tested for equality against this one
        :return: True if other has the same number of nodes and with the same values in the same positions
        resulting from a pre-order traversal (NOTE: this allows for different structures to be equivalent)
        """
        this_nodes = self.get_preorder()
        other_nodes = other.get_preorder()
        if len(this_nodes) != len(other_nodes):  # unequal number of nodes
            return False
        for (a, b) in zip(this_nodes, other_nodes):
            if a.val != b.val:  # unequal node at a particular position in the traversal
                return False
        return True





