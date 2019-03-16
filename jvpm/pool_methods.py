from collections import defaultdict

class OpCodeMethods():

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

        "01": UTF_8_string,  
        "03": integer,  
        "04": float,  
        "05": long,  
        "06": double,  
        "07": class_reference,  
        "08": string_reference,  
        "09": field_reference,  
        "0a": method_reference,  
        "0b": interface_method_reference,  
        "0c": name_and_type_discriptor,  
        "0f": method_handle,  
        "10": method_type,  
        "11": dynamic,  
        "12": invoke_dynamic, 
        "13": module,  
        "14": package,  

    }

    def token_dict(self, argument):
        method = OpCodeMethods.switcher.get(argument, "invalid")
        # execute function
        return method(self)
