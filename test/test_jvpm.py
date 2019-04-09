import unittest
from unittest.mock import mock_open, patch, call
from jvpm import packages
import sys
from collections import deque, defaultdict


class UnittestHeader(unittest.TestCase):

    def setUp(self):
        m = mock_open(read_data='CAFEBABE00000036000F')
        with patch(__name__ + '.open', m):
            self.cf = packages.jvpm_opcodes.HeaderClass()

#     def test_magic(self):
#         self.assertEqual(self.cf.get_magic(), 'CAFEBABE')
#         self.assertEqual(self.cf.get_minor(), 0)
#         self.assertTrue(53 <= self.cf.get_major() <= 55)
#         self.assertEqual(self.cf.get_const_pool_count(), 42)

class test_get_opcode(unittest.TestCase):
    def test_opcode(self):
        self.assertEqual(packages.jvpm_dict.get_opcode("91"), "i2b")
        self.assertEqual(packages.jvpm_dict.get_opcode("82"), "ixor")
        self.assertEqual(packages.jvpm_dict.get_opcode("1c"), "iload_2")
        self.assertEqual(packages.jvpm_dict.get_opcode("03"), "iconst_0")
        self.assertEqual(packages.jvpm_dict.get_opcode("SQ"), "Byte code not found!")

        ####################################################
# class test_const_pool(unittest.TestCase):
#     def test_const_pool(self):
#         with open('jvpm/javafiles/test.class', 'rb') as binary_file:
#             self.data = binary_file.read()

#         x = packages.jvpm_opcodes.HeaderClass()
#         x.data = self.data
#         n = x.get_const_pool()

#         new_dict = {

#              0: ['0a', '05', '13'],
#              1: ['09', '14', '15'],
#              2: ['0a', '16', '17'],
#              3: ['07', '18'], 4: ['07', '19'],
#              5: ['01', '06', '3c', '69', '6e', '69', '74', '3e'],
#              6: ['01', '03', '28', '29', '56'],
#              7: ['01', '04', '43', '6f', '64', '65'],
#              8: ['01', '0f', '4c', '69', '6e', '65', '4e', '75', '6d', '62', '65', '72', '54', '61', '62', '6c', '65'],
#              9: ['01', '12', '4c', '6f', '63', '61', '6c', '56', '61', '72', '69', '61', '62', '6c', '65', '54', '61', '62','6c', '65'],
#              10: ['01', '04', '74', '68', '69', '73'],
#              11: ['01', '0c', '4c','48', '65', '6c', '6c', '6f', '57', '6f', '72','6c', '64', '3b'],
#              12: ['01', '04', '6d', '61', '69', '6e'],
#              13: ['01', '16', '28', '5b', '4c', '6a', '61', '76', '61', '2f', '6c', '61','6e', '67', '2f', '53', '74', '72', '69', '6e', '67', '3b', '29', '56'],
#              14: ['01', '04', '61', '72', '67', '73'],
#              15: ['01', '13', '5b', '4c', '6a', '61', '76', '61', '2f', '6c', '61','6e', '67', '2f', '53', '74', '72', '69', '6e', '67', '3b'],
#              16: ['01', '0a', '53', '6f', '75', '72', '63', '65', '46', '69', '6c', '65'],
#              17: ['01', '0f', '48', '65', '6c', '6c', '6f','57', '6f', '72', '6c', '64', '2e', '6a', '61', '76', '61'],
#              18: ['0c', '06', '07'],
#              19: ['07', '1a'],
#              20: ['0c', '1b', '1c'],
#              21: ['07', '1d'],
#              22: ['0c', '1e', '1f'],
#              23: ['01', '0a','48', '65', '6c', '6c', '6f', '57','6f', '72', '6c', '64'],
#              24: ['01', '10', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '4f', '62', '6a', '65', '63','74'],
#              25: ['01','10', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '53', '79', '73', '74','65', '6d'],
#              26: ['01', '03', '6f', '75', '74'],
#              27: ['01', '15', '4c', '6a', '61', '76', '61','2f', '69', '6f', '2f', '50', '72', '69', '6e', '74', '53', '74', '72', '65', '61', '6d', '3b'],
#              28: ['01', '13', '6a', '61', '76', '61', '2f', '69', '6f', '2f', '50', '72', '69', '6e','74', '53', '74', '72', '65', '61', '6d'],
#              29: ['01', '07', '70', '72', '69', '6e', '74', '6c', '6e'],
#              30: ['01', '04', '28', '49', '29', '56']
#         }

