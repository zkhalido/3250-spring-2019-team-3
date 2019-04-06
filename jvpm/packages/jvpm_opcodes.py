"""Read bit stream."""
from collections import defaultdict
from . import jvpm_dict, jvpm_methods  # import external opcode dictionary
from collections import deque

# a deque of invokevirtual constants used for method calls.
inv_virt_const = deque(["5", "5", "7"])

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

    def get_const_pool(self):
        """Get CP from .class file."""
        temp = defaultdict(list)
        position = 0
        count = self.get_const_pool_count() - 1
        for i in range(count):
            # Pulling class info
            if self.data[10 + i + position] == 7:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                position += 2
            # Field Ref
            elif self.data[10 + i + position] == 9:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # Method Ref
            elif self.data[10 + i + position] == 10:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # Interface Method Ref
            elif self.data[10 + i + position] == 11:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # String
            elif self.data[10 + i + position] == 8:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                position += 4
            # Integer
            elif self.data[10 + i + position] == 3:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position] +
                                      self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # Float
            elif self.data[10 + i + position] == 4:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position] +
                                      self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # Long
            elif self.data[10 + i + position] == 5:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position] +
                                      self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                temp[i].append(format(self.data[15 + i + position] +
                                      self.data[16 + i + position] +
                                      self.data[17 + i + position] +
                                      self.data[18 + i + position], '02x'))
                position += 8
            # Double
            elif self.data[10 + i + position] == 6:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position] +
                                      self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                temp[i].append(format(self.data[15 + i + position] +
                                      self.data[16 + i + position] +
                                      self.data[17 + i + position] +
                                      self.data[18 + i + position], '02x'))
                position += 8
            # Name and Type
            elif self.data[10 + i + position] == 12:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # Utf_8
            elif self.data[10 + i + position] == 1:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                for j in range(self.data[11 + i + position] + self.data[12 + i + position]):
                    temp[i].append(format(self.data[13 + i + position + j], '02x'))
                position += (self.data[11 + i + position] + self.data[12 + i + position])
                position += 2

            # Method Handle
            elif self.data[10 + i + position] == 15:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position], '02x'))
                temp[i].append(format(self.data[12 + i + position] +
                                      self.data[13 + i + position], '02x'))
                position += 3
            # Method Type
            elif self.data[10 + i + position] == 16:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                position += 2
            # Invoke Dynamic
            elif self.data[10 + i + position] == 18:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
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
