"""Read bit stream."""
from collections import defaultdict
from collections import deque
from . import jvpm_dict, jvpm_methods  # import external opcode dictionary

# a deque of invokevirtual constants used for method calls.
INVOKEVIRTUAL_CONST = deque(["5", "5", "7"])

# ****************************************************************************************

class HeaderClass():
    """Class that parses the header data from .class file and assigns values to variables."""
    def __init__(self, name="jvpm/javafiles/test.class"):
        with open(name, 'rb') as binary_file:
            self.data = binary_file.read()
            self.temp_2 = defaultdict(list)

    def get_magic(self):
        """Get magic from .class file."""
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print("\nMagic: ", magic)
        return magic

    def get_minor(self):
        """Get minor from .class file."""
        print("Minor: ", self.data[4] + self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        """Get major from .class file."""
        print("Major: ", self.data[6] + self.data[7])
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        """Get CP count from .class file."""
        return self.data[8] + self.data[9]
    
    def ten_to_fourteen(self):
        """CP algorithm."""
        temp[i].append(format(self.data[10 + i + position], '02x'))
        temp[i].append(format(self.data[11 + i + position] +
                              self.data[12 + i + position] +
                              self.data[13 + i + position] +
                              self.data[14 + i + position], '02x'))
        
    def ten_to_fourteen_B(self):
        temp[i].append(format(self.data[10 + i + position], '02x'))
        temp[i].append(format(self.data[11 + i + position] +
                              self.data[12 + i + position], '02x'))
        temp[i].append(format(self.data[13 + i + position] +
                              self.data[14 + i + position], '02x'))
        
    def ten_to_eighteen(self):
        temp[i].append(format(self.data[10 + i + position], '02x'))
        temp[i].append(format(self.data[11 + i + position] +
                              self.data[12 + i + position] +
                              self.data[13 + i + position] +
                              self.data[14 + i + position], '02x'))
        temp[i].append(format(self.data[15 + i + position] +
                              self.data[16 + i + position] +
                              self.data[17 + i + position] +
                              self.data[18 + i + position], '02x'))

    def get_const_pool(self):
        """Get CP from .class file."""
        temp = defaultdict(list)
        start_of_cp = 10
        position = 0
        count = self.get_const_pool_count() - 1
        for i in range(count):
            data_offset = start_of_cp + i + position
            # Utf_8
            if self.data[data_offset] == 1:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                for j in range(self.data[11 + i + position] + self.data[12 + i + position]):
                    temp[i].append(format(self.data[13 + i + position + j], '02x'))
                position += (self.data[11 + i + position] + self.data[12 + i + position])
                position += 2
            # Integer
            elif self.data[data_offset] == 3:
                self.ten_to_fourteen()
                position += 4
            # Float
            elif self.data[data_offset] == 4:
                self.ten_to_fourteen()
                position += 4
            # Long
            elif self.data[data_offset] == 5:
                self.ten_to_eighteen()
                position += 8
            # Double
            elif self.data[data_offset] == 6:
                self.ten_to_eighteen()
                position += 8
            # Pulling class info
            elif self.data[data_offset] == 7:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                position += 2
            # String
            elif self.data[data_offset] == 8:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                position += 4
            # Field Ref
            elif self.data[data_offset] == 9:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # Method Ref
            elif self.data[data_offset] == 10:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # Interface Method Ref
            elif self.data[data_offset] == 11:
                self.ten_to_fourteen_B()
                position += 4
            # Name and Type
            elif self.data[data_offset] == 12:
                self.ten_to_fourteen_B()
                position += 4
            # Method Handle
            elif self.data[data_offset] == 15:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position], '02x'))
                temp[i].append(format(self.data[12 + i + position] +
                                      self.data[13 + i + position], '02x'))
                position += 3
            # Method Type
            elif self.data[data_offset] == 16:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                position += 2
            # Invoke Dynamic
            elif self.data[data_offset] == 18:
                self.ten_to_fourteen_B()
                position += 4
        self.temp_2 = temp
        return temp

# **************************************************************************************************

class OpCodes():

    """Parse Opcodes into an array from the .class file, search the external dictionary of
    opcodes, and implement the methods using the external dictionary of methods."""
    def __init__(self):
        self.opcodes = ['1a', '3b', '1a', '3c', 'b6', '3d', 'b6', '3e', '1c', '1d', '60', 'b6']

        """


        METHOD GOES HERE TO FIND OPCODES FROM ANY .CLASS FILE AND SAVE TO self.opcodes LIST.



        """

    def dict_search(self):
        """dictionary search method."""
        print("Method Opcodes from the .class file: \n" + str(self.opcodes))
        index = 0
        while index < len(self.opcodes):
            opcall = jvpm_dict.get_opcode(self.opcodes[index])
            # print(opcall) # just to see what opcall is passed through
            jvpm_methods.OpCodeMethods().token_dict(opcall)
            index += 1
        print()
        
# ****************************************************************************************
