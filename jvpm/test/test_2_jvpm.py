import unittest
from unittest.mock import mock_open, patch, Mock, call

from stack import Stack
from jvpm_methods import OpCodeMethods
from jvpm_opcodes import OpCodes

import jvpm_dict
import jvpm_opcodes
import jvpm_methods
import sys

################################################################################
#cj branch start of test_2                                                     #
################################################################################

class Test_More_Jvpm_opcodes (unittest.TestCase):

    def test_dict_search(self):
        a = OpCodeMethods()
        l = OpCodes()

        l.opcodes =['06', '3c', '04', '3d', '1b', '1c', '82', '3e'] # Testing some op codes
        a.VARIABLES.append(0) # adding random constants to test methods \/
        a.VARIABLES.append(1)
        a.VARIABLES.append(2)
        a.VARIABLES.append(3)
        a.VARIABLES.append(4)
        a.VARIABLES.append(5)

        sys.stdout = unittest.mock.Mock()
        l.dict_search(a)
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

    def test_iload_0(self):
        a = OpCodeMethods()
        a.VARIABLES.append(7)
        a.VARIABLES.append(5)
        a.VARIABLES.append(6)
        a.VARIABLES.append(1)
        a.VARIABLES[0] = 2
        a.iload_0()
        b = a.stack.peek()
        self.assertEqual(b, 2)

    def test_iload_1(self):
        a = OpCodeMethods()
        a.VARIABLES.append(7)
        a.VARIABLES.append(5)
        a.VARIABLES.append(6)
        a.VARIABLES.append(1)
        a.VARIABLES[1] = 5
        a.iload_1()
        b = a.stack.peek()
        self.assertEqual(b, 5)

    def test_iload_2(self):
        a = OpCodeMethods()
        a.VARIABLES.append(7)
        a.VARIABLES.append(5)
        a.VARIABLES.append(6)
        a.VARIABLES.append(1)
        del a.VARIABLES[2]
        a.VARIABLES[2] = 7
        a.iload_2()
        b = a.stack.peek()
        self.assertEqual(b, 7)

    def test_iload_3(self):
        a = OpCodeMethods()
        a.VARIABLES.append(7)
        a.VARIABLES.append(5)
        a.VARIABLES.append(6)
        a.VARIABLES.append(1)
        a.VARIABLES.append(10)
        del a.VARIABLES[3]
        a.VARIABLES[3] = 9
        a.iload_3()
        b = a.stack.peek()
        self.assertEqual(b, 9)

    def test_istore_0(self):
        a = OpCodeMethods()
        a.stack.push(3)
        a.istore_0()
        b = a.VARIABLES[0]
        self.assertEqual(b, 3)

    def test_istore_1(self):
        a = OpCodeMethods()
        a.stack.push(2)
        a.stack.push(4)
        a.istore_0()
        a.istore_1()
        b = a.VARIABLES[1]
        self.assertEqual(b, 2)

    def test_istore_2(self):
        a = OpCodeMethods()
        a.stack.push(8)
        a.stack.push(7)
        a.stack.push(9)
        a.istore_0()
        a.istore_1()
        a.istore_2()
        b = a.VARIABLES[2]
        self.assertEqual(b, 8)

    def test_istore_3(self):
        a = OpCodeMethods()
        a.stack.push(9)
        a.stack.push(10)
        a.stack.push(3)
        a.stack.push(4)
        a.istore_0()
        a.istore_1()
        a.istore_2()
        a.istore_3()
        b = a.VARIABLES[3]
        self.assertEqual(b, 9)