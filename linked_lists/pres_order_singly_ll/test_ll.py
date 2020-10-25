import unittest
from random import randint

from linked_lists.pres_order_singly_ll.ll import PreserveOrderLinkedList
from linked_lists.pres_order_singly_ll.ll import Node


class TestPreserveOrderLinkedList(unittest.TestCase):
    def verify_none(self, ll: PreserveOrderLinkedList):
        head, tail = ll.getPointers()

        self.assertIsNone(head)
        self.assertIsNone(tail)

        self.assertRaises(Exception, ll.pop)
        self.assertRaises(Exception, ll.removeMiddle, randint(1, 50))
        self.assertRaises(Exception, ll.shift)

    def test_insert(self):
        for _ in range(5):
            ll = PreserveOrderLinkedList()

            self.verify_none(ll)

            pushedElements = []
            for _ in range(50):
                element = randint(-1000, 1000)
                pushedElements.append(element)
                pushedElements.sort()
                ll.insert(element)

                self.verify_data(pushedElements, ll.getPointers()[0])

    def test_remove_head(self):
        ll = PreserveOrderLinkedList()

        self.verify_none(ll)

        pushedElements = self.fill_data(ll)

        for _ in range(10):
            element = pushedElements[0]
            pushedElements = pushedElements[1:]
            removedElement = ll.shift()
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, ll.getPointers()[0])

    def test_remove_middle(self):
        ll = PreserveOrderLinkedList()

        self.verify_none(ll)

        self.assertRaises(Exception, ll.removeMiddle, 0)

        # number of elements to add from head and tail
        testRemoveHead = 5
        testRemoveMiddle = 10
        testRemoveTail = 5

        pushedElements = self.fill_data(ll)
        self.verify_data(pushedElements, ll.getPointers()[0])

        for _ in range(testRemoveHead):
            element = pushedElements[0]
            pushedElements = pushedElements[1:]
            removedElement = ll.removeMiddle(1)
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, ll.getPointers()[0])

        for _ in range(1, testRemoveTail):
            element = pushedElements[-1]
            pushedElements = pushedElements[:-1]
            removedElement = ll.removeMiddle(len(pushedElements)+1)
            self.assertEqual(element, removedElement)
            self.verify_data(pushedElements, ll.getPointers()[0])

        for _ in range(testRemoveMiddle):
            position = randint(2, len(pushedElements)-1)
            element = pushedElements[position-1]
            pushedElements = pushedElements[:position -
                                            1] + pushedElements[position:]
            removedElement = ll.removeMiddle(position)
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, ll.getPointers()[0])

    def test_remove_tail(self):
        ll = PreserveOrderLinkedList()

        self.verify_none(ll)

        pushedElements = self.fill_data(ll)

        for _ in range(10):
            element = pushedElements[-1]
            pushedElements = pushedElements[:-1]
            removedElement = ll.pop()
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, ll.getPointers()[0])

    def fill_data(self, ll: PreserveOrderLinkedList, fill_size=25):
        pushedElements = []

        for _ in range(fill_size):
            element = randint(-1000, 1000)
            pushedElements.append(element)
            ll.insert(element)

        return sorted(pushedElements)

    def verify_data(self, items, head: Node):
        currNode = head
        arr = []
        while currNode is not None:
            arr.append(currNode.data)
            currNode = currNode.next

        self.assertEqual(items, arr)
