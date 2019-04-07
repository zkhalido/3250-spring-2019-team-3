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
			self.parseSting(n, position)
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
		if self.tag == ConstTag.MODULE
			self.parseModule(n, position)



