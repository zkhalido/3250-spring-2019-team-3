from enum import Enum
from .Unpacker import Unpacker

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
		self.name_index = Unpacker.single_part_tuple(n, position)

	def parseField(self, n, position):
		self.class_index = Unpacker.single_part_tuple(n, position)
		self.name_and_type_index = Unpacker.single_part_tuple(n, position)

	def parseMethod(self, n, position):
		self.class_index = Unpacker.two_byte_unpack(n, position)
		self.name_and_type_index = Unpacker.two_byte_unpack(n, position)

	def parseInterface(self, n, position):
		self.class_index = Unpacker.two_byte_unpack(n, position)
		self.name_and_type_index = Unpacker.two_byte_unpack(n, position)

	def parseString(self, n, position):
		self.string_index = Unpacker.two_byte_unpack(n, position)

	def parseInteger(self, n, position):
		self.bytes = Unpacker.four_byte_unpack(n, position)

	def parseFloat(self, n, position):
		self.bytes = Unpacker.four_byte_unpack(n, position)

	def parseLong(self, n, position):
		self.high_bytes = Unpacker.four_byte_unpack(n, position)
		self.low_bytes = Unpacker.four_byte_unpack(n, position)

	def parseDouble(self, n, position):
		self.high_bytes = Unpacker.four_byte_unpack(n, position)
		self.low_bytes = Unpacker.four_byte_unpack(n, position)

	def parseNameAndType(self, n, position):
		self.name_index = Unpacker.two_byte_unpack(n, position)
		self.descriptor_index = Unpacker.two_byte_unpack(n, position)

	def parseUTF8(self, n, position):
		self.length = Unpacker.two_byte_unpack(n, position)
		self.string = Unpacker.UTF8_tuple(n, position, self.length)

	def parseMethodHandle(self, n, position):
		self.reference_kind = Unpacker.single_byte_unpack(n, position)
		self.reference_index = Unpacker.two_byte_unpack(n, position)

	def parseMethodType(self, n, position):
		self.descriptor_index = Unpacker.two_byte_unpack(n, position)

	def parseInvokeDynamic(self, n, position):
		self.bootstrap_method_attr_index = Unpacker.two_byte_unpack(n, position)
		self.name_and_type_index = Unpacker.two_byte_unpack(n, position)