"""import the unittest"""
import unittest
import stack

# from collections import namedtuple
from bitstring import ConstBitStream
#from pythonds.basic.stack import Stack


# pylint: disable = W0105, C0122
class HeaderClass():

    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print("Magic: ", magic)
        return magic

    def get_minor(self):
        print("Minor: ", self.data[4] + self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        print("Major: ", self.data[6] + self.data[7])
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        # print("Contant Pool Count: ", self.data[8] + self.data[9])
        return self.data[8] + self.data[9]

    def get_const_pool(self):
        temp = []
        count = self.get_const_pool_count() - 1
        for i in range(count):
            temp.append((format(self.data[10 + i]), '02X'))
        print("Constant Pool Length: ", len(temp))
        print(temp)
        return temp

    def get_access_flags(self):
        holder = self.get_const_pool_count() + 9
        print("Access Flags: ", self.data[holder] + self.data[holder + 1])
        print(format(self.data[holder], '02X'))
        print(format(self.data[holder + 1], '02X'))
        return self.data[holder] + self.data[holder + 1]
        
    def get_this_class(self):
        holder = self.get_const_pool_count() + 9
        print("This Class: ", self.data[holder + 2] + self.data[holder + 3])
        print(format(self.data[holder + 2], '02X'))
        print(format(self.data[holder + 3], '02X'))
        return self.data[holder + 2] + self.data[holder + 3]

    def get_super_class(self):
        holder = self.get_const_pool_count() + 9
        print("Super Class: ", self.data[holder + 4] + self.data[holder + 5])
        print(format(self.data[holder + 4], '02X'))
        print(format(self.data[holder + 5], '02X'))
        return self.data[holder + 4] + self.data[holder + 5]

    def get_interfaces_count(self):
        holder = self.get_const_pool_count() + 9
        print("Interfaces Count: ", self.data[holder + 6] + self.data[holder + 7])
        print(format(self.data[holder + 6], '02X'))
        print(format(self.data[holder + 7], '02X'))
        return self.data[holder + 6] + self.data[holder + 7]

    def get_interfaces(self):
        temp = []
        count = self.get_interfaces_count()
        index = self.get_const_pool_count() + 16
        for i in range(count):
            temp.append(format(self.data[index + i], '02X'))
        print("Interfaces Length: ", len(temp))
        print(temp)
        # return temp

    def get_fields_count(self):
        holder = self.get_const_pool_count() + self.get_interfaces_count() + 16
        print(format(self.data[holder], '02X'))
        print(format(self.data[holder + 1], '02X'))
        return self.data[holder] + self.data[holder + 1]

    def get_fields(self):
        temp = []
        count = self.get_fields_count()
        index = self.get_const_pool_count() + self.get_interfaces_count() + 18
        for i in range(count):
            temp.append(format(self.data[index + i], '02X'))
        print("Fields Length: ", len(temp))
        print(temp)
        return temp

    def get_methods_count(self):
        holder = self.get_const_pool_count() + self.get_interfaces_count() + self.get_fields_count() + 14
        print(format(self.data[holder], '02X'))
        print(format(self.data[holder + 1], '02X'))
        return self.data[holder] + self.data[holder + 1]

    def get_methods(self):
        temp = []
        count = self.get_methods_count()
        index = self.get_const_pool_count() + self.get_interfaces_count() + self.get_fields_count() + 16
        print("index = " + str(index))
        for i in range(count):
            temp.append(format(self.data[index + i], '02X'))
        print("Methods Length: ", len(temp))
        print(temp)
        print(temp[151], temp[152], temp[153]) # 04, 3c, 84
        return temp

    def get_attributes_count(self):
        holder = self.get_const_pool_count() + self.get_interfaces_count() + self.get_fields_count() + self.get_methods_count() + 20
        print(format(self.data[holder], '02X'))
        print(format(self.data[holder + 1], '02X'))
        return self.data[holder] + self.data[holder + 1]

    def get_attributes(self):
        temp = []
        count = self.get_attributes_count()
        index = self.get_const_pool_count() + self.get_interfaces_count() + self.get_fields_count() + self.get_methods_count() + 22
        for i in range(count):
            temp.append(format(self.data[index + i], '02X'))
        print("Attributes Length: ", len(temp))
        print(temp)
        return temp

if '__main__' == __name__:
    d = HeaderClass()
    d.get_magic()
    d.get_minor()
    d.get_major()
    d.get_const_pool()
    d.get_access_flags()
    d.get_this_class()
    d.get_super_class()
    d.get_interfaces_count()
    d.get_interfaces()
    d.get_fields_count()
    d.get_fields()
    d.get_methods_count()
    d.get_methods()
    d.get_attributes_count()
    d.get_attributes()
    
