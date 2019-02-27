# """import the unittest"""
# import unittest
"""Read bit stream."""
from bitstring import ConstBitStream
import jvpm_dict    # import external opcode dictionary
import jvpm_methods # import external method dictionary

# pylint: disable = W0105, C0122, R0903

# **************************************************************************************************

class HeaderClass():
    """Class that parses the data from test.class and assigns values to variables"""
    def __init__(self):
        self.stream = ConstBitStream(filename='test.class')
        self.header_magic = ""
        self.header_minor = ""
        self.header_major = ""
        self.header_const_pool_count = ""

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

# **************************************************************************************************

class OpCodes():
    """Class that searches the external dictionary of opcodes and implements using
    the external dictionary of methods"""
    def __init__(self):
        # List of the test1.java(math) opcodes.
        self.opcodes = ['04', '3c', '05', '3d', '1b', '1c',
                        '60', '3e']

        """


        METHOD GOES HERE TO FIND OPCODES FROM TEST.CLASS AND SAVE TO self.opcodes ARRAY.



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

if '__main__' == __name__:

    # **********************************************************************************************

    print('\n1) ___Parse, pull, and assign Header bytecodes:___')
    D = HeaderClass()
    D.pull_magic()
    D.pull_minor()
    D.pull_major()
    D.pull_const_pool_count()

    # **********************************************************************************************

    print('\n2) ___Parse, pull, and assign method bytecodes to an array, search imported '
          '\n  opcode dictionary for bytecode and pull opcode. If found, send opcode to'
          '\n  imported method dictionary to implement the method:___')
    Z = OpCodes()
    Z.dict_search()

# **************************************************************************************************