#         self.assertEqual(n, new_dict)

        #################################################

class test_pool_translate1(unittest.TestCase):
    #def setUp(self):
        #f = mock_open(read_data='cafebabe0000003700160a000300130700140700150100063c696e69743e010003282956010004436f646501000f4c696e654e756d6265725461626c650100124c6f63616c5661726961626c655461626c65010004746869730100084c7465737465723b0100046d61696e010016285b4c6a6176612f6c616e672f537472696e673b2956010004617267730100135b4c6a6176612f6c616e672f537472696e673b010001610100014901000a536f7572636546696c6501000b7465737465722e6a6176610c000400050100067465737465720100106a6176612f6c616e672f4f626a656374002000020003000000000002000000040005000100060000002f00010001000000052ab70001b10000000200070000000600010000000100080000000c0001000000050009000a00000008000b000c000100060000003a0001000200000006053c840101b100000002000700000006000100000001000800000016000200000006000d000e000000020004000f0010000100010011000000020012')
        #with patch(__name__ + '.open', f):
        #    self.bf = jvpm.jvpm_opcodes.HeaderClass()

     def test_working_methods(self):
         jvpm_opcodes_obj = packages.jvpm_opcodes.HeaderClass(name="jvpm/javafiles/tester.class")

         #x = packages.jvpm_opcodes.HeaderClass()
         #z = patch.get_const_pool()
         #y = packages.pool_translate.PoolTranslate()
         y = packages.pool_translate.PoolTranslate(name ="jvpm/javafiles/tester.class")

         #y.dictionary = x.get_const_pool()
         b = defaultdict(list)
         b = jvpm_opcodes_obj.get_const_pool()

         a = {
             0: ['0a', '03', '13'],
             1: ['07', '14'],
             2: ['07', '15'],
             3: ['01', '06', '3c', '69', '6e', '69', '74', '3e'],
             4: ['01', '03', '28', '29', '56'], 5: ['01', '04', '43', '6f', '64', '65'],
             6: ['01', '0f', '4c', '69', '6e', '65', '4e', '75', '6d', '62', '65', '72', '54', '61', '62', '6c', '65'],
             7: ['01', '12', '4c', '6f', '63', '61', '6c', '56', '61', '72', '69', '61', '62', '6c', '65', '54', '61', '62', '6c', '65'],
             8: ['01', '04', '74', '68', '69', '73'],
             9: ['01', '08', '4c', '74', '65', '73', '74', '65', '72', '3b'],
             10: ['01', '04', '6d', '61', '69', '6e'],
             11: ['01', '16', '28', '5b', '4c', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '53', '74', '72', '69', '6e', '67', '3b', '29', '56'],
             12: ['01', '04', '61', '72', '67', '73'],
             13: ['01', '13', '5b', '4c', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '53', '74', '72', '69', '6e', '67', '3b'],
             14: ['01', '01', '61'],
             15: ['01', '01', '49'],
             16: ['01', '0a', '53', '6f', '75', '72', '63', '65', '46', '69', '6c', '65'],
             17: ['01', '0b', '74', '65', '73', '74', '65', '72', '2e', '6a', '61', '76', '61'],
             18: ['0c', '04', '05'],
             19: ['01', '06', '74', '65', '73', '74', '65', '72'],
             20: ['01', '10', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '4f', '62', '6a', '65', '63', '74']
         }

         new_dict = y.translate()

         n = {
             0: ['0a', '03', '13', 'java/lang/Object.<init>:()V'],
             1: ['07', '14', 'tester'],
             2: ['07', '15', 'java/lang/Object'],
             3: ['01', '06', '3c', '69', '6e', '69', '74', '3e', '<init>'],
             4: ['01', '03', '28', '29', '56', '()V'],
             5: ['01','04', '43', '6f','64', '65', 'Code'],
             6: ['01', '0f', '4c', '69', '6e', '65', '4e', '75', '6d', '62', '65', '72', '54', '61', '62', '6c', '65', 'LineNumberTable'],
             7: ['01', '12', '4c', '6f', '63', '61', '6c', '56', '61', '72', '69', '61', '62', '6c', '65', '54', '61', '62', '6c', '65', 'LocalVariableTable'],
             8: ['01', '04', '74', '68', '69', '73', 'this'],
             9: ['01', '08', '4c', '74', '65', '73', '74', '65', '72', '3b', 'Ltester;'],
             10: ['01', '04', '6d', '61', '69', '6e', 'main'],
             11: ['01', '16', '28', '5b', '4c', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '53', '74', '72', '69', '6e', '67', '3b', '29', '56', '([Ljava/lang/String;)V'],
             12: ['01', '04', '61', '72', '67', '73', 'args'],
             13: ['01', '13', '5b', '4c', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '53', '74', '72', '69', '6e', '67', '3b', '[Ljava/lang/String;'],
             14: ['01', '01', '61', 'a'],
             15: ['01', '01', '49', 'I'],
             16: ['01', '0a', '53', '6f', '75', '72', '63', '65', '46', '69', '6c','65', 'SourceFile'],
             17: ['01', '0b', '74', '65', '73', '74', '65', '72', '2e', '6a', '61', '76', '61', 'tester.java'],
             18: ['0c', '04', '05', '<init>:()V'],
             19: ['01', '06', '74', '65', '73', '74', '65', '72', 'tester'],
             20: ['01', '10', '6a', '61', '76', '61', '2f', '6c', '61', '6e', '67', '2f', '4f', '62', '6a', '65', '63', '74', 'java/lang/Object']

         }
         self.assertEqual(new_dict, n)

         self.assertEqual(new_dict[0], n[0])
         self.assertEqual(new_dict[1], n[1])
         self.assertEqual(new_dict[2], n[2])
         self.assertEqual(new_dict[3], n[3])
         self.assertEqual(new_dict[4], n[4])
         self.assertEqual(new_dict[5], n[5])
         self.assertEqual(new_dict[6], n[6])
         self.assertEqual(new_dict[7], n[7])
         self.assertEqual(new_dict[8], n[8])
         self.assertEqual(new_dict[9], n[9])
         self.assertEqual(new_dict[10], n[10])
         self.assertEqual(new_dict[11], n[11])
         self.assertEqual(new_dict[12], n[12])
         self.assertEqual(new_dict[13], n[13])
         self.assertEqual(new_dict[14], n[14])
         self.assertEqual(new_dict[15], n[15])
         self.assertEqual(new_dict[16], n[16])
         self.assertEqual(new_dict[17], n[17])
         self.assertEqual(new_dict[18], n[18])
         self.assertEqual(new_dict[19], n[19])
         self.assertEqual(new_dict[20], n[20])


         #self.assertEqual(y.method_handle(), "Method Handle    3 bytes")
         self.assertEqual(new_dict[20], n[20])
         self.assertEqual(new_dict[20], n[20])
         self.assertEqual(new_dict[20], n[20])
         self.assertEqual(new_dict[20], n[20])
         self.assertEqual(new_dict[20], n[20])
         self.assertEqual(new_dict[20], n[20])
         self.assertEqual(new_dict[20], n[20])

