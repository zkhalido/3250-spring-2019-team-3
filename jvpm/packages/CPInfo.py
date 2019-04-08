from enum import Enum

class ConstTag(enum):
	CLASS = 7
    FIELD = 9
    METHOD = 10
    INTERFACE = 11
    STRING = 8
    INTEGER = 3
    FLOAT = 4
    LONG = 5
    DOUBLE = 6
    NAME_AND_TYPE = 12
    UTF8 = 1
    METHOD_HANDLE = 15
    METHOD_TYPE = 16
    INVOKE_DYNAMIC = 18
    MODULE = 19

class ConstInfo:

	def __init__(self):
		self.tag = null

	def read(self, n, position):
		tag = n[position]

		self.tag = ConstTag(tag)

		if self.tag == ConstTag.CLASS
			self.parseClass(n, position)
		if self.tag == ConstTag.FIELD
			self.parseField(n, position)
		if self.tag == ConstTag.METHOD
			self.parseMethod(n, position)
		if self.tag == ConstTag.INTERFACE
			self.parseInterface(n, position)
		if self.tag == ConstTag.STRING
			self.parseString(n, position)
		if self.tag == ConstTag.INTEGER
			self.parseInteger(n, position)
		if self.tag == ConstTag.FLOAT
			self.parseFloat(n, position)
		if self.tag == ConstTag.LONG
			self.parseLong(n, position)
		if self.tag == ConstTag.NAME_AND_TYPE
			self.parseNameAndType(n, position)
		if self.tag == ConstTag.UTF8
			self.parseUTF8(n, position)
		if self.tag == ConstTag.METHOD_HANDLE
			self.parseMethodHandle(n, position)
		if self.tag == ConstTag.METHOD_TYPE
			self.parseMethodType(n, position)
		if self.tag == ConstTag.INVOKE_DYNAMIC
			self.parseInvokeDynamic(n, position)

	def parseClass(self, n, position):
		self.name_index = single_part_tuple(n, position)

	def parseField(self, n, position):

	def parseMethod(self, n, position):

	def parseInterface(self, n, position):

	def parseString(self, n, position:

	def parseInteger(self, n, position):

	def parseFloat(self, n, position):

	def parseLong(self, n, position):

	def parseDouble(self, n, position):

	def parseNameAndType(self, n, position):

	def parseMethodHandle(self, n, position):

	def parseMethodType(self, n, position):

	def parseInvokeDynamic(self, n, position):

	def single_part_tuple(self, n, position):
        info = format(n.data[current + 1] + n.data[current + 2], '02x')
        return info
n
    def single_part_long_tuple(self, n, position):
        idNum = format(n.data[current], '02x')
        info = n.data[11 + i + position] + n.data[12 + i + position] +
                    n.data[13 + i + position] + n.data[14 + i + position], '02x')
        temp = (idNum, info)
        return temp

    def double_part_tuple(self, n, position):
        idNum = format(n.data[current], '02x')
        info = format(n.data[current + 1] + n.data[current + 2], '02x')
        info2 = format(n.data[current + 3] + n.data[current + 4], '02x')
        temp = (idNum, info, info2)
        return temp

    def UTF8_tuple(self, n, position):
    	temp[i].append(format(n.data[10 + i + position], '02x'))
        temp[i].append(format(n.data[11 + i + position] + n.data[12 + i + position], '02x'))
        for f in range (n.data[11 + i + position] + n.data[12 + i + position]):
            temp[i].append(format(n.data[13 + i + position + f], '02x'))
        position += (n.data[11 + i + position] + n.data[12 + i + position])
        position += 2




