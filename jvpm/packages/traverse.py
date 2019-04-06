"""import the unittest"""
import unittest
import stack

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
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        #print("Magic: ", magic)
        return magic

    def get_minor(self):
        #print("Minor: ", self.data[4] + self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        #print("Major: ", self.data[6] + self.data[7])
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        # print("Contant Pool Count: ", self.data[8] + self.data[9])
        return self.data[8] + self.data[9]
    

    
    def get_const_pool(self):
        
        def temp_append(self, extra_offset, current_offset):
            to_append = 0
            if type(extra_offset) == list:
                for offset in extra_offset:
                    to_append += self.data[current_offset + offset]
                to_append = format(to_append, '02x')
            else:
                to_append = format(self.data[current_offset + extra_offset], '02x')
            return to_append
        
        START_OF_CONSTANT_POOL = 10
        
        CLASS_REFERENCE = 7
        FIELD_REFERENCE = 9
        METHOD_REFERENCE = 10
        INTERFACE_METHOD_REFERENCE = 11
        STRING_REFERENCE = 8
        INTEGER = 3
        FLOAT = 4
        LONG = 5
        DOUBLE = 6
        NAME_AND_TYPE = 12
        UTF8_STRING = 1
        METHOD_HANDLE = 15
        METHOD_TYPE = 16
        INVOKE_DYNAMIC = 18
        MODULE = 19
        
        
        some_array = []
        
        constant_dict = {
               CLASS_REFERENCE: [[0, [1, 2]], 2],
               FIELD_REFERENCE: [[0, [1, 2], [3, 4]], 4],
               METHOD_REFERENCE: [[0, [1, 2], [3,4]], 4],
               INTERFACE_METHOD_REFERENCE: [[0, [1, 2], [3, 4]], 4],
               STRING_REFERENCE: [[0, [1, 2]], 4],
               INTEGER: [[0, [1, 2, 3, 4]], 4],
               FLOAT: [[0, [1, 2, 3, 4]], 4],
               LONG: [[0, [1, 2, 3, 4], [5, 6, 7, 8]], 8],
               DOUBLE: [[0, [1, 2, 3, 4], [5, 6, 7, 8]], 8],
               NAME_AND_TYPE: [[0, [1, 2], [3, 4]], 4],
               UTF8_STRING: [[0, [1, 2], some_array], 2],  ####### SPECIAL CASE
               METHOD_HANDLE: [[0, 1, [2, 3]], 3],
               METHOD_TYPE: [[0, [1, 2]], 2],
               INVOKE_DYNAMIC: [[0,[1, 2], [3, 4]], 4],
               MODULE: [[],2]
                }
        
        temp = defaultdict(list)
        count = self.get_const_pool_count() - 1
        for i in range(count):
<<<<<<< HEAD
            # Pulling class info
            if self.data[10 + i + position] == 7:
                temp[i] = single_part_tuple(self, 10 + i + position)
                position += 2
            # Field Ref
            elif self.data[10 + i + position] == 9:
                temp[i] = double_part_tuple(self, 10 + i + position)
                position += 4
            # Method Ref
            elif self.data[10 + i + position] == 10:
                temp[i] = double_part_tuple(self, 10 + i + position)
                position += 4
            # Interface Method Ref
            elif self.data[10 + i + position] == 11:
                temp[i] = double_part_tuple(self, 10 + i + position)
                position += 4
            # String
            elif self.data[10 + i + position] == 8:
                temp[i] = single_part_tuple(self, 10 + i + position)
                position += 4
            # Integer
            elif self.data[10 + i + position] == 3:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position] +
                    self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # Float
            elif self.data[10 + i + position] == 4:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position] +
                    self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # Long
            elif self.data[10 + i + position] == 5:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position] +
                    self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                temp[i].append(format(self.data[15 + i + position] + self.data[16 + i + position] +
                    self.data[17 + i + position] + self.data[18 + i + position], '02x'))
                position += 8
            # Double
            elif self.data[10 + i + position] == 6:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position] +
                    self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                temp[i].append(format(self.data[15 + i + position] + self.data[16 + i + position] +
                    self.data[17 + i + position] + self.data[18 + i + position], '02x'))
                position += 8
            # Name and Type
            elif self.data[10 + i + position] == 12:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # Utf_8
            elif self.data[10 + i + position] == 1:
=======
            DATA_OFFSET = START_OF_CONSTANT_POOL + position + i
            if self.data[DATA_OFFSET] == UTF8_STRING:
>>>>>>> f98f492b4039b9d349b544f7d9858b3ba1d198a2
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                for f in range (self.data[11 + i + position] + self.data[12 + i + position]):
                    temp[i].append(format(self.data[13 + i + position + f], '02x'))
                position += (self.data[11 + i + position] + self.data[12 + i + position])
                position += 2
            else:
                for extra_offset in constant_dict[self.data[DATA_OFFSET]][0]:
                    temp[i].append(temp_append(self, extra_offset, DATA_OFFSET))
                position += constant_dict[self.data[DATA_OFFSET]][1]
        return temp

    

    def get_access_flags(self):
        holder = position + 24
        #print("Access Flags: ", self.data[holder] + self.data[holder + 1])
        #print(format(self.data[holder], '02X'))
        #print(format(self.data[holder + 1], '02X'))
        return self.data[holder] + self.data[holder + 1]

    def get_this_class(self):
        holder = position + 24
        #print("This Class: ", self.data[holder + 2] + self.data[holder + 3])
        #print(format(self.data[holder + 2], '02X'))
        #print(format(self.data[holder + 3], '02X'))
        return self.data[holder + 2] + self.data[holder + 3]

    def get_super_class(self):
        holder = position + 24
        #print("Super Class: ", self.data[holder + 4] + self.data[holder + 5])
        #print(format(self.data[holder + 4], '02X'))
        #print(format(self.data[holder + 5], '02X'))
        return self.data[holder + 4] + self.data[holder + 5]

    def get_interfaces_count(self):
        holder = position + 25
        #joined = ''.join([format(self.data[holder + 6], '02X'), format(self.data[holder + 7], '02X')])
        #print(joined)
        #intj = int(joined)
        #hexi = hex(intj)
        # print(hexi)
        #print("Interfaces Count: " + hexi)
        #print(format(self.data[holder + 6], '02X'))
        #print(format(self.data[holder + 7], '02X'))
        return self.data[holder + 6] + self.data[holder + 7]
    
    
    def get_interfaces(self):
        temp = []
        count = self.get_interfaces_count()
        index = position + 16
        for i in range(count):
            temp.append(format(self.data[index + i], '02X'))
        #print("Interfaces Length: ", len(temp))
        #print(temp)
        return temp

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
