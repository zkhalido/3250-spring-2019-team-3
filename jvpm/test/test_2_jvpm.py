import unittest
from unittest.mock import mock_open, patch, Mock, call

from stack import Stack
from jvpm_methods import OpCodeMethods
from jvpm_opcodes import OpCodes

import jvpm_dict
import jvpm_opcodes
import jvpm_methods
import sys


class UnittestHeader(unittest.TestCase):


    def setUp(self):
        m = mock_open(read_data='CAFEBABE00000036000F')
        with patch(__name__ + '.open', m):
            self.cf = jvpm_opcodes.HeaderClass()

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')
        self.assertEqual(self.cf.get_minor(), 0)
        self.assertTrue(53 <= self.cf.get_major() <= 55)
        self.assertEqual(self.cf.get_const_pool_count(), 15)




class test_get_opcode(unittest.TestCase):
    def test_opcode(self):
        self.assertEqual(jvpm_dict.get_opcode("91"), "i2b")
        self.assertEqual(jvpm_dict.get_opcode("82"), "ixor")
        self.assertEqual(jvpm_dict.get_opcode("1c"), "iload_2")
        self.assertEqual(jvpm_dict.get_opcode("03"), "iconst_0")
        # going to have an issue with items not in dictionary need a condition if item not in dictionary


class test_stack(unittest.TestCase):
    #def test_is_empty(self):
    #    self.assertTrue(stack.Stack.is_empty())

    def test_push(self):
        s = Stack()
        s.push(2)
        s.push(3)
        v= s.pop()
        self.assertEqual(v, 3)

    def test_pop(self):
        s = Stack()
        s.push(3)
        s.push(2)
        s.push(4)
        s.push(0)
        a = s.pop()
        b = s.pop()

        self.assertEqual(a, 0)
        self.assertEqual(b, 4)

    def test_pop(self):
        s = Stack()
        s.push(3)
        s.push(2)
        s.push(4)
        s.push(0)
        a = s.pop()
        b = s.pop()

        self.assertEqual(a, 0)
        self.assertEqual(b, 4)

    def test_peek(self):
        s = Stack()
        s.push("hello")
        s.push("hi")
        self.assertEqual(s.peek(),"hi")
        s.pop()

    def test_size(self):
        s = Stack()
        s.push("hello")
        s.push(2)
        s.push("hi")
        self.assertEqual(s.size(), 3)
        s.pop()
        self.assertEqual(s.size(), 2)

class Test_Op_Methods(unittest.TestCase):

    def test_iadd(self):
        a = OpCodeMethods()

        a.stack.push(2)
        a.stack.push(1)
        a.iadd()
        b = a.stack.pop()
        self.assertEqual(b, 3)

################################################################################
#cj branch start of test_2                                                     #
################################################################################

class Test_More_Jvpm_opcodes (unittest.TestCase):

    def test_dict_search(self):

        L = jvpm_opcodes.OpCodes()
        L.opcodes =['06', '3c', '04', '3d', '1b', '1c', '82', '3e']
        sys.stdout = unittest.mock.Mock()
        L.dict_search(self)
        sys.stdout.assert_has_calls(

            [call.write('iconst_3'), call.write('\n'),
            call.write('ran iconst_3'), call.write('\n'),
            call.write('istore_1'), call.write('\n'),
            call.write('ran istore_1'), call.write('\n'),
            call.write('iconst_1'), call.write('\n'),
            call.write('ran iconst_1'), call.write('\n'),
            call.write('istore_2'), call.write('\n'),
            call.write('ran istore_2'), call.write('\n'),
            call.write('iload_1'), call.write('\n'),
            call.write('ran iload_1'), call.write('\n'),
            call.write('iload_2'), call.write('\n'),
            call.write('ran iload_2'), call.write('\n'),
            call.write('ixor'), call.write('\n'),
            call.write('ran ixor'), call.write('\n'),
            call.write('istore_3'), call.write('\n'),
            call.write('ran istore_3'), call.write('\n'), call.write('\n')]
        )

    #def test_iand(self):




