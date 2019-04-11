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
    def __init__(self, name="jvpm/javafiles/Test.class"):
        self.name = name
        add_one_byte = 1
        constant_pool_byte_size = 0
        with open(name, 'rb') as binary_file:
            self.data = binary_file.read()
            self.temp_2 = defaultdict(list)
            self.constant_pool = defaultdict(list)
            self.constant_pool_byte_size = 0
            self.constant_pool_total_size = 0
            self.constant_pool_indexes = []
            self.skips_in_constant_pool = 0
            self.add_one_byte = 1
            self.reader_location = 0
            self.integer_interface_count = 0
            self.integer_field_count = 0
            self.integer_method_count = 0

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        return magic

    def get_minor(self):
        return self.data[4] + self.data[5]

    def get_major(self):
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        return self.data[8] + self.data[9]

    def get_const_pool(self):

        self.constant_pool_size = self.get_const_pool_count()

        index = 1

        total_bytes = 0
        current_byte_location = 10

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
        while index < self.constant_pool_size:
            skip_index = str(self.data[current_byte_location])
            self.constant_pool[index].append(format(self.data[current_byte_location], '02x'))
            if self.data[current_byte_location] == 1:
                bytes_to_read = int(self.data[current_byte_location + 1] + self.data[current_byte_location + 2]) + 2
                byte_index = 1
                while byte_index <= bytes_to_read:
                    self.constant_pool[index].append(format(self.data[current_byte_location + byte_index], '02x'))
                    byte_index += 1
                total_bytes += 1
                index += 1
                current_byte_location += bytes_to_read + 1

            else:
                bytes_to_read = const_pool_var_dict[str(self.data[current_byte_location])]
                byte_index = 1
                while byte_index <= bytes_to_read:
                    empty_byte = format(self.data[current_byte_location + byte_index], '02x')
                    if (empty_byte == '00'):
                        byte_index += 1
                    self.constant_pool[index].append(format(self.data[current_byte_location + byte_index], '02x'))

                    byte_index += 1
                total_bytes += 1

                index += 1
                current_byte_location += bytes_to_read + 1
            if (skip_index == "5" or skip_index == "6"):
                index += 1
                self.skips_in_constant_pool += 1
        self.reader_location = current_byte_location
        self.constant_pool_byte_size = current_byte_location -10
        self.temp_2 = self.constant_pool
        #print(self.constant_pool)

        return self.constant_pool

    def get_access_flags(self):
        access_flag_position = self.reader_location
        access_flag = [format((self.data[access_flag_position]) , "02x")]
        access_flag.append(format((self.data[access_flag_position + self.add_one_byte]), "02x"))
        self.reader_location += 2

        return access_flag

    def get_this_class(self):
        this_class = [format((self.data[self.reader_location]) , "02x")]
        this_class.append(format((self.data[self.reader_location + self.add_one_byte]), "02x"))
        self.reader_location += 2
        return this_class

    def get_super_class(self):
        super_class = [format((self.data[self.reader_location]) , "02x")]
        super_class.append(format((self.data[self.reader_location + self.add_one_byte]), "02x"))
        self.reader_location += 2
        return super_class

    def get_interfaces_count(self):
        interface_count = [format((self.data[self.reader_location]) , "02x")]
        interface_count.append(format((self.data[self.reader_location + self.add_one_byte]), "02x"))
        self.integer_interface_count = (self.data[self.reader_location]) + (self.data[self.reader_location + self.add_one_byte])
        self.reader_location += 2
        return interface_count

    def get_interface(self):
        if (self.integer_interface_count == 0):
            print ("interface table empty")
            #self.reader_location += 2


    def get_field_count(self):
        field_count = [format((self.data[self.reader_location]) , "02x")]
        field_count.append(format((self.data[self.reader_location + self.add_one_byte]), "02x"))
        self.integer_field_count = (self.data[self.reader_location]) + (self.data[self.reader_location + self.add_one_byte])
        self.reader_location += 2
        return field_count


    def get_field(self):
        if (self.integer_field_count == 0):
            print("field table empty")


    def get_methods_count(self):
        method_count = [format((self.data[self.reader_location]) , "02x")]
        method_count.append(format((self.data[self.reader_location + self.add_one_byte]), "02x"))
        self.integer_method_count = (self.data[self.reader_location]) + (self.data[self.reader_location + self.add_one_byte])
        self.reader_location += 2
        return method_count

    def get_methods(self):
        if (self.integer_method_count == 0):
            print("method table empty")


    def get_attributes_count(self):
        print("temp")

    def get_attributes(self):
        print("temp")

    def PrintHeader(self): # pragma: no cover
        print("Magic: " + self.get_magic())
        print("Major:", self.get_major())
        print("Minor:", self.get_minor())
        print("Constant_pool_count:", self.get_const_pool_count())

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
