from collections import namedtuple
from bitstring import ConstBitStream
import unittest

class HeaderClass():
	def __init__(self):
            self.x = ConstBitStream(filename='test.class')
	def PullMagic(self):
		headerMagic = self.x.read(32).hex
		print("header: ", headerMagic)
		return headerMagic

	def PullMinor(self):
		headerMinor = self.x.read(8).uint + self.x.read(8).uint
		print("minor: ", headerMinor)
		return headerMinor

	def PullMajor(self):
		headerMajor = self.x.read(8).uint + self.x.read(8).uint
		print("major: ", headerMajor)
		return headerMajor

	def PullConstPoolCount(self):
		headerConstPoolCount = self.x.read(8).uint + self.x.read(8).uint
		print("const pool: ", headerConstPoolCount)
		return headerConstPoolCount

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

if '__main__' == __name__:
	d = HeaderClass()
	d.PullMagic()
	d.PullMinor()
	d.PullMajor()
	d.PullConstPoolCount()

