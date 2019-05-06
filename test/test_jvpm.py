import unittest
from unittest.mock import mock_open, patch, call
from jvpm import packages
from bitstring import ConstBitStream
import numpy
import sys
from collections import deque, defaultdict


class UnittestHeader(unittest.TestCase):

    def setUp(self):
        m = mock_open(read_data='CAFEBABE00000036000F')
        with patch(__name__ + '.open', m):
            self.cf = packages.jvpm_opcodes.HeaderClass()

class test_get_opcode(unittest.TestCase):
    def test_opcode(self):
        self.assertEqual(packages.jvpm_dict.get_opcode("91"), "i2b")
        self.assertEqual(packages.jvpm_dict.get_opcode("82"), "ixor")
        self.assertEqual(packages.jvpm_dict.get_opcode("1c"), "iload_2")
        self.assertEqual(packages.jvpm_dict.get_opcode("03"), "iconst_0")
        self.assertEqual(packages.jvpm_dict.get_opcode("SQ"), "Byte code not found!")

class test_const_pool(unittest.TestCase):
    def test_const_pool(self):


        test_bits = ConstBitStream('0x070003' +
            '09001400020a001500200b0000b0060800280300100004' +
            '040300000f0506000012004c006f06030000'+
            '04007400680c050000080100046d61696e' +
            '0f0201601060041200135b4c')
        i = 1
        n = []
        while i <= 14:
            x = packages.CPInfo.ConstInfo().read(test_bits)
            n.append(x)
            i += 1

        a = {
            0: ['07', '03'],
            1: ['09', '14', '02'],
            2: ['0a', '15', '20'],
            3: ['0b', 'b0', '06'],
            4: ['08', '28'],
            5: ['03', '10', '04'],
            6: ['04', '03', '0f'],
            7: ['05', '06', '12', '4c', '6f'],
            8: ['06', '03', '04', '74', '68'],
            9: ['0c', '05', '08'],
            10: ['01', '00', '04', '6d', '61', '69', '6e'],
            11: ['0f', '02', '01', '60'],
            12: ['10', '60', '04'],
            13: ['12', '13', '5b', '4c']
        }

        self.assertEqual(n[0], a[0])
        self.assertEqual(n[1], a[1])
        self.assertEqual(n[2], a[2])
        self.assertEqual(n[3], a[3])
        self.assertEqual(n[4], a[4])
        self.assertEqual(n[5], a[5])
        self.assertEqual(n[6], a[6])
        self.assertEqual(n[7], a[7])
        self.assertEqual(n[8], a[8])
        self.assertEqual(n[9], a[9])
        self.assertEqual(n[10], a[10])
        self.assertEqual(n[11], a[11])
        self.assertEqual(n[12], a[12])
        self.assertEqual(n[13], a[13])



class test_pool_translate1(unittest.TestCase):

    def test_working_methods(self):
        jvpm_opcodes_obj = packages.jvpm_opcodes.HeaderClass(name="jvpm/javafiles/testSaveVar.class")
        jvpm_opcodes_obj.get_magic()
        jvpm_opcodes_obj.get_minor()
        jvpm_opcodes_obj.get_major()
        const_pool_test = jvpm_opcodes_obj.get_const_pool()
        translated_const_pool = packages.pool_translate.PoolTranslate(const_pool_test, jvpm_opcodes_obj.skips_in_constant_pool,
                                                                      name="jvpm/javafiles/testSaveVar.class")

        expected_trans_pool = ["0",
                     "java/lang/Object.<init>:()V",
                     "hello",
                     1002,
                     "0",
                     None,
                     "0",
                     "java/lang/System.out:Ljava/io/PrintStream;",
                     None,
                     "java/io/PrintStream.println:(Ljava/lang/String;)V",
                     "testSaveVar",
                     "java/lang/Object",
                     "<init>",
                     "()V",
                     "Code",
                     "LineNumberTable",
                     "LocalVariableTable",
                     "this",
                     "LtestSaveVar;",
                     "main",
                     "([Ljava/lang/String;)V",
                     "args",
                     "[Ljava/lang/String;",
                     "myInt",
                     "I",
                     "myString",
                     "Ljava/lang/String;",
                     "myLong",
                     "J",
                     "myDouble",
                     "D",
                     "SourceFile",
                     "testSaveVar.java",
                     "<init>:()V",
                     "hello",
                     "java/lang/System",
                     "out:Ljava/io/PrintStream;",
                     "BootstrapMethods",
                     None,
                     "\x01 \x01 \x01 \x01",
                     "makeConcatWithConstants:(ILjava/lang/String;JD)Ljava/lang/String;",
                     "java/io/PrintStream",
                     "println:(Ljava/lang/String;)V",
                     "testSaveVar",
                     "java/lang/Object",
                     "java/lang/System",
                     "out",
                     "Ljava/io/PrintStream;",
                     "java/lang/invoke/StringConcatFactory.makeConcatWithConstants:(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
                     "\x01 \x01 \x01 \x01",
                     "makeConcatWithConstants",
                     "(ILjava/lang/String;JD)Ljava/lang/String;",
                     "java/io/PrintStream",
                     "println",
                     "(Ljava/lang/String;)V",
                     "java/lang/invoke/StringConcatFactory",
                     "makeConcatWithConstants:(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
                     "java/lang/invoke/StringConcatFactory",
                     "java/lang/invoke/MethodHandles$Lookup",
                     "Lookup",
                     "InnerClasses",
                     "(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite;",
                     "java/lang/invoke/MethodHandles",
                     "java/lang/invoke/MethodHandles$Lookup",
                     "java/lang/invoke/MethodHandles"
                     ]

        new_dict = translated_const_pool.translate_pool()

        self.assertEqual(new_dict, expected_trans_pool)

