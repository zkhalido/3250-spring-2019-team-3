import unittest
import sys
sys.path.append("/Users/zack/Documents/GitConfused/jvpm")
from stack import Stack

class TestStack(unittest.TestCase):
    #def setUp(self):

    def test_is_empty(self):
        #S = stack.Stack()
        S = Stack()
        S.push(3)
        self.assertFalse(S.is_empty())
        S.pop()
        self.assertTrue(S.is_empty())

    def test_push(self):
        #S = stack.Stack()
        S = Stack()
        S.push(2)
        S.push(3)
        v = S.pop()
        self.assertEqual(v, 3)

    def test_pop(self):
        #S = stack.Stack()
        S = Stack()
        S.push(3)
        S.push(2)
        S.push(4)
        S.push(0)
        a = S.pop()
        b = S.pop()

        self.assertEqual(a, 0)
        self.assertEqual(b, 4)
"""
    def test_peek(self):
        #S = stack.Stack()
        S = Stack()
        S.push("hello")
        S.push("hi")
        self.assertEqual(S.peek(),"hi")
        S.pop()
"""