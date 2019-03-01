import unittest
import sys
sys.path.append("/Users/zack/Documents/GitConfused/jvpm")
import stack

class TestStack(unittest.TestCase):
    #def setUp(self):

    def test_is_empty(self):
        S = stack.Stack()
        S.push(3)
        S.pop()
        self.assertTrue(S.is_empty())
