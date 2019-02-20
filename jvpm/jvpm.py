from collections import namedtuple
from bitstring import ConstBitStream
import unittest

class HeaderClass():
	def __init__(self):
            self.x = ConstBitStream(filename='test.class')

	def PullMagic(self):
		self.headerMagic = self.x.read(32).hex
		print("header: ", self.headerMagic)
		return self.headerMagic

	def PullMinor(self):
		self.headerMinor = self.x.read(8).uint + self.x.read(8).uint
		print("minor: ", self.headerMinor)
		return self.headerMinor

	def PullMajor(self):
		self.headerMajor = self.x.read(8).uint + self.x.read(8).uint
		print("major: ", self.headerMajor)
		return self.headerMajor

	def PullConstPoolCount(self):
		self.headerConstPoolCount = self.x.read(8).uint + self.x.read(8).uint - 1
		print("const pool: ", self.headerConstPoolCount)
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

    def test_headers(self):
        a = 0
        b = 54
        c = 14
        print()
        print('HEADERS:')
        self.test.PullMagic()
        self.test.PullMinor()
        self.test.PullMajor()
        self.test.PullConstPoolCount()
        print()
        print('UNITTESTS:')
        self.assertEqual(self.test.headerMagic, 'cafebabe')
        print('passed headerMagic, ' + self.test.headerMagic + ' = cafebabe')
        self.assertEqual(self.test.headerMinor, 0)
        print(f'passed headerMinor, {self.test.headerMinor}  = {a}')
        self.assertEqual(self.test.headerMajor, 54)
        print(f'passed headerMajor, {self.test.headerMajor} = {b}')
        self.assertEqual(self.test.headerConstPoolCount, 14)
        print(f'passed poolCount, {self.test.headerConstPoolCount} = {c}')
        print()

if '__main__' == __name__:
	d = HeaderClass()
	d.PullMagic()
	d.PullMinor()
	d.PullMajor()
	d.PullConstPoolCount()
