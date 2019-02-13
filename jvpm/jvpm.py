from collections import namedtuple
from bitstring import ConstBitStream


HeaderInformation = namedtuple("HeaderInformation", "magic minor_version major_version")

def PullHeader():
	x = ConstBitStream(filename='test.class')
	headerMagic = x.read(32).hex
	headerMinor = x.read(16).hex
	headerMajor = x.read(16).hex
	headerConstPoolCount = x.read(16).hex
	headerCPInfo = []
	headerAccessFlag = x.read(16).hex
	headerThisClass = x.read(16).hex
	headerSuperClass = x.read(16).hex
	headerInterfacesCount = x.read(16).hex
	headerInterfaces = []
	headerFieldsCount = x.read(16).hex
	headerFields = []
	headerMethodsCount = x.read(16).hex
	headerMethods = []
	headerAttributesCount = x.read(16).hex
	headerAttributes = []
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