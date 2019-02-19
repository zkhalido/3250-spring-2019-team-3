from collections import namedtuple
from bitstring import ConstBitStream

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
		print("const pool: ", headerConstPoolCount - 1)
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


if '__main__' == __name__:
	d = HeaderClass()
	d.PullMagic()
	d.PullMinor()
	d.PullMajor()
	d.PullConstPoolCount()
