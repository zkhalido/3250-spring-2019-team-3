"""Read cp and opcodes."""
from collections import defaultdict
from bitstring import ConstBitStream
from . import jvpm_dict, jvpm_methods, read_attribute, CPInfo  # import external opcode dictionary
# pylint: disable=C0111, W0612, R0903, R0902

# ****************************************************************************************

class HeaderClass():
    """Class that parses the header data from .class file and assigns values to variables."""
    def __init__(self, name="jvpm/javafiles/test.class"):
        self.name = name
        self.bits = ConstBitStream(filename=name)
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
            self.methods_table = defaultdict(list)
            self.op_codes = []
            self.integer_attribute_count = 0
            self.field_count = 0
            self.field_dictionary = defaultdict(list)
        binary_file.close()

    def get_magic(self):
        magic = self.bits.read('hex:32')
        return magic

    def get_minor(self):
        return self.bits.read('hex:16')

    def get_major(self):
        return self.bits.read('hex:16')

    def get_const_pool_count(self):
        return self.bits.read('uint:16')

    def get_const_pool(self):
        constants_pool = defaultdict(list)
        constants_pool[0].append("base")
        const_pool_count = self.get_const_pool_count()
        const_pool_count -= 1
        i = 1
        while i <= const_pool_count:
            constant = CPInfo.ConstInfo().read(self.bits)
            constants_pool[i] = (constant)
            if constant[0] == "06" or constant[0] == "05":
                self.skips_in_constant_pool += 1
                i += 1
            i += 1
        self.reader_location = self.bits.bytepos
        self.constant_pool = constants_pool
        return constants_pool

    def get_access_flags(self):
        access_flag = self.class_file_item_reader_in_hex()
        return access_flag

    def get_this_class(self):
        this_class = self.class_file_item_reader_in_hex()
        return this_class

    def get_super_class(self):
        super_class = self.class_file_item_reader_in_hex()
        return super_class

    def get_interfaces_count(self):
        self.integer_interface_count = self.class_file_item_count_to_int()
        interface_count = self.class_file_item_reader_in_hex()
        return interface_count

    def get_interface(self):
        if self.integer_interface_count == 0:
            pass
            # print("interface table empty")

    def get_field_count(self):
        self.integer_field_count = self.class_file_item_count_to_int()
        field_count = self.class_file_item_reader_in_hex()
        self.field_count = field_count
        return field_count

    def get_field(self):
        if self.integer_field_count == 0:
            pass

    def get_methods_count(self):
        self.integer_method_count = self.class_file_item_count_to_int()
        method_count = self.class_file_item_reader_in_hex()
        return method_count

    def get_methods(self, pool):
        if self.integer_method_count == 0:
            pass
            #print("method table empty")

        method_index = 0
        while method_index < self.integer_method_count:
            ################# access flags
            self.method_table_traverse(method_index)
            self.reader_location += 2
            ################### name index
            self.method_table_traverse(method_index)
            self.reader_location += 2
            ################# discriptor index
            self.method_table_traverse(method_index)
            self.reader_location += 2
            ################## attribute count
            self.method_table_traverse(method_index)

            attribute_count = (self.data[self.reader_location]) + (self.data[self.reader_location +
                                                                             self.add_one_byte])
            self.reader_location += 2
            attribute_index = 0

            while attribute_index < attribute_count:
                tag_location = (self.data[self.reader_location]) + (self.data[self.reader_location +
                                                                              self.add_one_byte])
                tag = pool[tag_location]
                atribute_reader = read_attribute.ReadAttribute()
                pass_through_variables = []
                pass_through_variables.append(tag)
                pass_through_variables.append(self.methods_table)
                pass_through_variables.append(self.reader_location)
                pass_through_variables.append(self.data)
                pass_through_variables.append(self.op_codes)
                pass_through_variables.append(method_index)
                pass_through_variables.append(pool)
                returned_vals = atribute_reader.get_attribute(pass_through_variables)

                if isinstance(returned_vals, int):
                    self.reader_location = returned_vals
                else:
                    self.reader_location = int(returned_vals[0])
                    self.op_codes = returned_vals[1]
                attribute_index += 1
            method_index += 1
        return self.op_codes

    def class_file_item_count_to_int(self):
        count_as_int = (self.data[self.reader_location]) + (self.data[self.reader_location +
                                                                      self.add_one_byte])
        return count_as_int

    def class_file_item_reader_in_hex(self):
        class_file_item = [format((self.data[self.reader_location]), "02x")]
        class_file_item.append(format((self.data[self.reader_location + self.add_one_byte]), "02x"))
        self.reader_location += 2
        return class_file_item

    def method_table_traverse(self, method_index):
        self.methods_table[method_index].append(format((self.data[self.reader_location]),
                                                       "02x"))
        self.methods_table[method_index].append(format((self.data[self.reader_location
                                                                  + self.add_one_byte]), "02x"))
class OpCodes():
    """Parse Opcodes into an array from the .class file, search the external dictionary of
    opcodes, and implement the methods using the external dictionary of methods."""
    def __init__(self, opcode, constantpool):
        self.constantpool = constantpool
        self.opcode = opcode

    def dict_search(self):
        jvpm_methods_object = jvpm_methods.OpCodeMethods()
        i = 0
        while i < len(self.opcode):
            opcall = jvpm_dict.get_opcode(self.opcode[i])
            if opcall == "invokevirtual":
                op_location = int(self.opcode[i+2])
                opcall = self.constantpool[op_location]
                i += 2
            if opcall != "Byte code not found!":
                jvpm_methods_object.token_dict(opcall, self.opcode, self.constantpool,)
            i += 1

    # *****************************************************************************
