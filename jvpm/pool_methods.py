
from collections import defaultdict

class OpCodeMethods():

    def UTF_8_string(self):
        #print("UTF_8_string  2+x bytes (variable)")
        return "UTF 8 String"

    def integer(self):
        #print("Integer  4 bytes")
        return "Integer"

    def float(self):
        #print("Float  4 bytes")
        return "Float"

    def long(self):
        #print("Long    8 bytes")
        return "Long"

    def double(self):
        #print("Double    8 bytes")
        return "Double"

    def class_reference(self):
        #print("Double    2 bytes")
        return "Class Reference"

    def string_reference(self):
        #print("Double    2 bytes")
        return "String Reference"

    def field_reference(self):
        #print("Field Reference    4 bytes")
        return"Field Reference"

    def method_reference(self):
        #print("Method Reference    4 bytes")
        return "Method Reference"

    def interface_method_reference(self):
        #print("Interface Method Reference    4 bytes")
        return "Interface Method Reference"

    def name_and_type_discriptor(self):
        #print("Name and Type Discriptor    4 bytes")
        return "Name and Type Descriptor"

    def method_handle(self):
        #print("Method Handle    3 bytes")
        return "Method Handle"

    def method_type(self):
        #print("Method Type    2 bytes")
        return "Method Type"

    def dynamic(self):
        #print("Dynamic    4 bytes")
        return"Dynamic"

    def invoke_dynamic(self):
        #print("Invoke Dynamic    4 bytes")
        return "Invoke Dynamic"

    def module(self):
        #print("Module    2 bytes")
        return "Module"

    def package(self):
        #print("Package    2 bytes")
        return "Package"


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

    def token_dict(self, argument):
        method = OpCodeMethods.switcher.get(argument, "invalid")
        # execute function
        return method(self)

