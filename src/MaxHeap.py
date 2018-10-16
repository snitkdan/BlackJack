class MaxHeap(object):
    """
    This class represents a binary (at most 2 children) MaxHeap, defined as a
    tree-like data structure that has 2 properties:

        1. All children are less than or equal to their parents in priority
        2. If a parent has children, it must have a left child. A right child is optional.
    """

    def __init__(self, initial_capacity=10, initial_heap=None):
        """
        Constructs a MaxHeap

        :param initial_capacity: starting number of items to support before resizing
        :param initial_heap: collection of items to be converted to a MaxHeap via Floyd's Build Heap algorithm
        """
        if initial_heap:
            self.size = initial_capacity
            self.floydBuildHeap(initial_heap)
        else:
            self.size = 0
            self.heap_arr = [None] * initial_capacity

    def __doublecapacity(self):
        """
        Copies the elements of heap_arr into a list with
        length = size * 2
        """
        doubled_heap_arr = [None] * self.size * 2
        for i in range(self.size):
            doubled_heap_arr[i] = self.heap_arr[i]
        self.heap_arr = doubled_heap_arr

    def __gt__(self, a: int, b: int):
        """
        :param a: index within heap_arr
        :param b: index within heap_arr
        :return: True if the item at index a has a higher priority than the item at index b, and False otherwise
        """
        priority_a = float('-inf') if (a is None or self.heap_arr[a] is None) else self.heap_arr[a].get_priority()
        priority_b = float('-inf') if (b is None or self.heap_arr[b] is None) else self.heap_arr[b].get_priority()
        return priority_a > priority_b

    def __swap(self, a: int, b: int):
        """
        Switches the element in index a with the element in index b

        :param a: index within heap_arr
        :param b: index within heap_arr
        """
        tmp = self.heap_arr[a]
        self.heap_arr[a] = self.heap_arr[b]
        self.heap_arr[b] = tmp

    def __percolateUp(self, out_of_order: int):
        """
        Swaps elements from out_of_order up the hierarchy until the MaxHeap property is restored.

        :param out_of_order: the index that violates the MaxHeap properties
        """
        while out_of_order > 0 and self.__gt__(out_of_order, self.__getparent(out_of_order)):
            self.__swap(out_of_order, self.__getparent(out_of_order))
            out_of_order = self.__getparent(out_of_order)

    def insert(self, item: object):
        """
        Inserts a value into the MaxHeap, re-arranging the structure
        to maintain the MaxHeap properties

        :param item: item to be inserted (must have a get_priority method)
        """
        if self.size == len(self.heap_arr) - 1:
            self.__doublecapacity()
        self.heap_arr[self.size] = item
        self.__percolateUp(self.size)
        self.size += 1

    def __biggestChild(self, a: int):
        """
        :param a: index within the heap_arr
        :return: the child index of a that has the highest priority, and None if there are no children
        """
        left_child, right_child = self.__getleftchild(a), self.__getrightchild(a)
        return left_child if self.__gt__(left_child, right_child) else right_child

    def __percolateDown(self, out_of_order: int):
        """
        Swaps elements from out_of_order down the hierarchy until the MaxHeap property is restored.

        :param out_of_order: the index that violates the MaxHeap properties
        """
        to_swap = self.__biggestChild(out_of_order)
        while to_swap and self.__gt__(to_swap, out_of_order):
            self.__swap(to_swap, out_of_order)
            out_of_order = to_swap
            to_swap = self.__biggestChild(out_of_order)

    def findMax(self):
        """
        :return: the maximum item from the MaxHeap, defined as the highest
        priority item. (raises a ValueError if the MaxHeap is empty).
        """
        if self.isEmpty():
            raise ValueError('Cannot perform operation on empty MaxHeap')
        return self.heap_arr[0]

    def removeMax(self):
        """
        :return: the maximum item from the MaxHeap, defined as the highest
        priority item. (raises a ValueError if the MaxHeap is empty). The item
        is removed from the MaxHeap, and causes it to re-arrange the structure to maintain
        the MaxHeap properties.
        """
        ret = self.findMax()
        self.heap_arr[0] = self.heap_arr[self.size - 1]
        self.size -= 1
        self.__percolateDown(0)
        return ret

    def isEmpty(self):
        """
        :return: True if there are no items left in the MaxHeap, and False otherwise.
        """
        return self.size == 0

    def __getparent(self, heap_index: int):
        """
        :param heap_index: index within heap_arr to find the parent of
        :return: the index within heap_arr of the parent of heap_index
        (None if getting the parent of the root)
        """
        return None if heap_index == 0 else int((heap_index - 1) / 2)

    def __getchild(self, heap_index: int, child_num: int):
        """
        :param heap_index: index within heap_arr to find the parent of
        :param child_num: 1 if left child, 2 if right child
        :return: the index within heap_arr of the child_num child of heap_index (None if the child is
        outside the bounds of the current size)
        """
        child_idx = 2 * heap_index + child_num
        return None if child_idx >= self.size else child_idx

    def __getleftchild(self, heap_index: int):
        """
        :param heap_index: index within heap_arr to find the parent of
        :return: the index within heap_arr of the left child of heap_index
        """
        return self.__getchild(heap_index, 1)

    def __getrightchild(self, heap_index: int):
        """
        :param heap_index: index within heap_arr to find the parent of
        :return: the index within heap_arr of the right child of heap_index
        """
        return self.__getchild(heap_index, 2)

    def floydBuildHeap(self, items: [object]):
        """
        Initializes self to a MaxHeap with the given items using
        Floyd's Build Heap algorithm

        :param items: collection of items to be converted to a MaxHeap
        """
        start = int((self.size + 1) / 2)
        self.heap_arr = [item for item in items]
        for i in range(start, -1, -1):
            self.__percolateDown(i)