class test_pool_methods(unittest.TestCase):
    def test_tag_translate(self):
         jvpm_opcodes_obj = packages.jvpm_opcodes.HeaderClass(name="jvpm/javafiles/tester.class")
         jvpm_opcodes_obj.get_magic()
         jvpm_opcodes_obj.get_minor()
         jvpm_opcodes_obj.get_major()
         const_pool_test = jvpm_opcodes_obj.get_const_pool()
         translated_const_pool = packages.pool_translate.PoolTranslate(const_pool_test, jvpm_opcodes_obj.skips_in_constant_pool,
                                                  name="jvpm/javafiles/tester.class")
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

         x_list = [0]



         translated_const_pool.interface_method_reference(x_list)

         translated_const_pool.method_handle(x_list)

         translated_const_pool.method_type(x_list)

         translated_const_pool.dynamic(x_list)

         translated_const_pool.invoke_dynamic(x_list)

         translated_const_pool.module(x_list)

         translated_const_pool.package(x_list)

         translated_const_pool = packages.pool_methods.TagTranslate()
         self.assertEqual(translated_const_pool.token_dict(new_dict['1']), "UTF 8 String")
         self.assertEqual(translated_const_pool.token_dict(new_dict['2']), "Integer")
         self.assertEqual(translated_const_pool.token_dict(new_dict['3']), "Float")
         self.assertEqual(translated_const_pool.token_dict(new_dict['4']), "Long")
         self.assertEqual(translated_const_pool.token_dict(new_dict['5']), "Double")
         self.assertEqual(translated_const_pool.token_dict(new_dict['6']), "Class Reference")
         self.assertEqual(translated_const_pool.token_dict(new_dict['7']), "String Reference")
         self.assertEqual(translated_const_pool.token_dict(new_dict['8']), "Field Reference")
         self.assertEqual(translated_const_pool.token_dict(new_dict['9']), "Method Reference")
         self.assertEqual(translated_const_pool.token_dict(new_dict['10']), "Interface Method Reference")
         self.assertEqual(translated_const_pool.token_dict(new_dict['11']), "Name and Type")
         self.assertEqual(translated_const_pool.token_dict(new_dict['12']), "Method Handle")
         self.assertEqual(translated_const_pool.token_dict(new_dict['13']), "Method Type")
         self.assertEqual(translated_const_pool.token_dict(new_dict['14']), "Dynamic")
         self.assertEqual(translated_const_pool.token_dict(new_dict['15']), "Invoke Dynamic")
         self.assertEqual(translated_const_pool.token_dict(new_dict['16']), "Module")
         self.assertEqual(translated_const_pool.token_dict(new_dict['17']), "Package")

