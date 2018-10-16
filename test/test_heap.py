import unittest
from src.MaxHeap import MaxHeap


class HeapTestClass(object):
    """
    Simple test class to use in unit tests for MaxHeap
    """
    def __init__(self, val):
        """
        Constructor
        """
        self.val = val

    def get_priority(self):
        """
        :return: the value of self
        """
        return self.val


class TestHeap(unittest.TestCase):
    """
    This class tests the MaxHeap class
    """
    def test_insert_one(self):
        """
        Tests the state of a MaxHeap after inserting 1 item.
        """
        h = MaxHeap(2)
        item = HeapTestClass(1)
        h.insert(item)
        self.assertEqual(item, h.findMax())
        self.assertListEqual(h.heap_arr, [item, None])

    def test_insert_two(self):
        """
        Tests the state of a MaxHeap after inserting 2 items in different orders.
        """
        h = MaxHeap(3)
        item1 = HeapTestClass(1)
        item2 = HeapTestClass(2)
        # Low priority --> Higher priority
        h.insert(item1)
        h.insert(item2)
        self.assertEqual(item2, h.findMax())
        self.assertListEqual(h.heap_arr, [item2, item1, None])
        # High priority --> lower priority
        h = MaxHeap(3)
        h.insert(item2)
        h.insert(item1)
        self.assertEqual(item2, h.findMax())
        self.assertListEqual(h.heap_arr, [item2, item1, None])

    def test_insert_five(self):
        """
        Tests the state of a MaxHeap after inserting 5 items
        """
        h = MaxHeap(6)
        item1 = HeapTestClass(1)
        item2 = HeapTestClass(2)
        item3 = HeapTestClass(3)
        item4 = HeapTestClass(4)
        item5 = HeapTestClass(5)
        h.insert(item2)
        h.insert(item3)
        h.insert(item4)
        h.insert(item1)
        h.insert(item5)
        self.assertEqual(item5, h.findMax())
        self.assertListEqual(h.heap_arr, [item5, item4, item3, item1, item2, None])

    def test_removeMax_empty(self):
        """
        Tests the edge case when removeMax is called on an empty MaxHeap
        """
        h = MaxHeap(2)
        try:
            h.removeMax()
        except ValueError:
            self.assertTrue(h.isEmpty())

    def test_removeMax_one(self):
        """
        Tests the state of a MaxHeap with 1 initial item that is then removed.
        """
        h = MaxHeap(2)
        item = HeapTestClass(1)
        h.insert(item)
        self.assertEqual(item, h.removeMax())
        self.assertEqual(h.size, 0)

    def test_removeMax_two(self):
        """
        Tests the state of a MaxHeap with 2 initial items that are removed in different orders
        """
        h = MaxHeap(3)
        item1 = HeapTestClass(1)
        item2 = HeapTestClass(2)
        # Low priority --> Higher priority
        h.insert(item1)
        h.insert(item2)
        self.assertEqual(item2, h.removeMax())
        self.assertEqual(h.size, 1)
        self.assertEqual(item1, h.removeMax())
        self.assertTrue(h.isEmpty())
        # High priority --> lower priority
        h = MaxHeap(3)
        h.insert(item2)
        h.insert(item1)
        self.assertEqual(item2, h.removeMax())
        self.assertEqual(h.size, 1)
        self.assertEqual(item1, h.removeMax())
        self.assertTrue(h.isEmpty())

    def test_removeMax_five(self):
        """
        Tests the stateof a MaxHeap with 5 initial items that are all removed
        """
        h = MaxHeap(6)
        item1 = HeapTestClass(1)
        item2 = HeapTestClass(2)
        item3 = HeapTestClass(3)
        item4 = HeapTestClass(4)
        item5 = HeapTestClass(5)
        h.insert(item2)
        h.insert(item3)
        h.insert(item4)
        h.insert(item1)
        h.insert(item5)
        removed = [h.removeMax() for i in range(5)]
        self.assertListEqual(removed, [item5, item4, item3, item2, item1])
        self.assertTrue(h.isEmpty())

    def test_floydBuildHeap_empty(self):
        """
        Tests the edge case of running Build Heap on an empty initial collection
        """
        h = MaxHeap(0, [])
        self.assertTrue(h.isEmpty())

    def test_floydBuildHeap_one(self):
        """
        Tests Build Heap on a 1 element collection
        """
        item = HeapTestClass(1)
        h = MaxHeap(1, [item])
        self.assertEqual(item, h.findMax())
        self.assertListEqual(h.heap_arr, [item])

    def test_floydBuildHeap_two(self):
        """
        Tests Build Heap on a 2 element collection
        """
        item1 = HeapTestClass(1)
        item2 = HeapTestClass(2)
        # Low priority --> Higher priority
        h = MaxHeap(2, [item1, item2])
        self.assertEqual(item2, h.findMax())
        self.assertListEqual(h.heap_arr, [item2, item1])
        # High priority --> lower priority
        h = MaxHeap(2, [item1, item2])
        self.assertEqual(item2, h.findMax())
        self.assertListEqual(h.heap_arr, [item2, item1])



