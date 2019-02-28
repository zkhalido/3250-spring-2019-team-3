# """import the unittest"""
# import unittest
"""Read bit stream."""
from bitstring import ConstBitStream
import jvpm_dict    # import external opcode dictionary
import jvpm_methods # import external method dictionary

# pylint: disable = W0105, C0122, R0903

# **************************************************************************************************

class HeaderClass():
    """Class that parses the header data from .class file and assigns values to variables."""
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print("\nMagic: ", magic)
        return magic

    def get_minor(self):
        print("Minor: ", self.data[4] + self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        print("Major: ", self.data[6] + self.data[7])
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        print("Contant Pool Count: ", self.data[8] + self.data[9] - 1)
        return self.data[8] + self.data[9]

# **************************************************************************************************

class OpCodes():
    """Parse Opcodes into an array from the .class file, search the external dictionary of
    opcodes, and implement the methods using the external dictionary of methods"""
    def __init__(self):
        self.opcodes = ['06', '3c', '1b', '74', '3e']
        """this is the constructor"""
        with open('test.class', 'rb') as binary_file:
            self.data = bytes(binary_file.read())
        self.table = {0x2a: aload_0,
                      0xb1: ret,
                      0x04: iconst_1,
                      0x3c: istore_1,
                      0x84: iinc,
                      0xb7: invokespecial,
                      0x60: iadd,
                      0x64: isub,
                      0x68: imul,
                      0x6c: idiv,
                      0x70: irem,
                      0x7e: iand,
                      0x74: ineg,
                      0x80: ior,
                      0x82: ixor,
                      0x00: not_implemented}
        self.byte_count = 0
    def parse_codes(self, op_start):
        """this method searches the binary for only the opcodes we know are in it"""
        self.byte_count = op_start
        while self.byte_count < len(self.data):
            if self.data[self.byte_count] in {0x2a, 0xb1, 0x04, 0x3c, 0x84, 0xb7}:
                print(self.interpret(self.data[self.byte_count]))
            else:
                self.interpret(0)

    def interpret(self, value):
        """this is the method used to interpret a given opcode"""
        return self.table[value](self)

        """


        METHOD GOES HERE TO FIND OPCODES FROM ANY .CLASS FILE AND SAVE TO self.opcodes LIST.



        """

    def dict_search(self):
        """Search the jvpm.dict.py(dictionary) file for the bytecode/opcode translation and
        implement if found."""
	# Hex to Opcode from imported opcode dictionary - jvpm_dict,
        # implemented using imported method dictionary - jvpm_methods.
        print("\nBytecodes from .class file: " + str(self.opcodes))
        index = 0
        while index < len(self.opcodes):
            opcall = jvpm_dict.get_opcode(self.opcodes[index])
            print("Bytecode " + self.opcodes[index] + ' = Opcode: ' + opcall)
            jvpm_methods.opcode_methods(opcall)
            index += 1
        print()
        # return
        
def aload_0(self):
    """this is a dummy method"""
    print('aload_0')
    self.byte_count += 1

def ret(self):
    """this function will eventually implement the ret opcode"""
    self.byte_count += 1
    print('return')

def iconst_1(self):
    """this function implements the iconst_1 opcode"""
    self.byte_count += 1
    print('iconst_1')

def istore_1(self):
    """this function implements the istore_1 opcode"""
    self.byte_count += 1
    print('istore_1')

def iinc(self):
    """this function implements the iinc opcode"""
    self.byte_count += 1
    print('iinc')

def invokespecial(self):
    """This function implements the invokespecial opcode"""
    byte_1 = self.data[self.byte_count + 1]
    byte_2 = self.data[self.byte_count + 2]
    self.byte_count += 3
    print('invokespecial')
    return byte_1+byte_2
def iadd(self):
    """implements the iadd opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1+val2)
    self.byte_count += 1
def isub(self):
    """implements the isub opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1-val2)
    self.byte_count += 1
def imul(self):
    """implements the imul opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1*val2)
    self.byte_count += 1
def idiv(self):
    """implements the idiv opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(numpy.int32(val1/val2))
    self.byte_count += 1
#irem will be implemented in terms of the other operations.
#a%b = a-(a/b)*b
def irem(self):
    """implements the irem opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1)
    self.stack.push_op(val1)
    self.stack.push_op(val2)
    idiv(self)
    self.stack.push_op(val2)
    imul(self)
    isub(self)
#fixes a bug where byte_count is incremented too many times
    self.byte_count -= 2

def iand(self):
    """Perform bitwise AND on the top two operands on the stack."""
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val & that_val)
    self.byte_count += 1

def ineg(self):
    """ Perform bitwise NOT on the top operand on the stack. """
    not_this = self.stack.pop_op()
    self.stack.push_op(~not_this)
    self.byte_count += 1

def ior(self):
    """ Perform bitwise OR on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val | that_val)
    self.byte_count += 1

def ixor(self):
    """ Perform bitwise XOR on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val ^ that_val)
    self.byte_count += 1

# **************************************************************************************************

if '__main__' == __name__:

    # **********************************************************************************************

    print('\n1) ___Parse, pull, and assign Header bytecodes:___')
    D = HeaderClass()
    D.get_magic()
    D.get_minor()
    D.get_major()
    D.get_const_pool_count()

    # **********************************************************************************************

    print('\n2) ___Parse, pull, and assign method bytecodes to an array, search imported '
          '\n  opcode dictionary for bytecode and pull opcode. If found, send opcode to'
          '\n  imported method dictionary to implement the method:___')
    Z = OpCodes()
    Z.dict_search()
    Z.parse_codes(183)

# **************************************************************************************************

# Unittest to test the output of the HeaderClass() methods.
# python3 -m unittest jvpm_opcodes.py
# We have a warning about an unclosed file but no errors.

# class UnittestHeader(unittest.TestCase):
#     """unittest to test method outputs"""
#     def setUp(self):
#         """instantiate an instance of HeaderClass"""
#         self.test = HeaderClass()

#     def test_magic(self):
#         """method to test the pull_magic output"""
#         self.test.pull_magic()
#         """the comparison"""
#         self.assertEqual(self.test.header_magic, 'cafebabe')
#         print('<<<< passed header_magic, ' + self.test.header_magic + ' = cafebabe >>>>\n')

#     def test_minor(self):
#         """method to test the pull_minor output"""
#         known_minor = 0
#         """call methods in order, including the desired method, to acquire value."""
#         self.test.pull_magic()
#         self.test.pull_minor()
#         """the comparison"""
#         self.assertEqual(self.test.header_minor, 0)
#         print(f'<<<< passed header_minor, {self.test.header_minor} = {known_minor} >>>>\n')

#     def test_major(self):
#         """method to test the pull_major output"""
#         known_major = 54
#         """call methods in order, including the desired method, to acquire value."""
#         self.test.pull_magic()
#         self.test.pull_minor()
#         self.test.pull_major()
#         """the comparison"""
#         self.assertEqual(self.test.header_major, 54)
#         print(f'<<<< passed header_major, {self.test.header_major} = {known_major} >>>>\n')

#     def test_pool_count(self):
#         """method to test the pull_const_pool_count output"""
#         known_pool_count = 14
#         """call methods in order, including the desired method, to acquire value."""
#         self.test.pull_magic()
#         self.test.pull_minor()
#         self.test.pull_major()
#         self.test.pull_const_pool_count()
#         """the comparison"""
#         self.assertEqual(self.test.header_const_pool_count, 14)
#         print(f'< passed poolCount, {self.test.header_const_pool_count} = {known_pool_count} >\n')

# **************************************************************************************************
