from queues.simple_queue.simple_queue import SimpleQueue
from random import randint
import unittest


class TestSimpleQueue(unittest.TestCase):
    def verify_empty(self, q: SimpleQueue):
        front, rear = q.get_pointers()

        self.assertEqual(front, -1)
        self.assertEqual(rear, -1)

        self.assertRaises(Exception, q.remove)

        self.assertEqual([None] * (q.size+1), q.get_queue())

    def test_insert_remove(self):
        q = SimpleQueue(randint(1, 50))

        self.verify_empty(q)

        element = randint(0, 10)
        q.insert(element)

        front, rear = q.get_pointers()
        self.assertEqual(front, 0)
        self.assertEqual(rear, 0)

        removedElement = q.remove()
        self.assertEqual(element, removedElement)

        front, rear = q.get_pointers()
        self.assertEqual(front, -1)
        self.assertEqual(rear, -1)

        self.verify_empty(q)

    def test_full_insert_remove(self):
        q = SimpleQueue(randint(1, 50))
        self.verify_empty(q)

        for index in range(q.size+1):
            q.insert(index)
            front, rear = q.get_pointers()
            self.assertEqual(front, 0)
            self.assertEqual(rear, index)

        for index in range(q.size+1):
            element = q.remove()
            self.assertEqual(element, index)

            front, rear = q. get_pointers()
            if index == q.size:
                self.assertEqual(front, -1)
                self.assertEqual(rear, -1)
            else:
                self.assertEqual(front, index+1)
                self.assertEqual(rear, q.size)

        self.verify_empty(q)

    def verify_full(self, q: SimpleQueue):
        _, rear = q.get_pointers()
        self.assertEqual(rear, q.size)

        self.assertRaises(Exception, q.insert, randint(0, 10))

        arr = q.get_queue()
        self.assertIsNotNone(arr[-1])
