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
        self.pool.append(tag)
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
        return self.pool

    def parseClass(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)




    def parseField(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseMethod(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseInterface(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseString(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseInteger(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseFloat(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseLong(self, bits):
        for i in range(8):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)


    def parseDouble(self, bits):
        for i in range(8):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseNameAndType(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseUTF8(self, bits):
        self.pool.append(bits.read('hex:8'))
        self.pool.append(bits.read('hex:8'))
        bytes_to_read = int(self.pool[1], 16)+int(self.pool[2], 16)

        for i in range(bytes_to_read):
            next_byte = bits.read('hex:8')
            self.pool.append(next_byte)

    def parseMethodHandle(self, bits):
        for i in range(3):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseMethodType(self, bits):
        for i in range(2):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)

    def parseInvokeDynamic(self, bits):
        for i in range(4):
            next_byte = bits.read('hex:8')
            if (next_byte != "00"):
                self.pool.append(next_byte)