class test_pool_methods(unittest.TestCase):
    def test_tag_translate(self):
         new_dict = {
             "1": "01",
             "2": "03",
             "3": "04",
             "4": "05",
             "5": "06",
             "6": "07",
             "7": "08",
             "8": "09",
             "9": "0a",
             "10": "0b",
             "11": "0c",
             "12": "0f",
             "13": "10",
             "14": "11",
             "15": "12",
             "16": "13",
             "17": "14"
         }
         x = packages.pool_translate.PoolTranslate(name ="jvpm/javafiles/tester.class")
         #x.dictionary = {
         #    '0':"0"
         #}
         """
         x.field_reference()
         sys.stdout.assert_has_calls(
             [call.write("Field Reference    4 bytes")]
         )
         """
         x.integer()
         sys.stdout.assert_has_calls(
             [call.write("Integer  4 bytes")]
         )
         x.float()
         sys.stdout.assert_has_calls(
            [call.write("Float  4 bytes")]
         )
         x.long()
         sys.stdout.assert_has_calls(
             [call.write("Long    8 bytes")]
         )
         x.double()
         sys.stdout.assert_has_calls(
             [call.write("Double    8 bytes")]
         )
         x.interface_method_reference()
         sys.stdout.assert_has_calls(
             [call.write("Interface Method Reference    4 bytes")]
         )

         x.method_handle()
         sys.stdout.assert_has_calls(
             [call.write("Method Handle    3 bytes")]
         )

         x.method_type()
         sys.stdout.assert_has_calls(
             [call.write("Method Type    2 bytes")]
         )

         x.dynamic()
         sys.stdout.assert_has_calls(
             [call.write("Dynamic    4 bytes")]
         )
         x.invoke_dynamic()
         sys.stdout.assert_has_calls(
             [call.write("Invoke Dynamic    4 bytes")]
         )
         x.module()
         sys.stdout.assert_has_calls(
             [call.write("Module    2 bytes")]
         )
         x.package()
         sys.stdout.assert_has_calls(
             [call.write("Package    2 bytes")]
         )


         x = packages.pool_methods.TagTranslate()
         self.assertEqual(x.token_dict(new_dict['1']), "UTF 8 String")
         self.assertEqual(x.token_dict(new_dict['2']), "Integer")
         self.assertEqual(x.token_dict(new_dict['3']), "Float")
         self.assertEqual(x.token_dict(new_dict['4']), "Long")
         self.assertEqual(x.token_dict(new_dict['5']), "Double")
         self.assertEqual(x.token_dict(new_dict['6']), "Class Reference")
         self.assertEqual(x.token_dict(new_dict['7']), "String Reference")
         self.assertEqual(x.token_dict(new_dict['8']), "Field Reference")
         self.assertEqual(x.token_dict(new_dict['9']), "Method Reference")
         self.assertEqual(x.token_dict(new_dict['10']), "Interface Method Reference")
         self.assertEqual(x.token_dict(new_dict['11']), "Name and Type")
         self.assertEqual(x.token_dict(new_dict['12']), "Method Handle")
         self.assertEqual(x.token_dict(new_dict['13']), "Method Type")
         self.assertEqual(x.token_dict(new_dict['14']), "Dynamic")
         self.assertEqual(x.token_dict(new_dict['15']), "Invoke Dynamic")
         self.assertEqual(x.token_dict(new_dict['16']), "Module")
         self.assertEqual(x.token_dict(new_dict['17']), "Package")

