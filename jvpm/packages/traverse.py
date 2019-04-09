"""import the unittest"""
import unittest
import stack
import struct

from collections import defaultdict
# from collections import namedtuple
# from bitstring import ConstBitStream
# from pythonds.basic.stack import Stack

# pylint: disable = W0105, C0122
class HeaderClass():

    def __init__(self):
        with open('../javafiles/testPrintLine.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = struct.unpack('!I', self.data.read(4))
        return magic

    def get_minor(self):
        #print("Minor: ", self.data[4] + self.data[5])
        return struct.unpack('!H', self.data.read(2))

    def get_major(self):
        #print("Major: ", self.data[6] + self.data[7])
        return struct.unpack('!H', self.data.read(2))

    def get_const_pool_count(self):
        # print("Contant Pool Count: ", self.data[8] + self.data[9])
        return struct.unpack('!H', self.data.read(2))
    

    
    def get_const_pool(self):
        
        constant_pool = []
        const_pool_count = get_const_pool_count()

        i = 1
        for i in range(const_pool_count):
            constants = CPInfo.read(self.data)
            constant_pool.append(constants)

            i + 1
        return constant_pool

    

    def get_access_flags(self):
        return struct.unpack('!H', self.data.read(2))

    def get_this_class(self):
        return struct.unpack('!H', self.data.read(2))

    def get_super_class(self):
        return struct.unpack('!H', self.data.read(2))

    def get_interfaces_count(self):
        return struct.unpack('!H', self.data.read(2))
    
    
    def get_interfaces(self):
        interface_class_names = []
        count = self.get_interfaces_count()
        for i in range(count):
            
        return interface_class_names

    def get_fields_count(self):
        holder = position + self.get_interfaces_count() + 33
        #print(format(self.data[holder], '02X'))
        #print(format(self.data[holder + 1], '02X'))
        return self.data[holder] + self.data[holder + 1]

    def get_fields(self):
        temp = []
        count = self.get_fields_count()
<<<<<<< HEAD:jvpm/jvpm.py
        index = position + self.get_interfaces_count() + 33
        for i in range(count):
            temp.append(format(self.data[index + i], '02X'))
        #print("Fields Length: ", len(temp))
        #print(temp)
=======
        index = self.get_const_pool_length() + self.get_interfaces_count() + 18
        if(count > 0):
            for i in range(count):
                 temp.append(format(self.data[index + i], '02X'))
            print("Fields Length: ", len(temp))
            print(temp)
        else:
            print("No interface table")
>>>>>>> efe2fe216147da0e585c21df952cf5d2af792f4d:jvpm/packages/traverse.py
        return temp

    def get_methods_count(self):
        holder = position + self.get_interfaces_count() + self.get_fields_count() + 35
        #print(format(self.data[holder], '02X'))
        #print(format(self.data[holder + 1], '02X'))
        return self.data[holder] + self.data[holder + 1]

    def get_methods(self):
        temp = []
        count = self.get_methods_count()
        index = position + self.get_interfaces_count() + self.get_fields_count() + 35
        print("index = " + str(index))
        if(count > 0):
            for i in range(count):
                temp.append(format(self.data[index + i], '02X'))
            print("Methods Length: ", len(temp))
            print(temp)
            print(temp[151], temp[152], temp[153], temp[154], temp[155]) # 04, 3c, 84, 01, 01
        else:
            print("No Methods")
        return temp

    def get_attributes_count(self):
        holder = position + self.get_interfaces_count() + self.get_fields_count() + self.get_methods_count() + 20
        print(format(self.data[holder], '02X'))
        print(format(self.data[holder + 1], '02X'))
        return self.data[holder] + self.data[holder + 1]

    def get_attributes(self):
        temp = []
        count = self.get_attributes_count()
        index = position + self.get_interfaces_count() + self.get_fields_count() + self.get_methods_count() + 22
        for i in range(count):
            temp.append(format(self.data[index + i], '02X'))
        print("Attributes Length: ", len(temp))
        print(temp)
        return temp

    def single_part_tuple(self, current):
        idNum = format(self.data[current], '02x')
        info = format(self.data[current + 1] + self.data[current + 2], '02x')
        temp = (idNum, info)
        return temp

    def single_part_long_tuple(self, current):
        idNum = format(self.data[current], '02x')
        info = self.data[11 + i + position] + self.data[12 + i + position] +
                    self.data[13 + i + position] + self.data[14 + i + position], '02x')
        temp = (idNum, info)
        return temp

    def double_part_tuple(self, current):
        idNum = format(self.data[current], '02x')
        info = format(self.data[current + 1] + self.data[current + 2], '02x')
        info2 = format(self.data[current + 3] + self.data[current + 4], '02x')
        temp = (idNum, info, info2)
        return temp

if '__main__' == __name__:
    d = HeaderClass()
    d.get_magic()
    d.get_minor()
    d.get_major()
    #print(d.get_const_pool())
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
