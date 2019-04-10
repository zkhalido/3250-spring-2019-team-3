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
        self.name = name
        with open(name, 'rb') as binary_file:
            self.data = binary_file.read()
            self.temp_2 = defaultdict(list)
            self.constant_pool = defaultdict(list)
            self.constant_pool_size = 0
            self.constant_pool_total_size = 0
            self.constant_pool_indexes = []


    def get_magic(self):
        """Get magic from .class file."""
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        return magic

    def get_minor(self):
        """Get minor from .class file."""
        return self.data[4] + self.data[5]

    def get_major(self):
        """Get major from .class file."""
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        """Get CP count from .class file."""
        return self.data[8] + self.data[9]

    def get_const_pool(self):

       self.constant_pool_size = self.get_const_pool_count()

       index = 0
       #index = 1

       bytes_to_read = 0
       total_bytes = 0
       start_of_pool = 10

       const_pool_var_dict = {
           "1": 2,  # 2+x bytes
           "3": 4,  # 4 bytes
           "4": 4,  # 4 bytes
           "5": 8,  # 8 bytes
           "6": 8,  # 8 bytes
           "7": 2,  # 2 bytes
           "8": 2,  # 2 bytes
           "9": 4,  # 4 bytes
           "10": 4,  # 4 bytes
           "11": 4,  # 4 bytes
           "12": 4,  # 4 bytes
           "15": 3,  # 3 bytes
           "16": 2,  # 2 bytes
           "17": 4,  # 4 bytes
           "18": 4,  # 4 bytes
           "19": 2,  # 2 bytes
           "20": 2,  # 2 bytes
       }
       #while index < self.constant_pool_size:
       while index < self.constant_pool_size-1:
           skip_index = str(self.data[start_of_pool])
           if (skip_index == "5" or skip_index == "6"):
               index += 1
           self.constant_pool[index].append(format(self.data[start_of_pool], '02x'))
           if self.data[start_of_pool] == 1:
               bytes_to_read = int(self.data[start_of_pool+1] + self.data[start_of_pool+2]) +2
               byte_index = 1
               while byte_index <= bytes_to_read:
                   self.constant_pool[index].append(format(self.data[start_of_pool + byte_index],'02x'))
                   byte_index += 1
               total_bytes += 1
               index += 1
               start_of_pool += bytes_to_read + 1

           else:
               bytes_to_read = const_pool_var_dict[str(self.data[start_of_pool])]
               byte_index = 1
               while byte_index < bytes_to_read:
                   self.constant_pool[index].append(format(self.data[start_of_pool+byte_index] + self.data[start_of_pool+byte_index +1], '02x'))
                   byte_index += 2
               total_bytes += 1
               index += 1
               start_of_pool += bytes_to_read + 1
       self.temp_2 = self.constant_pool

       return self.constant_pool

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
        for opcode in self.opcodes:
            opcall = jvpm_dict.get_opcode(opcode)
            jvpm_methods.OpCodeMethods().token_dict(opcall)
