from collections import namedtuple
from bitstring import ConstBitStream
import unittest

class HeaderClass():
    from collections import namedtuple
from bitstring import ConstBitStream

class HeaderClass():
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print(magic)
        return magic

    def get_minor(self):
        print(self.data[4] + self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        print(self.data[6] + self.data[7])
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        print(self.data[8] + self.data[9])
        return self.data[8] + self.data[9]

    def get_const_pool(self):
        temp = []
        count = self.get_const_pool_count() - 1
        for i in range(count):
            temp.append((self.data[10 + i]))
        print(len(temp))
        return temp

    def get_access_flags(self):
    	holder = self.get_const_pool_count() + 8
    	print(self.data[holder] + self.data[holder + 1])
    	return self.data[holder] + self.data[holder + 1]
        

if '__main__' == __name__:
	d = HeaderClass()
	d.get_magic()
	d.get_minor()
	d.get_major()
	d.get_const_pool()
	d.get_access_flags()
