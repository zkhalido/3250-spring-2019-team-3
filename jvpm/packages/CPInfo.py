from enum import Enum
from .Unpacker import Unpacker
import struct

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
		tag = struct.unpack('!B', r.read(1))

		self.tag = ConstTag(tag)

		if self.tag == ConstTag.CLASS
			self.parseClass(n)
		if self.tag == ConstTag.FIELD
			self.parseField(n)
		if self.tag == ConstTag.METHOD
			self.parseMethod(n)
		if self.tag == ConstTag.INTERFACE
			self.parseInterface(n)
		if self.tag == ConstTag.STRING
			self.parseString(n)
		if self.tag == ConstTag.INTEGER
			self.parseInteger(n)
		if self.tag == ConstTag.FLOAT
			self.parseFloat(n)
		if self.tag == ConstTag.LONG
			self.parseLong(n)
		if self.tag == ConstTag.NAME_AND_TYPE
			self.parseNameAndType(n)
		if self.tag == ConstTag.UTF8
			self.parseUTF8(n)
		if self.tag == ConstTag.METHOD_HANDLE
			self.parseMethodHandle(n)
		if self.tag == ConstTag.METHOD_TYPE
			self.parseMethodType(n)
		if self.tag == ConstTag.INVOKE_DYNAMIC
			self.parseInvokeDynamic(n)

	def parseClass(self, n):
		self.name_index = struct.unpack('!H', self.data.read(2))

	def parseField(self, n):
		self.class_index = struct.unpack('!H', self.data.read(2))
		self.name_and_type_index = struct.unpack('!H', self.data.read(2))

	def parseMethod(self, n):
		self.class_index = struct.unpack('!H', self.data.read(2))
		self.name_and_type_index = struct.unpack('!H', self.data.read(2))

	def parseInterface(self, n):
		self.class_index = struct.unpack('!H', self.data.read(2))
		self.name_and_type_index = struct.unpack('!H', self.data.read(2))

	def parseString(self, n):
		self.string_index = struct.unpack('!H', self.data.read(2))

	def parseInteger(self, n):
		self.bytes = struct.unpack('!I', self.data.read(4))

	def parseFloat(self, n):
		self.bytes = struct.unpack('!I', self.data.read(4))

	def parseLong(self, n):
		self.high_bytes = struct.unpack('!I', self.data.read(4))
		self.low_bytes = struct.unpack('!I', self.data.read(4))

	def parseDouble(self, n):
		self.high_bytes = struct.unpack('!I', self.data.read(4))
		self.low_bytes = struct.unpack('!I', self.data.read(4))

	def parseNameAndType(self, n):
		self.name_index = struct.unpack('!H', self.data.read(2))
		self.descriptor_index = struct.unpack('!H', self.data.read(2))

	def parseUTF8(self, n):
		self.length = struct.unpack('!H', self.data.read(2))
		self.string = struct.unpack('!s'.format(self.length), self.data.read(self.length))

	def parseMethodHandle(self, n):
		self.reference_kind = struct.unpack('!B', r.read(1))
		self.reference_index = struct.unpack('!H', self.data.read(2))

	def parseMethodType(self, n):
		self.descriptor_index = struct.unpack('!H', self.data.read(2))

	def parseInvokeDynamic(self, n):
		self.bootstrap_method_attr_index = struct.unpack('!H', self.data.read(2)).decode('utf-8')
		self.name_and_type_index = struct.unpack('!H', self.data.read(2))