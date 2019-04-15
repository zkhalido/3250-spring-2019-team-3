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

class ConstInfo:

    def __init__(self):
        self.tag = None

    def read(self, bits):
        tag = bits.read('uint:8')
        self.tag = ConstTag(tag)

        if self.tag == ConstTag.CLASS:
            self.parseClass(bits)
        elif self.tag == ConstTag.FIELD:
            self.parseField(bits)
        elif self.tag == ConstTag.METHOD:
            self.parseMethod(bits)
        elif self.tag == ConstTag.INTERFACE:
            self.parseInterface(bits)
        elif self.tag == ConstTag.STRING:
            self.parseString(bits)
        elif self.tag == ConstTag.INTEGER:
            self.parseInteger(bits)
        elif self.tag == ConstTag.FLOAT:
            self.parseFloat(bits)
        elif self.tag == ConstTag.LONG:
            self.parseLong(bits)
        elif self.tag == ConstTag.DOUBLE:
            self.parseDouble(bits)
        elif self.tag == ConstTag.NAME_AND_TYPE:
            self.parseNameAndType(bits)
        elif self.tag == ConstTag.UTF8:
            self.parseUTF8(bits)
        elif self.tag == ConstTag.METHOD_HANDLE:
            self.parseMethodHandle(bits)
        elif self.tag == ConstTag.METHOD_TYPE:
            self.parseMethodType(bits)
        elif self.tag == ConstTag.INVOKE_DYNAMIC:
            self.parseInvokeDynamic(bits)

        return self

    def parseClass(self, bits):
        self.name_index = bits.read('uint:16')

    def parseField(self, bits):
        self.class_index = bits.read('uint:16')
        self.name_and_type_index = bits.read('uint:16')

    def parseMethod(self, bits):
        self.class_index = bits.read('uint:16')
        self.name_and_type_index = bits.read('uint:16')

    def parseInterface(self, bits):
        self.class_index = bits.read('uint:16')
        self.name_and_type_index = bits.read('uint:16')

    def parseString(self, bits):
        self.string_index = bits.read('uint:16')

    def parseInteger(self, bits):
        self.bytes = bits.read(4)

    def parseFloat(self, bits):
        self.bytes = bits.read(4)

    def parseLong(self, bits):
        self.high_bytes = bits.read(4)
        self.low_bytes = bits.read(4)

    def parseDouble(self, bits):
        self.high_bytes = bits.read(4)
        self.low_bytes = bits.read(4)

    def parseNameAndType(self, bits):
        self.name_index = bits.read('uint:16')
        self.descriptor_index = bits.read('uint:16')

    def parseUTF8(self, bits):
        self.length = bits.read('uint:16')
        self.string = bits.read('bytes:(%d)' % self.length).decode('utf-8')

    def parseMethodHandle(self, bits):
        self.reference_kind = bits.read('uint:8')
        self.reference_index = bits.read('uint:16')

    def parseMethodType(self, bits):
        self.descriptor_index = bits.read('uint:16')

    def parseInvokeDynamic(self, bits):
        self.bootstrap_method_attr_index = bits.read('uint:16')
        self.name_and_type_index = bits.read('uint:16')