class test_stack(unittest.TestCase):
    def test_is_empty(self):
        stack = packages.stack.Stack()
        stack.push(1)
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_push(self):
        stack = packages.stack.Stack()
        stack.push(2)
        stack.push(3)
        popped_var = stack.pop()
        self.assertEqual(popped_var, 3)

    def test_pop(self):
        stack = packages.stack.Stack()
        stack.push(3)
        stack.push(2)
        stack.push(4)
        stack.push(0)
        popped_var_1 = stack.pop()
        popped_var_2 = stack.pop()
        self.assertEqual(popped_var_1, 0)
        self.assertEqual(popped_var_2, 4)

    def test_peek(self):
        stack = packages.stack.Stack()
        stack.push("hello")
        stack.push("hi")
        self.assertEqual(stack.peek(),"hi")
        stack.pop()

    def test_size(self):
        stack = packages.stack.Stack()
        stack.push("hello")
        stack.push(2)
        stack.push("hi")
        self.assertEqual(stack.size(), 3)
        stack.pop()
        self.assertEqual(stack.size(), 2)

class test_op_methods(unittest.TestCase):

    def test_iadd(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(2)
        packages.jvpm_methods.Stack.push(1)
        opcode_test.iadd(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 3)
        packages.jvpm_methods.Stack.push(2.1)
        packages.jvpm_methods.Stack.push(1.2)
        opcode_test.iadd(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 3.3)

    def test_iand(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(5)
        packages.jvpm_methods.Stack.push(3)
        opcode_test.iand(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 1)

    def test_iconst_m1(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        opcode_test.iconst_m1(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, -1)
        packages.jvpm_methods.Stack.push(5)
        self.assertEqual(packages.jvpm_methods.Stack.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.Stack.peek(), -1)

    def test_iconst_0(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        opcode_test.iconst_0(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 0)
        packages.jvpm_methods.Stack.push(5)
        self.assertEqual(packages.jvpm_methods.Stack.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.Stack.peek(), 0)

    def test_iconst_1(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        opcode_test.iconst_1(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 1)
        packages.jvpm_methods.Stack.push(5)
        self.assertEqual(packages.jvpm_methods.Stack.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.Stack.peek(), 1)

    def test_iconst_2(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        opcode_test.iconst_2(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 2)
        packages.jvpm_methods.Stack.push(5)
        self.assertEqual(packages.jvpm_methods.Stack.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.Stack.peek(), 2)

    def test_iconst_3(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        opcode_test.iconst_3(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 3)
        packages.jvpm_methods.Stack.push(5)
        self.assertEqual(packages.jvpm_methods.Stack.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.Stack.peek(), 3)

    def test_iconst_4(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        opcode_test.iconst_4(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 4)
        packages.jvpm_methods.Stack.push(5)
        self.assertEqual(packages.jvpm_methods.Stack.peek(), 5)
        self.assertNotEqual(packages.jvpm_methods.Stack.peek(), 4)

    def test_iconst_5(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        opcode_test.iconst_5(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 5)
        packages.jvpm_methods.Stack.push(2)
        self.assertEqual(packages.jvpm_methods.Stack.peek(), 2)
        self.assertNotEqual(packages.jvpm_methods.Stack.peek(), 5)

    def test_idiv(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(4)
        packages.jvpm_methods.Stack.push(2)
        opcode_test.idiv(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(peeked_var, 2.0)
        packages.jvpm_methods.Stack.push(6)
        packages.jvpm_methods.Stack.push(-2)
        opcode_test.idiv(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(peeked_var, -3)
        packages.jvpm_methods.Stack.push(-6)
        packages.jvpm_methods.Stack.push(-2)
        opcode_test.idiv(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(peeked_var, 3)

    def test_iload_0(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES[0] = 2
        opcode_test.iload_0(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 2)

    def test_aload_0(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(0)
        opcode_test.aload_0(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 0)

    def test_iload_1(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.insert(0, 7)
        packages.jvpm_methods.VARIABLES.insert(1, 5)
        opcode_test.iload_1(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 5)

    def test_iload_2(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        del packages.jvpm_methods.VARIABLES[2]
        packages.jvpm_methods.VARIABLES[2] = 7
        opcode_test.iload_2(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 7)

    def test_iload_3(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.VARIABLES.append(7)
        packages.jvpm_methods.VARIABLES.append(5)
        packages.jvpm_methods.VARIABLES.append(6)
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES.append(10)
        del packages.jvpm_methods.VARIABLES[3]
        packages.jvpm_methods.VARIABLES[3] = 9
        opcode_test.iload_3(op, con, arg)
        peeked_var = packages.jvpm_methods.Stack.peek()
        self.assertEqual(peeked_var, 9)

    def test_imul(self):
        op = None
        con = None
        arg = None

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(3)
        packages.jvpm_methods.Stack.push(4)
        opcode_test.imul(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 12)
        packages.jvpm_methods.Stack.push(-2)
        packages.jvpm_methods.Stack.push(3)
        opcode_test.imul(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -6)
        packages.jvpm_methods.Stack.push(-5)
        packages.jvpm_methods.Stack.push(-4)
        opcode_test.imul(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 20)

    def test_ineg(self):
        op = None
        con = None
        arg = None

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(3)
        opcode_test.ineg(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -3)
        packages.jvpm_methods.Stack.push(-5)
        opcode_test.ineg(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 5)

    def test_ior(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(2)
        packages.jvpm_methods.Stack.push(5)
        opcode_test.ior(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 7)
        packages.jvpm_methods.Stack.push(8)
        packages.jvpm_methods.Stack.push(2)
        opcode_test.ior(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 10)
        packages.jvpm_methods.Stack.push(10)
        packages.jvpm_methods.Stack.push(-3)
        opcode_test.ior(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -1)
        packages.jvpm_methods.Stack.push(-5)
        packages.jvpm_methods.Stack.push(-6)
        opcode_test.ior(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -5)

    def test_irem(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(5)
        packages.jvpm_methods.Stack.push(2)
        opcode_test.irem(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 1)

        packages.jvpm_methods.Stack.push(10)
        packages.jvpm_methods.Stack.push(5)
        opcode_test.irem(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

        packages.jvpm_methods.Stack.push(-6)
        packages.jvpm_methods.Stack.push(5)
        opcode_test.irem(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 4)

        packages.jvpm_methods.Stack.push(6)
        packages.jvpm_methods.Stack.push(-6)
        opcode_test.irem(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

    def test_ishl(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(2)
        packages.jvpm_methods.Stack.push(1)
        opcode_test.ishl(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 4)

    def test_ishr(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(3)
        packages.jvpm_methods.Stack.push(1)
        opcode_test.ishr(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 1)

        packages.jvpm_methods.Stack.push(-1)
        packages.jvpm_methods.Stack.push(1)
        opcode_test.ishr(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -1)

        packages.jvpm_methods.Stack.push(5)
        packages.jvpm_methods.Stack.push(0)
        opcode_test.ishr(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 5)

        packages.jvpm_methods.Stack.push(0)
        packages.jvpm_methods.Stack.push(5)
        opcode_test.ishr(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

    def test_istore_0(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(3)
        opcode_test.istore_0(op, con, arg)
        array_var = packages.jvpm_methods.VARIABLES[0]
        self.assertEqual(array_var, 3)

    def test_istore_1(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(2)
        packages.jvpm_methods.Stack.push(4)
        opcode_test.istore_0(op, con, arg)
        opcode_test.istore_1(op, con, arg)
        array_var = packages.jvpm_methods.VARIABLES[1]
        self.assertEqual(array_var, 2)

    def test_istore_2(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(8)
        packages.jvpm_methods.Stack.push(7)
        packages.jvpm_methods.Stack.push(9)
        opcode_test.istore_0(op, con, arg)
        opcode_test.istore_1(op, con, arg)
        opcode_test.istore_2(op, con, arg)
        array_var = packages.jvpm_methods.VARIABLES[2]
        self.assertEqual(array_var, 8)

    def test_istore_3(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(9)
        packages.jvpm_methods.Stack.push(10)
        packages.jvpm_methods.Stack.push(3)
        packages.jvpm_methods.Stack.push(4)
        opcode_test.istore_0(op, con, arg)
        opcode_test.istore_1(op, con, arg)
        opcode_test.istore_2(op, con, arg)
        opcode_test.istore_3(op, con, arg)
        array_var = packages.jvpm_methods.VARIABLES[3]
        self.assertEqual(array_var, 9)

    def test_isub(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(5)
        packages.jvpm_methods.Stack.push(2)
        opcode_test.isub(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 3)

        packages.jvpm_methods.Stack.push(5)
        packages.jvpm_methods.Stack.push(5)
        opcode_test.isub(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

        packages.jvpm_methods.Stack.push(5)
        packages.jvpm_methods.Stack.push(0)
        opcode_test.isub(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 5)

        packages.jvpm_methods.Stack.push(0)
        packages.jvpm_methods.Stack.push(0)
        opcode_test.isub(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

    def test_iushr(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(5)
        packages.jvpm_methods.Stack.push(2)
        opcode_test.iushr(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 1)

    def test_ixor(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(5)
        packages.jvpm_methods.Stack.push(3)
        opcode_test.ixor(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 6)

    def test_i2f(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(5)
        opcode_test.i2f(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 5.0)

        packages.jvpm_methods.Stack.push(0)
        opcode_test.i2f(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0.0)

        packages.jvpm_methods.Stack.push(-1)
        opcode_test.i2f(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -1.0)

    def test_i2b(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(5)
        opcode_test.i2b(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, b'\x00\x00\x00\x00\x00\x00\x00\x05')

        packages.jvpm_methods.Stack.push(0)
        opcode_test.i2b(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, b'\x00\x00\x00\x00\x00\x00\x00\x00')

    def test_i2c(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(5)
        opcode_test.i2c(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, '\x05')

        packages.jvpm_methods.Stack.push(0)
        opcode_test.i2c(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, '\x00')

    def test_i2s(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(5)
        opcode_test.i2d(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 5)

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(0)
        opcode_test.i2d(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(-1)
        opcode_test.i2d(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -1)

    def test_i2d(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(5)
        opcode_test.i2d(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 5)

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(0)
        opcode_test.i2d(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(-1)
        opcode_test.i2d(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -1)

    def test_i2l(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(5)
        opcode_test.i2l(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 5)

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(0)
        opcode_test.i2l(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(-1)
        opcode_test.i2d(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -1)

    def test_i2s(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(5)
        opcode_test.i2s(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 5)

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(0)
        opcode_test.i2s(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, 0)

        opcode_test = packages.jvpm_methods.OpCodeMethods()
        packages.jvpm_methods.Stack.push(-1)
        opcode_test.i2d(op, con, arg)
        popped_var = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var, -1)

    def test_dup(self):
        op = None
        con = None
        arg = None
        opcode_test = packages.jvpm_methods.OpCodeMethods()

        packages.jvpm_methods.Stack.push(5)
        opcode_test.dup(op, con, arg)
        popped_var_1 = packages.jvpm_methods.Stack.pop()
        popped_var_2 = packages.jvpm_methods.Stack.pop()
        self.assertEqual(popped_var_1, 5)
        self.assertEqual(popped_var_2, 5)

    def test_dict_search(self):
        op = None
        con = None
        opcode_method_test = packages.jvpm_methods.OpCodeMethods()
        opcode_test = packages.jvpm_opcodes.OpCodes(op, con)

        opcode_test.opcodes =['06', '3c', '04', '3d', '1b', '1c', '82', '3e'] # Testing some op codes
        packages.jvpm_methods.VARIABLES.append(0) # adding random constants to test methods \/
        packages.jvpm_methods.VARIABLES.append(1)
        packages.jvpm_methods.VARIABLES.append(2)
        packages.jvpm_methods.VARIABLES.append(3)
        packages.jvpm_methods.VARIABLES.append(4)
        packages.jvpm_methods.VARIABLES.append(5)

        sys.stdout = unittest.mock.Mock()

class test_long(unittest.TestCase):
    def test_tag_long(self):
        sub_list = ["00", "00", "00", "00", "00", "00", "03", "ea"]
        long_result = packages.pool_translate.PoolTranslate.tag_long(self, sub_list)

        self.assertEqual(long_result, 1002)

    def test_tag_float(self):
        sub_list = ["44","a3","1a","38"]
        float_result = packages.pool_translate.PoolTranslate.tag_float(self, sub_list)
        self.assertEqual(float_result, 1304.8193359375)

class test_pool_opcodes(unittest.TestCase):

    def test_get_opcodes(self):
        jvpm_opcodes_obj = packages.jvpm_opcodes.HeaderClass(name="jvpm/javafiles/AddTwo.class")

        self.assertEqual(jvpm_opcodes_obj.get_magic(), "cafebabe")
        self.assertEqual(jvpm_opcodes_obj.get_minor(), "0000")
        self.assertEqual(jvpm_opcodes_obj.get_minor(), "0037")

        const_pool = jvpm_opcodes_obj.get_const_pool()
        translator = packages.pool_translate.PoolTranslate(const_pool, jvpm_opcodes_obj.skips_in_constant_pool, name="jvpm/javafiles/AddTwo.class")
        translated_pool = translator.translate_pool()
        a_f = ['00', '21']
        this = ['00', '08']
        super = ['00', '09']
        interface = ['00', '00']
        int_table = "interface table empty"
        f_c = ['00', '00']
        field_table = "field table empty"
        methods_count = ['00', '02']
        op_codes = ['2a', 'b7', '00', '01', 'b1', 'bb', '00', '02', '59', 'b2', '00', '03', 'b7', '00', '04', '4c', '2b', 'b6', '00', '05', '3d', '2b', 'b6', '00', '05', '3e', 'b2', '00', '06', '1c', '1d', '60', 'b6', '00', '07', 'b1']
        self.assertEqual(jvpm_opcodes_obj.get_access_flags(), a_f)
        self.assertEqual(jvpm_opcodes_obj.get_this_class(), this)
        self.assertEqual(jvpm_opcodes_obj.get_super_class(), super)
        self.assertEqual(jvpm_opcodes_obj.get_interfaces_count(), interface)
        self.assertEqual(jvpm_opcodes_obj.get_interface(), None)
        self.assertEqual(jvpm_opcodes_obj.get_field_count(), f_c)
        self.assertEqual(jvpm_opcodes_obj.get_field(), None)
        self.assertEqual(jvpm_opcodes_obj.get_methods_count(), methods_count)
        self.assertEqual(jvpm_opcodes_obj.get_methods(translated_pool), op_codes)

    def test_hello_world(self):
        file_name = "jvpm/javafiles/HelloWorld.class"
        header_class_object = packages.jvpm_opcodes.HeaderClass(name=file_name)
        header_class_object.get_magic()
        header_class_object.get_minor()
        header_class_object.get_major()
        get_cp = header_class_object.get_const_pool()
        p_translator = packages.pool_translate.PoolTranslate(get_cp, header_class_object.skips_in_constant_pool,
                                                             name=file_name)
        pool = p_translator.translate_pool()
        access_flags = header_class_object.get_access_flags()
        this_class = header_class_object.get_this_class()
        super_class = header_class_object.get_super_class()
        get_ic = header_class_object.get_interfaces_count()
        header_class_object.get_interface()  # no method built yet but should just be index in constant pool
        get_fc = header_class_object.get_field_count()
        header_class_object.get_field()  # no method built yet but should just be variable table
        opcodes = header_class_object.get_methods_count()
        opcodes = header_class_object.get_methods(pool)

        # ****************************************************************************************

        dict_search_object = packages.jvpm_opcodes.OpCodes(opcodes, pool)
        dict_search_object.dict_search()
        sys.stdout.assert_has_calls([call.write('java/lang/System.in:Ljava/io/InputStream;'), call.write('\n')])


class TestAccessFlagTranslater(unittest.TestCase):
    def test_translate_access_flag(self):
        access_flag_test = packages.access_flag_translater_dictionary.AccessFlagTranslater()

        self.assertEqual(access_flag_test.translate_access_flag(1), "ACC_PUBLIC")
        self.assertEqual(access_flag_test.translate_access_flag(2), "ACC_PRIVATE")
        self.assertEqual(access_flag_test.translate_access_flag(4), "ACC_PROTECTED")
        self.assertEqual(access_flag_test.translate_access_flag(8), "ACC_STATIC")
        self.assertEqual(access_flag_test.translate_access_flag(10), "ACC_FINAL")
        self.assertEqual(access_flag_test.translate_access_flag(20), "ACC_SUPER")
        self.assertEqual(access_flag_test.translate_access_flag(200), "ACC_INTERFACE")
        self.assertEqual(access_flag_test.translate_access_flag(400), "ACC_ABSTRACT")
        self.assertEqual(access_flag_test.translate_access_flag(1000), "ACC_SYNTHETIC")
        self.assertEqual(access_flag_test.translate_access_flag(2000), "ACC_ANNOTATION")
        self.assertEqual(access_flag_test.translate_access_flag(4000), "ACC_ENUM")