class test_stack(unittest.TestCase):
    def test_is_empty(self):
        s = packages.stack.Stack()
        s.push(1)
        s.pop()
        self.assertTrue(s.is_empty())

    def test_push(self):
        s = packages.stack.Stack()
        s.push(2)
        s.push(3)
        v = s.pop()
        self.assertEqual(v, 3)

    def test_pop(self):
        s = packages.stack.Stack()
        s.push(3)
        s.push(2)
        s.push(4)
        s.push(0)
        a = s.pop()
        b = s.pop()
        self.assertEqual(a, 0)
        self.assertEqual(b, 4)

    def test_peek(self):
        s = packages.stack.Stack()
        s.push("hello")
        s.push("hi")
        self.assertEqual(s.peek(),"hi")
        s.pop()

    def test_size(self):
        s = packages.stack.Stack()
        s.push("hello")
        s.push(2)
        s.push("hi")
        self.assertEqual(s.size(), 3)
        s.pop()
        self.assertEqual(s.size(), 2)

class Test_Op_Methods(unittest.TestCase):

    def test_iadd(self):
        a = packages.jvpm_methods.OpCodeMethods()
        # packages.jvpm_methods.S.push(1) EXAMPLE THAT I USED IN THE MAIN AND IT WORKS
        packages.jvpm_methods.S.push(2)
        packages.jvpm_methods.S.push(1)
        a.iadd()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 3)

    def test_iand(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(3)
        a.iand()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b,1)

    def test_iconst_m1(self):
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_m1()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, -1)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), -1)

    def test_iconst_0(self):
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_0()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 0)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 0)

    def test_iconst_1(self):
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_1()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 1)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 1)

    def test_iconst_2(self):
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_2()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 2)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 2)

    def test_iconst_3(self):
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_3()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 3)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 3)

    def test_iconst_4(self):
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_4()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 4)
        packages.jvpm_methods.S.push(5)
        self.assertEqual(packages.jvpm_methods.S.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 4)

    def test_iconst_5(self):
        a = packages.jvpm_methods.OpCodeMethods()
        a.iconst_5()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 5)
        packages.jvpm_methods.S.push(2)
        self.assertEqual(packages.jvpm_methods.S.peek(), 2)
        self.assertNotEqual(packages.jvpm_methods.S.peek(), 5)

    def test_idiv(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(4)
        packages.jvpm_methods.S.push(2)
        a.idiv()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 2.0)
        packages.jvpm_methods.S.push(6)
        packages.jvpm_methods.S.push(-2)
        a.idiv()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -3)
        packages.jvpm_methods.S.push(-6)
        packages.jvpm_methods.S.push(-2)
        a.idiv()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 3)

    def test_iload_0(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES[0] = 2
        a.iload_0()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 2)

    def test_iload_1(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.insert(0, 7)
        packages.jvpm_methods.VARIABLES.insert(1, 5)
#         a.VARIABLES.append(6)
#         a.VARIABLES.append(1)
#        a.VARIABLES[1] = 5
        a.iload_1()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 5)

    def test_iload_2(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        del packages.jvpm_methods.VARIABLES[2]
        packages.jvpm_methods.VARIABLES[2] = 7
        a.iload_2()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 7)

    def test_iload_3(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES.append(10)
        del packages.jvpm_methods.VARIABLES[3]
        packages.jvpm_methods.VARIABLES[3] = 9
        a.iload_3()
        b = packages.jvpm_methods.S.peek()
        self.assertEqual(b, 9)

    def test_imul(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(3)
        packages.jvpm_methods.S.push(4)
        a.imul()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 12)
        packages.jvpm_methods.S.push(-2)
        packages.jvpm_methods.S.push(3)
        a.imul()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -6)
        packages.jvpm_methods.S.push(-5)
        packages.jvpm_methods.S.push(-4)
        a.imul()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 20)   

    def test_ineg(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(3)
        a.ineg()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -3)
        packages.jvpm_methods.S.push(-5)
        a.ineg()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

    def test_ior(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(2)
        packages.jvpm_methods.S.push(5)
        a.ior()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 7)
        packages.jvpm_methods.S.push(8)
        packages.jvpm_methods.S.push(2)
        a.ior()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 10)
        packages.jvpm_methods.S.push(10)
        packages.jvpm_methods.S.push(-3)
        a.ior()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -1)
        packages.jvpm_methods.S.push(-5)
        packages.jvpm_methods.S.push(-6)
        a.ior()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -5)

    def test_irem(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(2)
        a.irem()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 1)

        packages.jvpm_methods.S.push(10)
        packages.jvpm_methods.S.push(5)
        a.irem()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

        packages.jvpm_methods.S.push(-6)
        packages.jvpm_methods.S.push(5)
        a.irem()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 4)

        packages.jvpm_methods.S.push(6)
        packages.jvpm_methods.S.push(-6)
        a.irem()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

    def test_ishl(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(2)
        packages.jvpm_methods.S.push(1)
        a.ishl()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 4)

    def test_ishr(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(3)
        packages.jvpm_methods.S.push(1)
        a.ishr()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 1)

        packages.jvpm_methods.S.push(-1)
        packages.jvpm_methods.S.push(1)
        a.ishr()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, -1)

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(0)
        a.ishr()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

        packages.jvpm_methods.S.push(0)
        packages.jvpm_methods.S.push(5)
        a.ishr()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

    def test_istore_0(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(3)
        a.istore_0()
        b = packages.jvpm_methods.VARIABLES[0]
        self.assertEqual(b, 3)

    def test_istore_1(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(2)
        packages.jvpm_methods.S.push(4)
        a.istore_0()
        a.istore_1()
        b = packages.jvpm_methods.VARIABLES[1]
        self.assertEqual(b, 2)

    def test_istore_2(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(8)
        packages.jvpm_methods.S.push(7)
        packages.jvpm_methods.S.push(9)
        a.istore_0()
        a.istore_1()
        a.istore_2()
        b = packages.jvpm_methods.VARIABLES[2]
        self.assertEqual(b, 8)

    def test_istore_3(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(9)
        packages.jvpm_methods.S.push(10)
        packages.jvpm_methods.S.push(3)
        packages.jvpm_methods.S.push(4)
        a.istore_0()
        a.istore_1()
        a.istore_2()
        a.istore_3()
        b = packages.jvpm_methods.VARIABLES[3]
        self.assertEqual(b, 9)

    def test_isub(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(2)
        a.isub()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 3)

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(5)
        a.isub()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(0)
        a.isub()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

        packages.jvpm_methods.S.push(0)
        packages.jvpm_methods.S.push(0)
        a.isub()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0)

    def test_iushr(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(2)
        a.iushr()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 1)
    """
        a.stack.push(-1)
        a.stack.push(2)
        a.iushr()
        b = a.stack.pop()
        self.assertEqual(b, 3)
    """

    def test_ixor(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        packages.jvpm_methods.S.push(3)
        a.ixor()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 6)    

    def test_i2f(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        a.i2f()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5.0)

        packages.jvpm_methods.S.push(0)
        a.i2f()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 0.0)

    def test_i2b(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        a.i2b()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, b'\x00\x00\x00\x00\x00\x00\x00\x05')

        packages.jvpm_methods.S.push(0)
        a.i2b()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, b'\x00\x00\x00\x00\x00\x00\x00\x00')

    def test_i2c(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(5)
        a.i2c()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, '\x05')

        packages.jvpm_methods.S.push(0)
        a.i2c()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, '\x00')

    def test_i2s(self):
        a = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.S.push(555555)
        a.i2s()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, "0x7a23")

        packages.jvpm_methods.S.push(000000)
        a.i2s()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, "0x0")

    def test_i2d(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(5)
        a.i2d()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

    def test_i2l(self):
        a = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.S.push(5)
        a.i2l()
        b = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)

    def test_dup(self):
        a = packages.jvpm_methods.OpCodeMethods()
        
        packages.jvpm_methods.S.push(5)
        a.dup()
        b = packages.jvpm_methods.S.pop()
        c = packages.jvpm_methods.S.pop()
        self.assertEqual(b, 5)
        self.assertEqual(c, 5)

    def test_dict_search(self):
        a = packages.jvpm_methods.OpCodeMethods()
        l = packages.jvpm_opcodes.OpCodes()

        l.opcodes =['06', '3c', '04', '3d', '1b', '1c', '82', '3e'] # Testing some op codes
        packages.jvpm_methods.VARIABLES.append(0) # adding random constants to test methods \/
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES.append(2)
        packages.jvpm_methods.VARIABLES.append(3)
        packages.jvpm_methods.VARIABLES.append(4)
        packages.jvpm_methods.VARIABLES.append(5)

        sys.stdout = unittest.mock.Mock()
        # l.dict_search()
#         sys.stdout.assert_has_calls(

#             [call.write('iconst_3'), call.write('\n'),
#             call.write('ran iconst_3'), call.write('\n'),
#             call.write('istore_1'), call.write('\n'),
#             call.write('ran istore_1'), call.write('\n'),
#             call.write('iconst_1'), call.write('\n'),
#             call.write('ran iconst_1'), call.write('\n'),
#             call.write('istore_2'), call.write('\n'),
#             call.write('ran istore_2'), call.write('\n'),
#             call.write('iload_1'), call.write('\n'),
#             call.write('ran iload_1'), call.write('\n'),
#             call.write('iload_2'), call.write('\n'),
#             call.write('ran iload_2'), call.write('\n'),
#             call.write('ixor'), call.write('\n'),
#             call.write('ran ixor'), call.write('\n'),
#             call.write('istore_3'), call.write('\n'),
#             call.write('ran istore_3'), call.write('\n'), call.write('\n')]
#         )
