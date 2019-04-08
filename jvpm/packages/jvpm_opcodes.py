"""Read bit stream."""
from collections import defaultdict
from collections import deque
from . import jvpm_dict, jvpm_methods  # import external opcode dictionary

# A deque of invokevirtual constants used for method calls from AddToo.class.
#     Eventually wee will acquire these values from the CP, but they are hardcoded for now.
INVOKEVIRTUAL_CONST = deque(["5", "5", "7"])

# ****************************************************************************************

class HeaderClass():
    """Class that parses the header data from .class file and assigns values to variables."""
    def __init__(self, name="jvpm/javafiles/AddTwo.class"):
        with open(name, 'rb') as binary_file:
            self.data = binary_file.read()
            self.temp_2 = defaultdict(list)
            # print("\nFile opened: " + name)

    def get_magic(self):
        """Get magic from .class file."""
        # print("\nFile opened: " + self.name)
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print("Magic: ", magic)
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

#     def ten_to_fourteen(self):
#         """CP algorithm."""
#         temp = defaultdict(list)
#         temp[i].append(format(self.data[10 + i + position], '02x'))
#         temp[i].append(format(self.data[11 + i + position] +
#                               self.data[12 + i + position] +
#                               self.data[13 + i + position] +
#                               self.data[14 + i + position], '02x'))

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
                # self.ten_to_fourteen()
                position += 4
            # Float
            elif self.data[data_offset] == 4:
                # self.ten_to_fourteen()
                position += 4
            # Long
            elif self.data[data_offset] == 5:
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
            elif self.data[data_offset] == 6:
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
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
                position += 4
            # Name and Type
            elif self.data[data_offset] == 12:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] +
                                      self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] +
                                      self.data[14 + i + position], '02x'))
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
        # Eventually we will acquire these values from the CP, but they are hardcoded for now.
        self.opcodes = ['2a', '59', '4c', '2b', 'b6', '3d', 'b6', '3e', '1c', '1d', '60', 'b6']

        """


        METHOD GOES HERE TO FIND OPCODES FROM ANY .CLASS FILE AND SAVE TO self.opcodes LIST.



        """

    def dict_search(self):
        """dictionary search method."""
        print("Method Opcodes called from the .class file: \n" + str(self.opcodes))
        index = 0
        while index < len(self.opcodes):
            opcall = jvpm_dict.get_opcode(self.opcodes[index])
            # print(opcall) # just to see what opcall is passed through
            jvpm_methods.OpCodeMethods().token_dict(opcall)
            index += 1
        # print()

    def get_opcode_bytes():
        input_file = input("Enter class filename - type 'helloworld': ")
        data = []
        if input_file.upper() == "HELLOWORLD":
            with open("jvpm/javafiles/HelloWorld.class",'rb') as binary_file:
                # opcode_bytes = binary_file[336:343]
                op_bytes = binary_file.read()
                return op_bytes[336:343]
        if input_file.upper() == "TESTPRINTLINE":    
            with open("jvpm/javafiles/testPrintLine.class",'rb') as binary_file:
                opcode_bytes = binary_file[362:369]
                return opcode_bytes
            
    # ****************************************************************************************

