import unittest
from unittest.mock import mock_open, patch

class ClassFile():
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print('hexprint ' + hex(self.data[0]))
        print('magic ' + magic)
        return magic

    def get_minor(self):
        print("minor", self.data[4], self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        print("major", self.data[6], self.data[7])
        return self.data[6] + self.data[7]

    def get_poolCount(self):
        print("count", self.data[8], self.data[9])
        return self.data[8]+ self.data[9]

class OpCodes():
    def __init__(self):
        self.table = {0x00: self.not_implemented}

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value):
        return self.table[value]()

class TestClassFile(unittest.TestCase):
    def setUp(self):
        m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x00\x37\x00\x0F')
        with patch(__name__ + '.open', m):
            self.cf = ClassFile()

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')
        print("unittestmagic", self.cf.get_magic())

    def test_minor(self):
        self.assertEqual(self.cf.get_minor(), 0)
        print("unittestprintminor", self.cf.get_minor())

    def test_major(self):
        self.assertEqual(self.cf.get_major(), 55)
        print("unittestprintmajor", self.cf.get_major())

    def test_PoolCount(self):
        self.assertEqual(self.cf.get_poolCount(), 15)
        print("unittestprintpool", self.cf.get_poolCount())

class TestOpCodes(unittest.TestCase):
    def test_not_implmented(self):
        self.assertEqual(OpCodes().interpret(0), 'not implemented')
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
