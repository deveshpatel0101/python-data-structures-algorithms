from stack.stack import Stack
import unittest


class TestStack(unittest.TestCase):
    def test_empty(self, stck: Stack = Stack()):
        # Case 1:
        # should return empty stack array
        self.assertEqual([], stck.get_items())

        # Case 2:
        # should return true if is_empty is called on empty stack
        self.assertTrue(stck.is_empty())

        # Case 3:
        # should return error if called pop on an empty stack
        self.assertRaises(Exception, stck.pop)

        # Case 4:
        # should return false if stack is not full
        self.assertFalse(stck.is_full())

        # Case 5:
        # should return the size of stack
        self.assertEqual(5, stck.get_size())

    def test_push_pop(self, stck: Stack = Stack()):
        stck.push(1)

        # Case 1:
        # All items pushed should be in the stack
        self.assertEqual([1], stck.get_items())

        # Case 2:
        # should not be empty
        self.assertFalse(stck.is_empty())

        # Case 3:
        # peek should return the last pushed item
        self.assertEqual(1, stck.peek())

        # Case 4:
        # pop should return the last item pushed and top value, and remove it from the stack
        item, top = stck.pop()
        self.assertEqual(1, item)
        self.assertEqual(0, top)

        # Case 5:
        # should satisfy all properties of empty stack
        self.test_empty(stck)

    def test_full_push_full_pop(self, stck: Stack = Stack()):
        for index in range(stck.get_size()):
            item, top = stck.push(index)
            self.assertEqual(index, item)
            self.assertEqual(index+1, top)

        self.verify_full(stck)

        for index in range(stck.get_size()-1, -1, -1):
            self.assertEqual(index, stck.peek())
            item, top = stck.pop()
            self.assertEqual(index, item)
            self.assertEqual(index, top)

        self.test_empty(stck)

    def verify_full(self, stck: Stack = Stack()):
        # Case 1:
        # should return true on full stack
        self.assertTrue(stck.is_full())

        # Case 2:
        # should return false on un empty stack
        self.assertFalse(stck.is_empty())

        # Case 3:
        # should have 5 items in full stack
        self.assertEqual(5, len(stck.get_items()))

        # Case 4:
        # should return items the way they were inserted
        self.assertEqual([0, 1, 2, 3, 4], stck.get_items())

        # Case 5:
        # should return the last item pushed on peek
        self.assertEqual(4, stck.peek())

        # Case 6:
        # should raise Exception on pushing on full stack
        self.assertRaises(Exception, stck.push, 5)
