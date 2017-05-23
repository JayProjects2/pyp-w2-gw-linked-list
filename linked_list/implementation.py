from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.elements = []
        self.start = None
        self.end = None
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return "{}".format([item.elem for item in self])

    def __len__(self):
        count = 0
        for elem in self:
            count += 1
        return count

    def __iter__(self):
        elem = self.start
        while elem:
            yield elem
            elem = elem.next
        raise StopIteration()

    def __getitem__(self, index):
        if index < 0:
            index = (len(self) - abs(index))
        if index >= len(self):
            raise IndexError()
        count = 0
        for elem in self:
            if count == index:
                return elem
            else:
                count += 1

    def __add__(self, other):
        new = LinkedList([elem.elem for elem in self])
        for item in other:
            new.append(item.elem)
        return new

    def __iadd__(self, other):
        for elem in other:
            self.append(elem.elem)
        return self

    def __eq__(self, other):
        # If both are empty (None), it has to be equal...
        if self.start is None and other.start is None:
            return True
        # This way, since both aren't None, if either of them is None, we stop here.
        elif other.start is None or self.start is None:
            return False
        elem1 = self.start
        elem2 = other.start

        if len(self) == len(other):
            while True:
                if elem1.elem != elem2.elem:
                    return False
                if elem1.next is None:
                    return True
                elem1 = elem1.next
                elem2 = elem2.next
        return False

    def __ne__(self, other):
        return not self == other

    def append(self, elem):
        node = Node(elem)
        if self.start is None:
            self.start = node
            self.end = self.start
            return self.start

        self.end.next = node
        self.end = node

    def count(self):
        return len(self)


    def pop(self, index=None):
        if index is None:
            index = (len(self) - 1)
        if index < 0:
            index = len(self) - abs(index)
        if len(self) == 0 or index >= len(self):
            raise IndexError
        if index == 0:
            elem = self.start.elem
            self.start = self.start.next
            return elem
        
        node = self.start
        hold = None
        count = 0
        while True: 
            if count == index:
                hold.next = node.next
                return node.elem
            hold = node
            node = node.next
            count += 1