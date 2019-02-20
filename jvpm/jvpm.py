from collections import namedtuple
from bitstring import ConstBitStream
import unittest

class HeaderClass():
	def __init__(self):
            self.x = ConstBitStream(filename='test.class')

	def PullMagic(self):
		self.headerMagic = self.x.read(32).hex
		# print("header: ", self.headerMagic)
		return self.headerMagic

	def PullMinor(self):
		self.headerMinor = self.x.read(8).uint + self.x.read(8).uint
		# print("minor: ", self.headerMinor)
		return self.headerMinor

	def PullMajor(self):
		self.headerMajor = self.x.read(8).uint + self.x.read(8).uint
		# print("major: ", self.headerMajor)
		return self.headerMajor

	def PullConstPoolCount(self):
		self.headerConstPoolCount = self.x.read(8).uint + self.x.read(8).uint - 1
		# print("const pool: ", self.headerConstPoolCount)
		return self.headerConstPoolCount

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
class UnittestHeader(unittest.TestCase):
    def setUp(self):
        self.test = HeaderClass() # instantiate an instance of HeaderClass

    def test_magic(self):
        self.test.PullMagic()
        self.assertEqual(self.test.headerMagic, 'cafebabe')
        print('passed headerMagic, ' + self.test.headerMagic + ' = cafebabe')

    def test_minor(self):
        a = 0
        self.test.PullMagic()
        self.test.PullMinor()
        self.assertEqual(self.test.headerMinor, 0)
        print(f'passed headerMinor, {self.test.headerMinor} = {a}')
        print()

    def test_major(self):
        b = 54
        self.test.PullMagic()
        self.test.PullMinor()
        self.test.PullMajor()
        self.assertEqual(self.test.headerMajor, 54)
        print(f'passed headerMajor, {self.test.headerMajor} = {b}')
        print()

    def test_poolCount(self):
        c = 14
        self.test.PullMagic()
        self.test.PullMinor()
        self.test.PullMajor()
        self.test.PullConstPoolCount()
        self.assertEqual(self.test.headerConstPoolCount, 14)
        print(f'passed poolCount, {self.test.headerConstPoolCount} = {c}')
        print()
	
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
	d = HeaderClass()
	d.PullMagic()
	d.PullMinor()
	d.PullMajor()
	d.PullConstPoolCount()

