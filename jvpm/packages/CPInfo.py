from enum import Enum
from bitstring import ConstBitStream
import struct

class ConstTag(Enum):
    CLASS = "07"
    FIELD = "09"
    METHOD = "0a"
    INTERFACE = "0b"
    STRING = "08"
    INTEGER = "03"
    FLOAT = "04"
    LONG = "05"
    DOUBLE = "06"
    NAME_AND_TYPE = "0c"
    UTF8 = "01"
    METHOD_HANDLE = "0f"
    METHOD_TYPE = "10"
    INVOKE_DYNAMIC = "12"

class ConstInfo:

    def __init__(self):
        self.tag = None
        self.pool = []

    def read(self, bits):
        #pool = []
        tag = bits.read('hex:8')
        print(int(tag,16), "  iinnntt")
        self.pool.append(tag)
        print (tag, "%%%%%%%%%%%%%%%%tag")
        self.tag = ConstTag(tag)
        print(self.tag, "^^^^^^^^^^^^^^^^^^^ self.tag")

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
        #print(self.class_index, " ^^^^^^^^^^^self")
        return self.pool

    def parseClass(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))


    def parseField(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseMethod(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseInterface(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseString(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseInteger(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseFloat(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseLong(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))


    def parseDouble(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseNameAndType(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseUTF8(self, bits):
        self.length = bits.read('uint:16')

        self.pool.append(bits.read('bytes:(%d)' % self.length).decode('utf-8'))

    def parseMethodHandle(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseMethodType(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))

    def parseInvokeDynamic(self, bits):
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))
        self.pool.append (bits.read('hex:8'))