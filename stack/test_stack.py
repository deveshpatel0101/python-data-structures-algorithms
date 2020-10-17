from stack.stack import Stack
from random import randint
import unittest


class TestStack(unittest.TestCase):
    def verify_empty(self, stck: Stack):
        self.assertEqual([], stck.get_items())

        self.assertTrue(stck.is_empty())

        self.assertRaises(Exception, stck.pop)

        self.assertFalse(stck.is_full())

        self.assertEqual(stck.size, stck.get_size())

    def test_push_pop(self):
        stck = Stack(randint(1, 50))

        self.verify_empty(stck)

        stck.push(1)
        self.assertEqual([1], stck.get_items())

        self.assertFalse(stck.is_empty())

        self.assertEqual(1, stck.peek())

        item, top = stck.pop()
        self.assertEqual(item, 1)
        self.assertEqual(top, 0)

        self.verify_empty(stck)

    def test_full_push_pop(self):
        stck = Stack(randint(1, 50))

        self.verify_empty(stck)

        for index in range(stck.size):
            item, top = stck.push(index)
            self.assertEqual(index, item)
            self.assertEqual(index+1, top)

        self.verify_full(stck)

        for index in range(stck.size-1, -1, -1):
            self.assertEqual(index, stck.peek())
            item, top = stck.pop()
            self.assertEqual(index, item)
            self.assertEqual(index, top)

        self.verify_empty(stck)

    def verify_full(self, stck: Stack):
        self.assertTrue(stck.is_full())

        self.assertFalse(stck.is_empty())

        self.assertEqual(stck.size, len(stck.get_items()))

        self.assertEqual(
            [index for index in range(stck.size)], stck.get_items())

        self.assertEqual(stck.size-1, stck.peek())

        self.assertRaises(Exception, stck.push, randint(0, 10))
