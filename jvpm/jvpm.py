from collections import namedtuple
from bitstring import ConstBitStream


HeaderInformation = namedtuple("HeaderInformation", "magic minor_version major_version")

def PullHeader():
	x = ConstBitStream(filename='test.class')
	headerMagic = x.read(32).hex
	headerMinor = x.read(16).hex
	headerMajor = x.read(16).hex
	headerConstPoolCount = x.read(16).hex
	headerCPInfo = [None] * (int(headerConstPoolCount, 16) - 1)
	headerAccessFlag = x.read(16).hex
	headerThisClass = x.read(16).hex
	headerSuperClass = x.read(16).hex
	headerInterfacesCount = x.read(16).hex
	headerInterfaces = [None] * int(headerInterfacesCount, 16)
	headerFieldsCount = x.read(16).hex
	headerFields = [None] * int(headerFieldsCount, 16)
	headerMethodsCount = x.read(16).hex
	headerMethods = [None] * int(headerMethodsCount, 16)
	headerAttributesCount = x.read(16).hex
	headerAttributes = [None] * int(headerAttributesCount, 16)
	print(headerMagic)
	print(headerMinor)
	print(headerMajor)
	print(headerConstPoolCount)
	print(headerCPInfo)
	print(headerAccessFlag)
	print(headerThisClass)
	print(headerSuperClass)
	print(headerInterfacesCount)
	print(headerInterfaces)
	print(headerFieldsCount)
	print(headerFields)
	print(headerMethodsCount)
	print(headerMethods)
	print(headerAttributesCount)
	print(headerAttributes)

	

if '__main__' == __name__:
	PullHeader()