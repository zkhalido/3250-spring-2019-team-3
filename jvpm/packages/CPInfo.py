from enum import Enum
from bitstring import ConstBitStream
import struct

class ConstTag(Enum):
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
        self.tag = None

    def read(self, n):
        tag = n.read('uint:8')
        self.tag = ConstTag(tag)

        if self.tag == ConstTag.CLASS:
            self.parseClass(n)
        elif self.tag == ConstTag.FIELD:
            self.parseField(n)
        elif self.tag == ConstTag.METHOD:
            self.parseMethod(n)
        elif self.tag == ConstTag.INTERFACE:
            self.parseInterface(n)
        elif self.tag == ConstTag.STRING:
            self.parseString(n)
        elif self.tag == ConstTag.INTEGER:
            self.parseInteger(n)
        elif self.tag == ConstTag.FLOAT:
            self.parseFloat(n)
        elif self.tag == ConstTag.LONG:
            self.parseLong(n)
        elif self.tag == ConstTag.DOUBLE:
            self.parseDouble(n)
        elif self.tag == ConstTag.NAME_AND_TYPE:
            self.parseNameAndType(n)
        elif self.tag == ConstTag.UTF8:
            self.parseUTF8(n)
        elif self.tag == ConstTag.METHOD_HANDLE:
            self.parseMethodHandle(n)
        elif self.tag == ConstTag.METHOD_TYPE:
            self.parseMethodType(n)
        elif self.tag == ConstTag.INVOKE_DYNAMIC:
            self.parseInvokeDynamic(n)

        return self

    def parseClass(self, n):
        self.name_index = n.read('uint:16')

    def parseField(self, n):
        self.class_index = n.read('uint:16')
        self.name_and_type_index = n.read('uint:16')

    def parseMethod(self, n):
        self.class_index = n.read('uint:16')
        self.name_and_type_index = n.read('uint:16')

    def parseInterface(self, n):
        self.class_index = n.read('uint:16')
        self.name_and_type_index = n.read('uint:16')

    def parseString(self, n):
        self.string_index = n.read('uint:16')

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
        self.name_index = n.read('uint:16')
        self.descriptor_index = n.read('uint:16')

    def parseUTF8(self, n):
        self.length = n.read('uint:16')
        self.string = n.read('bytes:(%d)' % self.length).decode('utf-8')

    def parseMethodHandle(self, n):
        self.reference_kind = n.read('uint:8')
        self.reference_index = n.read('uint:16')

    def parseMethodType(self, n):
        self.descriptor_index = struct.unpack('!H', self.data.read(2))

    def parseInvokeDynamic(self, n):
        self.bootstrap_method_attr_index = struct.unpack('!H', self.data.read(2)).decode('utf-8')
        self.name_and_type_index = struct.unpack('!H', self.data.read(2))