import unittest
from unittest.mock import mock_open, patch

from stack import Stack

from jvpm_methods import OpCodeMethods

import jvpm_dict
import jvpm_opcodes


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
        self.assertEqual(jvpm_dict.get_opcode("SQ"), "Byte code not found!")


class test_stack(unittest.TestCase):
    def test_is_empty(self):
        s = Stack()
        s.push(1)
        s.pop()
        self.assertTrue(s.is_empty())

    def test_push(self):
        s = Stack()
        s.push(2)
        s.push(3)
        v = s.pop()
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

    def test_iand(self):
        a = OpCodeMethods()
        
        a.stack.push(5)
        a.stack.push(3)
        a.iand()
        b = a.stack.pop()
        self.assertEqual(b,1)

    def test_iconst_m1(self):
        a = OpCodeMethods()

        a.iconst_m1()
        b = a.stack.peek()
        self.assertEqual(b, -1)

        a.stack.push(5)
        self.assertEqual(a.stack.peek(), 5)
        self.assertNotEqual(a.stack.peek(), -1)

    def test_iconst_0(self):
        a = OpCodeMethods()

        a.iconst_0()
        b = a.stack.peek()
        self.assertEqual(b, 0)

        a.stack.push(5)
        self.assertEqual(a.stack.peek(), 5)
        self.assertNotEqual(a.stack.peek(), 0)

    def test_iconst_1(self):
        a = OpCodeMethods()

        a.iconst_1()
        b = a.stack.peek()
        self.assertEqual(b, 1)

        a.stack.push(5)
        self.assertEqual(a.stack.peek(), 5)
        self.assertNotEqual(a.stack.peek(), 1)

    def test_iconst_2(self):
        a = OpCodeMethods()

        a.iconst_2()
        b = a.stack.peek()
        self.assertEqual(b, 2)

        a.stack.push(5)
        self.assertEqual(a.stack.peek(), 5)
        self.assertNotEqual(a.stack.peek(), 2)

    def test_iconst_3(self):
        a = OpCodeMethods()

        a.iconst_3()
        b = a.stack.peek()
        self.assertEqual(b, 3)

        a.stack.push(5)
        self.assertEqual(a.stack.peek(), 5)
        self.assertNotEqual(a.stack.peek(), 3)

    def test_iconst_4(self):
        a = OpCodeMethods()

        a.iconst_4()
        b = a.stack.peek()
        self.assertEqual(b, 4)

        a.stack.push(5)
        self.assertEqual(a.stack.peek(), 5)
        self.assertNotEqual(a.stack.peek(), 4)

    def test_iconst_5(self):
        a = OpCodeMethods()

        a.iconst_5()
        b = a.stack.peek()
        self.assertEqual(b, 5)

        a.stack.push(2)
        self.assertEqual(a.stack.peek(), 2)
        self.assertNotEqual(a.stack.peek(), 5)

    def test_idiv(self):
        a = OpCodeMethods()

        a.stack.push(4)
        a.stack.push(2)
        a.idiv()
        b = a.stack.pop()
        self.assertEqual(b, 2)

        a.stack.push(6)
        a.stack.push(-2)
        a.idiv()
        b = a.stack.pop()
        self.assertEqual(b, -3)

        a.stack.push(-6)
        a.stack.push(-2)
        a.idiv()
        b = a.stack.pop()
        self.assertEqual(b, 3)

    #def test_iload_0(self):

    #def test_iload_1(self):

    #def test_iload_2(self):

    #def test_iload_3(self):

    def test_imul(self):
        a = OpCodeMethods()

        a.stack.push(3)
        a.stack.push(4)
        a.imul()
        b = a.stack.pop()
        self.assertEqual(b, 12)

        a.stack.push(-2)
        a.stack.push(3)
        a.imul()
        b = a.stack.pop()
        self.assertEqual(b, -6)

        a.stack.push(-5)
        a.stack.push(-4)
        a.imul()
        b = a.stack.pop()
        self.assertEqual(b, 20)

    def test_ineg(self):
        a = OpCodeMethods()

        a.stack.push(3)
        a.ineg()
        b = a.stack.pop()
        self.assertEqual(b, -3)

        a.stack.push(-5)
        a.ineg()
        b = a.stack.pop()
        self.assertEqual(b, 5)

    def test_ior(self):
        a = OpCodeMethods()

        a.stack.push(2)
        a.stack.push(5)
        a.ior()
        b = a.stack.pop()
        self.assertEqual(b, 7)

        a.stack.push(8)
        a.stack.push(2)
        a.ior()
        b = a.stack.pop()
        self.assertEqual(b, 10)

        a.stack.push(10)
        a.stack.push(-3)
        a.ior()
        b = a.stack.pop()
        self.assertEqual(b, -1)

        a.stack.push(-5)
        a.stack.push(-6)
        a.ior()
        b = a.stack.pop()
        self.assertEqual(b, -5)

    def test_irem(self):
        a = OpCodeMethods()

        a.stack.push(5)
        a.stack.push(2)
        a.irem()
        b = a.stack.pop()
        self.assertEqual(b, 1)

        a.stack.push(10)
        a.stack.push(5)
        a.irem()
        b = a.stack.pop()
        self.assertEqual(b, 0)

        a.stack.push(-6)
        a.stack.push(5)
        a.irem()
        b = a.stack.pop()
        self.assertEqual(b, 4)

        a.stack.push(6)
        a.stack.push(-6)
        a.irem()
        b = a.stack.pop()
        self.assertEqual(b, 0)

    def test_ishl(self):
        a = OpCodeMethods()
        
        a.stack.push(2)
        a.stack.push(1)
        a.ishl()
        b = a.stack.pop()
        self.assertEqual(b, 4)
    """
    def test_ishr(self):
        a = OpCodeMethods()
        
        a.stack.push(3)
        a.stack.push(1)
        a.ishr()
        b = a.stack.pop()
        self.assertEqual(b, 2)
        
        a.stack.push(-1)
        a.stack.push(1)
        a.ishr()
        b = a.stack.pop()
        self.asertEqual(b, -1)
        
        a.stack.push(5)
        a.stack.push(0)
        a.ishr()
        b = a.stack.pop()
        self.assertEqual(b, 5)
        
        a.stack.push(0)
        a.stack.push(5)
        a.ishr()
        b = a.stack.pop()
        self.assertEqual(b, 0)
    """
    #def test_istore_0(self):

    #def test_istore_1(self):

    #def test_istore_2(self):

    #def test_istore_3(self):

    def test_isub(self):
        a = OpCodeMethods()

        a.stack.push(5)
        a.stack.push(2)
        a.isub()
        b = a.stack.pop()
        self.assertEqual(b, 3)

        a.stack.push(5)
        a.stack.push(5)
        a.isub()
        b = a.stack.pop()
        self.assertEqual(b, 0)

        a.stack.push(5)
        a.stack.push(0)
        a.isub()
        b = a.stack.pop()
        self.assertEqual(b, 5)

        a.stack.push(0)
        a.stack.push(0)
        a.isub()
        b = a.stack.pop()
        self.assertEqual(b, 0)

        a.stack.push(3)
        a.stack.push(5)
        a.isub()
        b = a.stack.pop()
        self.assertEqual(b, -2)
    """
    def test_iushr(self):
        a = OpCodeMethods()
        
        a.stack.push(5)
        a.stack.push(2)
        a.iushr()
        b = a.stack.pop()
        self.assertEqual(b, 1)
        
        a.stack.push(-1)
        a.stack.push(2)
        a.iushr()
        b = a.stack.pop()
        self.assertEqual(b, 3)
    """
    """
    def test_ixor(self):
        a = OpCodeMethods()
        
        a.stack.push(5)
        a.stack.push(3)
        a.ixor()
        b = a.stack.pop()
        self.assertEqual(b, 7)
    """