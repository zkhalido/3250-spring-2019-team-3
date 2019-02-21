"""import the unittest"""
import unittest
from collections import namedtuple
from bitstring import ConstBitStream

# pylint: disable = W0105

"""Class that parses the data from test.class"""
class HeaderClass():
    def __init__(self):
        self.stream = ConstBitStream(filename='test.class')
        self.header_magic = ""
        self.header_minor = ""
        self.header_major = ""
        self.header_const_pool_count = ""

    def pull_magic(self):
        self.header_magic = self.stream.read(32).hex
        print("header: ", self.header_magic)
        return self.header_magic

    def pull_minor(self):
        self.header_minor = self.stream.read(8).uint + self.stream.read(8).uint
        print("minor: ", self.header_minor)
        return self.header_minor

    def pull_major(self):
        self.header_major = self.stream.read(8).uint + self.stream.read(8).uint
        print("major: ", self.header_major)
        return self.header_major

    def pull_const_pool_count(self):
        self.header_const_pool_count = self.stream.read(8).uint + self.stream.read(8).uint - 1
        print("const pool: ", self.header_const_pool_count)
        return self.header_const_pool_count

"""
		headerConstPoolCount = self.x.read(8).uint + self.x.read(8).uint
		headerCPInfo = [None] * (headerConstPoolCount - 1)
		headerAccessFlag = self.x.read(8).uint + self.x.read(8).uint
		headerThisClass = self.x.read(8).uint + self.x.read(8).uint
		headerSuperClass = self.x.read(8).uint + self.x.read(8).uint
		headerInterfacesCount = self.x.read(8).uint + self.x.read(8).uint
		headerInterfaces = [None] * headerInterfacesCount
		headerFieldsCount = self.x.read(8).uint + self.x.read(8).uint
		headerFields = [None] * headerFieldsCount
		headerMethodsCount = self.x.read(8).uint + self.x.read(8).uint
		headerMethods = [None] * headerMethodsCount
		headerAttributesCount = self.x.read(8).uint + self.x.read(8).uint
		headerAttributes = [None] * headerAttributesCount
		print("header: ", headerMagic)
		print(headerMinor)
		print(headerMajor)
		print(headerConstPoolCount)
		print(len(headerCPInfo))
		print(headerAccessFlag)
		print(headerThisClass)
		print(headerSuperClass)
		print(headerInterfacesCount)
		print(len(headerInterfaces))
		print(headerFieldsCount)
		print(len(headerFields))
		print(headerMethodsCount)
		print(len(headerMethods))
		print(headerAttributesCount)
		print(len(headerAttributes))
"""

# Unittest to test the output of the HeaderClass() methods.
# python3 -m unittest jvpm.py
# We have a warning about an unclosed file but no errors.

"""unittest to test method outputs"""
class UnittestHeader(unittest.TestCase):
    def setUp(self):
        """instantiate an instance of HeaderClass"""
        self.test = HeaderClass()

    def test_magic(self):
        self.test.pull_magic()
        """the comparison"""
        self.assertEqual(self.test.header_magic, 'cafebabe')
        print('<<<< passed header_magic, ' + self.test.header_magic + ' = cafebabe >>>>\n')

    def test_minor(self):
        """the known output"""
        known_minor = 0
        """call methods in order, including the desired method, to acquire value."""
        self.test.pull_magic()
        self.test.pull_minor()
        """the comparison"""
        self.assertEqual(self.test.header_minor, 0)
        print(f'<<<< passed header_minor, {self.test.header_minor} = {known_minor} >>>>\n')

    def test_major(self):
        """the known output"""
        known_major = 54
        """call methods in order, including the desired method, to acquire value."""
        self.test.pull_magic()
        self.test.pull_minor()
        self.test.pull_major()
        """the comparison"""
        self.assertEqual(self.test.header_major, 54)
        print(f'<<<< passed header_major, {self.test.header_major} = {known_major} >>>>\n')

    def test_pool_count(self):
        """the known output"""
        known_pool_count = 14
        """call methods in order, including the desired method, to acquire value."""
        self.test.pull_magic()
        self.test.pull_minor()
        self.test.pull_major()
        self.test.pull_const_pool_count()
        """the comparison"""
        self.assertEqual(self.test.header_const_pool_count, 14)
        print(f'< passed poolCount, {self.test.header_const_pool_count} = {known_pool_count} >\n')

# NOT SURE WHERE THESE LAST THREE CLASSES CAME FROM
# BUT IF YOU COMMENT THEM OUT THE UNITTEST WILL WORK. D

"""
class OpCodes():
    def __init__(self):
        self.table = {
        	0x32: 'aaload',
        	0x01: 'aconst_null'

        }

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value):
        return self.table[value]()

class UnittestHeader(unittest.TestCase):
	def setUp(self):
		m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x00\x36\x00\x0F')
		with patch(__name__ + '.open', m):
			self.cf = HeaderClass()

	def test_magic(self):
		self.assertEqual(self.cf.get_magic(), 'CAFEBABE')
		print("unittestmagic", self.cf.get_magic())

	def test_minor(self):
		self.assertEqual(self.cf.get_minor(), 0)
		print("unittestprintminor", self.cf.get_minor())

	def test_major(self):
		self.assertEqual(self.cf.get_major(), 54)
		print("unittestprintmajor", self.cf.get_major())

	def test_PoolCount(self):
		self.assertEqual(self.cf.get_poolCount(), 15)
		print("unittestprintpool", self.cf.get_poolCount())

class TestOpCodes(unittest.TestCase):
	def setUp(self):
		m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x00\x36\x00\x0F')
		with patch(__name__ + '.open', m):
			self.cf = OpCodes()

	def test_interpret(self, value):
		self.assertEqual(self.cf.interpret(1), 'aconst_null')

	def test_not_implmented(self):
		self.assertEqual(OpCodes().interpret(1), 'aconst_null')
		with self.assertRaises(KeyError):
			OpCodes().interpret(1)
"""

if '__main__' == __name__:
    D = HeaderClass()
    D.pull_magic()
    D.pull_minor()
    D.pull_major()
    D.pull_const_pool_count()
