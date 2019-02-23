"""import the unittest"""
import unittest
# from collections import namedtuple
from bitstring import ConstBitStream
# pylint: disable = W0105, C0122
import jvpm_dict
import jvpm_methods

class HeaderClass():
    """Class that parses the data from test.class
    and assigns values to variables
    """
    def __init__(self):
        self.stream = ConstBitStream(filename='test.class')
        self.header_magic = ""
        self.header_minor = ""
        self.header_major = ""
        self.header_const_pool_count = ""
        self.opcode0 = ""
        self.opcode1 = ""
        self.opcode2 = ""

    def pull_magic(self):
        """method to pull the magic data"""
        self.header_magic = self.stream.read(32).hex
        print("\nheader: ", self.header_magic)
        return self.header_magic

    def pull_minor(self):
        """method to pull the minor data"""
        self.header_minor = self.stream.read(8).uint + self.stream.read(8).uint
        print("minor: ", self.header_minor)
        return self.header_minor

    def pull_major(self):
        """method to pull the major data"""
        self.header_major = self.stream.read(8).uint + self.stream.read(8).uint
        print("major: ", self.header_major)
        return self.header_major

    def pull_const_pool_count(self):
        """method to pull the pool count data"""
        self.header_const_pool_count = self.stream.read(8).uint + self.stream.read(8).uint - 1
        print("const pool: ", self.header_const_pool_count)
        return self.header_const_pool_count

