import unittest
from random import randint

from linked_lists.singly_ll.ll import SinglyLinkedList
from linked_lists.singly_ll.ll import Node


class TestSinglyLinkedList(unittest.TestCase):
    def verify_none(self, ll: SinglyLinkedList):
        head, tail = ll.getPointers()

        self.assertIsNone(head)
        self.assertIsNone(tail)

        self.assertRaises(Exception, ll.pop)
        self.assertRaises(Exception, ll.removeMiddle, randint(1, 50))
        self.assertRaises(Exception, ll.insertMiddle, 0, randint(1, 50))
        self.assertRaises(Exception, ll.shift)

    def test_insert_head(self):
        ll = SinglyLinkedList()

        self.verify_none(ll)

        pushedElements = []
        element = randint(1, 50)
        pushedElements.append(element)
        ll.unshift(element)

        head, tail = ll.getPointers()
        self.assertEqual(head, tail)
        self.verify_data(pushedElements, ll.getPointers()[0])

        for _ in range(randint(5, 20)):
            element = randint(1, 50)
            pushedElements.append(element)
            ll.unshift(element)
            self.verify_data(pushedElements[::-1], ll.getPointers()[0])

    def test_insert_middle(self):
        ll = SinglyLinkedList()

        self.verify_none(ll)

        # number of elements to add from head and tail
        testPushHead = 5
        testPushMiddle = 5
        testPushTail = 10

        pushedElements = []
        element = randint(1, 50)
        pushedElements.append(element)
        ll.insertMiddle(1, element)

        head, tail = ll.getPointers()
        self.assertEqual(head, tail)

        for _ in range(testPushHead):
            element = randint(1, 50)
            pushedElements = [element] + pushedElements
            ll.insertMiddle(1, element)
            self.verify_data(pushedElements, ll.getPointers()[0])

        for _ in range(1, testPushTail):
            element = randint(1, 50)
            pushedElements.append(element)
            ll.insertMiddle(len(pushedElements), element)
            self.verify_data(pushedElements, ll.getPointers()[0])

        for _ in range(testPushMiddle):
            element = randint(1, 50)
            position = randint(1, len(pushedElements)-1)
            ll.insertMiddle(position, element)
            pushedElements = pushedElements[:position-1] + \
                [element] + pushedElements[position-1:]
            self.verify_data(pushedElements, ll.getPointers()[0])

    def test_insert_tail(self):
        ll = SinglyLinkedList()

        self.verify_none(ll)

        pushedElements = []
        element = randint(1, 50)
        pushedElements.append(element)
        ll.push(element)
        head, tail = ll.getPointers()
        self.assertEqual(head, tail)
        self.verify_data(pushedElements, head)

        for _ in range(10):
            element = randint(1, 50)
            pushedElements.append(element)
            ll.push(element)
            self.verify_data(pushedElements, ll.getPointers()[0])

    def test_remove_head(self):
        ll = SinglyLinkedList()

        self.verify_none(ll)

        pushedElements = self.fill_data(ll)

        for _ in range(10):
            element = pushedElements[0]
            pushedElements = pushedElements[1:]
            removedElement = ll.shift()
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, ll.getPointers()[0])

    def test_remove_middle(self):
        ll = SinglyLinkedList()

        self.verify_none(ll)

        self.assertRaises(Exception, ll.removeMiddle, 0)

        # number of elements to add from head and tail
        testRemoveHead = 5
        testRemoveMiddle = 5
        testRemoveTail = 10

        pushedElements = self.fill_data(ll)
        pushedElements = pushedElements[1:]
        ll.removeMiddle(1)
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
        ll = SinglyLinkedList()

        self.verify_none(ll)

        pushedElements = self.fill_data(ll)

        for _ in range(10):
            element = pushedElements[-1]
            pushedElements = pushedElements[:-1]
            removedElement = ll.pop()
            self.assertEqual(removedElement, element)
            self.verify_data(pushedElements, ll.getPointers()[0])

    def test_reverse(self):
        ll = SinglyLinkedList()

        self.verify_none(ll)

        pushedElements = self.fill_data(ll)

        ll.reverse()
        self.verify_data(pushedElements[::-1], ll.getPointers()[0])

    def fill_data(self, ll: SinglyLinkedList, fill_size=25):
        pushedElements = []

        for _ in range(fill_size):
            element = randint(1, 50)
            pushedElements.append(element)
            ll.push(element)

        return pushedElements

    def verify_data(self, items, head: Node):
        currNode = head
        arr = []
        while currNode is not None:
            arr.append(currNode.data)
            currNode = currNode.next

        self.assertEqual(items, arr)
