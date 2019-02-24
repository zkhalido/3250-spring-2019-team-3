"""import the unittest"""
import unittest
from bitstring import ConstBitStream
import jvpm_dict    # import external opcode dictionary
import jvpm_methods # import external method dictionary

# pylint: disable = W0105, C0122, R0903

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

# ****************************************************************************************

# Unittest to test the output of the HeaderClass() methods.
# python3 -m unittest jvpm_opcodes.py
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

# ****************************************************************************************

class OpCodes():
    """Class that searches the external dictionary of opcodes and Implements using
    the external dictionary of methods"""
    def __init__(self):
#         self.opcodes = ['02', '03', '04', '05', '06', '07',
#                         '08', '3b', '3c', '3d', '3e', '84']
        self.opcode0 = '02'
        self.opcode1 = '3c'
        self.opcode2 = '84'

        """


        METHOD GOES HERE TO FIND AND ASSIGN OPCODES FROM TEST.CLASS AND ASSIGN TO ABOVE VARIABLES.



        """

    def dict_search(self):
        """Search the jvpm.dict.py(dictionary) file for the bytecode/opcode translation and
        Implement if found"""
	# Opcode to implement from imported dictionary:
        opcode_to_call_0 = jvpm_dict.get_opcode(self.opcode0)
        print("\nOpcode to implement from bytecode " + self.opcode0 + ': ' + opcode_to_call_0)
        opcode_to_call_1 = jvpm_dict.get_opcode(self.opcode1)
        print("Opcode to implement from bytecode " + self.opcode1 + ': ' + opcode_to_call_1)
        opcode_to_call_2 = jvpm_dict.get_opcode(self.opcode2)
        print("Opcode to implement from bytecode " + self.opcode2 + ': ' + opcode_to_call_2)

        # Search jvpm_method.py for method from above opcodeToCall variables and Implement.
        print('\n3) ____IMPLEMENT THE OPCODES:____\n')
        jvpm_methods.opcode_methods(opcode_to_call_0)
        jvpm_methods.opcode_methods(opcode_to_call_1)
        jvpm_methods.opcode_methods(opcode_to_call_2)
        print()
        return self.opcode0

# ****************************************************************************************

if '__main__' == __name__:

    # ************************************************************************************

    print('\n1) ___Parse, pull, and assign Header bytecodes:___')
    D = HeaderClass()
    D.pull_magic()
    D.pull_minor()
    D.pull_major()
    D.pull_const_pool_count()

    # ************************************************************************************

    print('\n2) ___Parse, pull, and assign Method bytecodes, search imported dictionary for'
          '\n  bytecode and return opcode. If found, send opcode to jvpm_methods.py to'
          '\n  Implement the method:___')
    Z = OpCodes()
    Z.dict_search()

# ****************************************************************************************
