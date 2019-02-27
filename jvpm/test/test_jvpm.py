import unittest
from unittest.mock import mock_open, patch

import jvpm_dict
import jvpm_opcodes
import stack


class UnittestHeader(unittest.TestCase):

    def setUp(self):
        m = mock_open(read_data='CAFEBABE00000036000F')
        with patch(__name__ + '.open', m):
            self.cf = jvpm_opcodes.HeaderClass()

    def test_magic(self):
        self.assertEqual(self.cf.pull_magic(), 'cafebabe')
        self.assertEqual(self.cf.pull_minor(), 0)
        self.assertEqual(self.cf.pull_major(), 54)
        self.assertEqual(self.cf.pull_const_pool_count(), 14)



class test_get_opcode(unittest.TestCase):
    def test_opcode(self):
        self.assertEqual(jvpm_dict.get_opcode("91"), "i2b")
        self.assertEqual(jvpm_dict.get_opcode("82"), "ixor")
        self.assertEqual(jvpm_dict.get_opcode("1c"), "iload_2")
        self.assertEqual(jvpm_dict.get_opcode("03"), "iconst_0")

"""
class test_stack(unittest.TestCase):
    #def test_is_empty(self):
    #    self.assertTrue(stack.Stack.is_empty())

    def test_push(self):
        s = stack()
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop, 3)

"""
