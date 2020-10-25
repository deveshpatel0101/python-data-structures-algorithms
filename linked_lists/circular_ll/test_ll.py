import unittest
from random import randint

from linked_lists.circular_ll.ll import CircularLinkedList
from linked_lists.circular_ll.ll import Node


class TestCircularLinkedList(unittest.TestCase):
    def verify_none(self, ll: CircularLinkedList):
        head, tail = ll.getPointers()

        self.assertIsNone(head)
        self.assertIsNone(tail)

        self.assertRaises(Exception, ll.pop)
        self.assertRaises(Exception, ll.removeMiddle, randint(1, 50))
        self.assertRaises(Exception, ll.insertMiddle, 0, randint(1, 50))
        self.assertRaises(Exception, ll.shift)

    def test_insert_head(self):
        ll = CircularLinkedList()

        self.verify_none(ll)

        pushedElements = []
        element = randint(1, 50)
        pushedElements.append(element)
        ll.unshift(element)

        head, tail = ll.getPointers()
        self.assertEqual(head, tail)
        self.verify_data(pushedElements, *ll.getPointers())
        self.assertEqual(tail.next, head)

        for _ in range(randint(5, 20)):
            element = randint(1, 50)
            pushedElements.append(element)
            ll.unshift(element)
            self.verify_data(pushedElements[::-1], *ll.getPointers())

    def test_insert_middle(self):
        ll = CircularLinkedList()

        self.verify_none(ll)

        # number of elements to add from head and tail
        testPushHead = 5
        testPushMiddle = 10
        testPushTail = 5

        pushedElements = []
        element = randint(1, 50)
        pushedElements.append(element)
        ll.insertMiddle(1, element)

        head, tail = ll.getPointers()
        self.assertEqual(head, tail)
        self.assertEqual(tail.next, head)

        for _ in range(testPushHead):
            element = randint(1, 50)
            pushedElements = [element] + pushedElements
            ll.insertMiddle(1, element)
            self.verify_data(pushedElements, *ll.getPointers())

        for _ in range(1, testPushTail):
            element = randint(1, 50)
            pushedElements.append(element)
            ll.insertMiddle(len(pushedElements), element)
            self.verify_data(pushedElements, *ll.getPointers())

        for _ in range(testPushMiddle):
            element = randint(1, 50)
            position = randint(1, len(pushedElements)-1)
            ll.insertMiddle(position, element)
            pushedElements = pushedElements[:position-1] + \
                [element] + pushedElements[position-1:]
            self.verify_data(pushedElements, *ll.getPointers())

    def test_insert_tail(self):
        ll = CircularLinkedList()

        self.verify_none(ll)

        pushedElements = []
        element = randint(1, 50)
        pushedElements.append(element)
        ll.push(element)
        head, tail = ll.getPointers()
        self.assertEqual(head, tail)
        self.verify_data(pushedElements, head, tail)
        self.assertEqual(tail.next, head)

        for _ in range(10):
            element = randint(1, 50)
            pushedElements.append(element)
            ll.push(element)
            self.verify_data(pushedElements, *ll.getPointers())

    def test_remove_head(self):
        ll = CircularLinkedList()

        self.verify_none(ll)

        pushedElements = self.fill_data(ll)

        for _ in range(10):
            element = pushedElements[0]
            pushedElements = pushedElements[1:]
            removedElement = ll.shift()
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, *ll.getPointers())

    def test_remove_middle(self):
        ll = CircularLinkedList()

        self.verify_none(ll)

        self.assertRaises(Exception, ll.removeMiddle, 0)

        # number of elements to add from head and tail
        testRemoveHead = 5
        testRemoveMiddle = 10
        testRemoveTail = 5

        pushedElements = self.fill_data(ll)
        self.verify_data(pushedElements, *ll.getPointers())

        for _ in range(testRemoveHead):
            element = pushedElements[0]
            pushedElements = pushedElements[1:]
            removedElement = ll.removeMiddle(1)
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, *ll.getPointers())

        for _ in range(1, testRemoveTail):
            element = pushedElements[-1]
            pushedElements = pushedElements[:-1]
            removedElement = ll.removeMiddle(len(pushedElements)+1)
            self.assertEqual(element, removedElement)
            self.verify_data(pushedElements, *ll.getPointers())

        for _ in range(testRemoveMiddle):
            position = randint(2, len(pushedElements)-1)
            element = pushedElements[position-1]
            pushedElements = pushedElements[:position -
                                            1] + pushedElements[position:]
            removedElement = ll.removeMiddle(position)
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, *ll.getPointers())

    def test_remove_tail(self):
        ll = CircularLinkedList()

        self.verify_none(ll)

        pushedElements = self.fill_data(ll)
        self.verify_data(pushedElements, *ll.getPointers())

        for _ in range(10):
            element = pushedElements[-1]
            pushedElements = pushedElements[:-1]
            removedElement = ll.pop()
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, *ll.getPointers())

    def test_reverse(self):
        ll = CircularLinkedList()

        self.verify_none(ll)

        pushedElements = self.fill_data(ll)
        self.verify_data(pushedElements, *ll.getPointers())

        ll.reverse()
        self.verify_data(pushedElements[::-1], *ll.getPointers())

    def fill_data(self, ll: CircularLinkedList, fill_size=25):
        pushedElements = []

        for _ in range(fill_size):
            element = randint(1, 50)
            pushedElements.append(element)
            ll.push(element)

        return pushedElements

    def verify_data(self, items, head: Node, tail: Node):
        currNode = head
        arr = []

        while currNode.next is not head:
            arr.append(currNode.data)
            currNode = currNode.next
        else:
            arr.append(currNode.data)
            currNode = currNode.next

        self.assertEqual(items, arr)
        self.assertEqual(tail.next, head)