class Stack:
    """Class that creates a Stack, with methods to interact with the Stack"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """test if Stack is empty"""
        return self.items == []

    def push(self, item):
        """Put item on the stack"""
        self.items.append(item)

    def pop(self):
        """Take item off stack"""
        return self.items.pop()

    def peek(self):
        """Look at item on top of stack"""
        return self.items[len(self.items)-1]

    def size(self):
        """Tells how many items are on the stack"""
        return len(self.items)

# Unittest to test the output of the HeaderClass() methods.
# python3 -m unittest jvpm.py
# We have a warning about an unclosed file but no errors.

class UnittestHeader(unittest.TestCase):
    """unittest to test method outputs"""
    def setUp(self):
        """instantiate an instance of HeaderClass"""
        self.test = HeaderClass()

    def test_magic(self):
        """method to test the pull_magic output"""
        self.test.pull_magic()
        """the comparison"""
        self.assertEqual(self.test.header_magic, 'cafebabe')
        print('<<<< passed header_magic, ' + self.test.header_magic + ' = cafebabe >>>>\n')

    def test_minor(self):
        """method to test the pull_minor output"""
        known_minor = 0
        """call methods in order, including the desired method, to acquire value."""
        self.test.pull_magic()
        self.test.pull_minor()
        """the comparison"""
        self.assertEqual(self.test.header_minor, 0)
        print(f'<<<< passed header_minor, {self.test.header_minor} = {known_minor} >>>>\n')

    def test_major(self):
        """method to test the pull_major output"""
        known_major = 54
        """call methods in order, including the desired method, to acquire value."""
        self.test.pull_magic()
        self.test.pull_minor()
        self.test.pull_major()
        """the comparison"""
        self.assertEqual(self.test.header_major, 54)
        print(f'<<<< passed header_major, {self.test.header_major} = {known_major} >>>>\n')

    def test_pool_count(self):
        """method to test the pull_const_pool_count output"""
        known_pool_count = 14
        """call methods in order, including the desired method, to acquire value."""
        self.test.pull_magic()
        self.test.pull_minor()
        self.test.pull_major()
        self.test.pull_const_pool_count()
        """the comparison"""
        self.assertEqual(self.test.header_const_pool_count, 14)
        print(f'< passed poolCount, {self.test.header_const_pool_count} = {known_pool_count} >\n')

class OpCodes():
    """Class that contains a dictionary of opcodes to Implement"""
    def __init__(self):
        self.opcodes = ['02', '03', '04', '05', '06', '07',
                        '08', '3b', '3c', '3d', '3e', '84']
        self.opcode0 = '02'
        self.opcode1 = '3c'
        self.opcode2 = '84'

        """
        
        
        BOB"S CODE HERE TO FIND AND ASSIGN OPCODE VARIABLES TO ABOVE ASSIGNED VARIABLES
        
        
        
        """
	
    """Search the jvpm.dict.py(dictionary) file for the bytecode/opcode translation"""
    def dict_search(self):
        jvpm_dict.get_opcode(self.opcode0)
        print("\nImported Dictionary search for bytecode: " + self.opcode0 + 
	      " returns opcode: " + jvpm_dict.get_opcode(self.opcode0))
        print("Imported Dictionary search for bytecode: " + self.opcode1 + 
	      " returns opcode: " + jvpm_dict.get_opcode(self.opcode1))
        print("Imported Dictionary search for bytecode: " + self.opcode2 + 
	      " returns opcode: " + jvpm_dict.get_opcode(self.opcode2))
        return self.opcode0

    def opcode0_list_search(self):
        """search list for iconst opcodes and returns the index position to method call in the main"""
        if self.opcode0 in self.opcodes:
            if self.opcode0 == '02':
                code = 'iconst_m1'
                print('Test File contains the ' + code + ' opcode.')
            elif self.opcode0 == '03':
                code = 'iconst_0'
                print('Test File contains the ' + code + ' opcode.')
            elif self.opcode0 == '04':
                code = 'iconst_1'
                print('Test File contains the ' + code + ' opcode.')
            elif self.opcode0 == '05':
                code = 'iconst_2'
                print('Test File contains the ' + code + ' opcode.')
            elif self.opcode0 == '06':
                code = 'iconst_3'
                print('Test File contains the ' + code + ' opcode.')
            elif self.opcode0 == '07':
                code = 'iconst_4'
                print('Test File contains the ' + code + ' opcode.')
            elif self.opcode0 == '08':
                code = 'iconst_5'
                print('Test File contains the ' + code + ' opcode.')
        return self.opcodes.index(self.opcode0)

    def opcode1_list_search(self):
        """search list for istore opcodes and 
	returns the index position to method call in the main"""
        if self.opcode1 in self.opcodes:
            if self.opcode1 == '3b':
                code_1 = 'istore_0'
                print('Test File contains the ' + code_1 + ' opcode.')
            elif self.opcode1 == '3c':
                code_1 = 'istore_1'
                print('Test File contains the ' + code_1 + ' opcode.')
            elif self.opcode1 == '3d':
                code_1 = 'istore_2'
                print('Test File contains the ' + code_1 + ' opcode.')
            elif self.opcode1 == '3e':
                code_1 = 'istore_3'
                print('Test File contains the ' + code_1 + ' opcode.')
        return self.opcodes.index(self.opcode1)

    def opcode2_list_search(self):
        """search list for iinc opcodes and 
	returns the index position to method call in the main"""
        if self.opcode2 in self.opcodes:
            print('Test File contains the iinc(++) opcode.')
        return self.opcodes.index(self.opcode2)

if '__main__' == __name__:
    print('\n1) ___Parse, pull, and assign Header bytecodes:___')
    D = HeaderClass()
    D.pull_magic()
    D.pull_minor()
    D.pull_major()
    D.pull_const_pool_count()
    
    print('\n2) ___Parse, pull, and assign Method bytecodes, search imported disctionary for\n' 
          '    Method bytecodes and return opcode mnemonics:___')
    Z = OpCodes()
    Z.dict_search()
	
    methodToCall = jvpm_methods.tokenDict[Z.dict_search()]
    print(methodToCall)
    print('XXXXX')
    #jvpm_methods.methodToCall()

    print('\n3) ____IMPLEMENT THE OPCODES:____\n')
    S = Stack()
    """tests if the Stack is empty and pritns result"""
    print('       ' + str(S.is_empty()) + ': Stack is Empty.')

    """method call that searches Opcode method list for iconst opcode and returns index position,
    then it calls the Stack method corresponding to the Opcode command returned from the list search."""
    OP_VALUE_0 = Z.opcode0_list_search()
    """If list search return is equal to index position 0, method pushes -1 to stack, 
    etc., etc. , for each value."""
    if OP_VALUE_0 == 0:
        S.push(-1)
        print('      <<<< Push ' + str(S.peek()) + ' to Stack >>>>')
    elif OP_VALUE_0 == 1:
        S.push(0)
        print('      <<<< Push ' + str(S.peek()) + ' to Stack >>>>')
    elif OP_VALUE_0 == 2:
        S.push(1)
        print('      <<<< Push ' + str(S.peek()) + ' to Stack >>>>')
    elif OP_VALUE_0 == 3:
        S.push(2)
        print('      <<<< Push ' + str(S.peek()) + ' to Stack >>>>')
    elif OP_VALUE_0 == 4:
        S.push(3)
        print('      <<<< Push ' + str(S.peek()) + ' to Stack >>>>')
    elif OP_VALUE_0 == 5:
        S.push(4)
        print('      <<<< Push ' + str(S.peek()) + ' to Stack >>>>')
    elif OP_VALUE_0 == 6:
        S.push(5)
        print('      <<<< Push ' + str(S.peek()) + ' to Stack >>>>')

    """method call that searches Opcode method list for istore opcode and returns index position,
    then it calls the Stack method corresponding to the Opcode command returned from the list search."""
    OP_VALUE_1 = Z.opcode1_list_search()
    if OP_VALUE_1 == 7:
        VARIABLE_0 = S.peek()
        print('       <<<< VARIABLE_0 = ' + str(VARIABLE_0) + ' >>>>')
    elif OP_VALUE_1 == 8:
        VARIABLE_1 = S.peek()
        print('       <<<< VARIABLE_1 = ' + str(VARIABLE_1) + ' >>>>')
    elif OP_VALUE_1 == 9:
        VARIABLE_2 = S.peek()
        print('       <<<< VARIABLE_2 = ' + str(VARIABLE_2) + ' >>>>')
    elif OP_VALUE_1 == 10:
        VARIABLE_3 = S.peek()
        print('       <<<< VARIABLE_3 = ' + str(VARIABLE_3) + ' >>>>')

    """method call that searches Opcode method list for iinc opcode and returns index position,
    then it calls the Stack method corresponding to the Opcode command returned from the list search."""
    OP_VALUE_2 = Z.opcode2_list_search()
    if OP_VALUE_2 == 11:
        VARIABLE_4 = S.peek() + 1
        if OP_VALUE_1 == 7:
            VARIABLE_0 = VARIABLE_4
            print('      <<<< VARIABLE_0++ = ' + str(VARIABLE_0) + ' >>>>')
        elif OP_VALUE_1 == 8:
            VARIABLE_1 = VARIABLE_4
            print('      <<<< VARIABLE_1++ = ' + str(VARIABLE_1) + ' >>>>')
        elif OP_VALUE_1 == 9:
            VARIABLE_2 = VARIABLE_4
            print('      <<<< VARIABLE_2++ = ' + str(VARIABLE_2) + ' >>>>')
        elif OP_VALUE_1 == 10:
            VARIABLE_3 = VARIABLE_4
            print('      <<<< VARIABLE_3++ = ' + str(VARIABLE_3) + ' >>>>')
        print()
