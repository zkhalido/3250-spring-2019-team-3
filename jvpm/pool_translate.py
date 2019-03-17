
from collections import defaultdict
import jvpm_opcodes



class PoolTranslate:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def UTF_8_string(self):
        print("UTF_8_string  2+x bytes (variable)")

    def integer(self):
        print("Integer  4 bytes")

    def float(self):
        print("Float  4 bytes")

    def long(self):
        print("Long    8 bytes")

    def double(self):
        print("Double    8 bytes")

    def class_reference(self):
        print("Double    2 bytes")

    def string_reference(self):
        print("Double    2 bytes")

    def field_reference(self):
        print("Field Reference    4 bytes")

    def method_reference(self):
        print("Method Reference    4 bytes")

    def interface_method_reference(self):
        print("Interface Method Reference    4 bytes")

    def name_and_type_discriptor(self):
        print("Name and Type Discriptor    4 bytes")

    def method_handle(self):
        print("Method Handle    3 bytes")

    def method_type(self):
        print("Method Type    2 bytes")

    def dynamic(self):
        print("Dynamic    4 bytes")

    def invoke_dynamic(self):
        print("Invoke Dynamic    4 bytes")

    def module(self):
        print("Module    2 bytes")

    def package(self):
        print("Package    2 bytes")



    switcher = {

        "01": UTF_8_string,  # add two ints
        "03": integer,  # add two ints
        "04": float,  # add two ints
        "05": long,  # add two ints
        "06": double,  # add two ints
        "07": class_reference,  # add two ints
        "08": string_reference,  # add two ints
        "09": field_reference,  # add two ints
        "0a": method_reference,  # add two ints
        "0b": interface_method_reference,  # add two ints
        "0c": name_and_type_discriptor,  # add two ints
        "0f": method_handle,  # add two ints
        "10": method_type,  # add two ints
        "11": dynamic,  # add two ints
        "12": invoke_dynamic,  # add two ints
        "13": module,  # add two ints
        "14": package,  # add two ints

    }

    def method_dict(self, argument):
        method = PoolTranslate.switcher.get(argument, "invalid")
        # execute function
        return method(self)



    pool_dict = {
        "01": "UTF_8_string",
        "03": "integer",
        "04": "float",
        "05": "long",
        "06": "double",
        "07": "class_reference",
        "08": "string_reference",
        "09": "field_reference",
        "0a": "method_reference",
        "0b": "interface_method_reference",
        "0c": "name_and_type_descriptor",
        "0f": "method_handle",
        "10": "method_type",
        "11": "dynamic",
        "12": "invoke_dynamic",
        "13": "module",
        "14": "package",
    }


    def name_tostring (byte_code):
        try:
            byte_code2 = PoolTranslate.pool_dict[byte_code]
        except KeyError:
            byte_code2 = "Byte code not found!"

        return byte_code2



    def do_it(self):
        temp = defaultdict(list)
        temp =jvpm_opcodes.get_const_pool()
        print(temp)
        g ="t"

if '__main__' == __name__:
    o = PoolTranslate
    o.do_it()