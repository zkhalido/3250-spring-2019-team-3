
from collections import defaultdict
import jvpm_opcodes


class PoolTranslate:

    def __init__(self):
        self.dictionary = defaultdict(list)
        H = jvpm_opcodes.HeaderClass()

        self.dictionary = H.get_const_pool()
        d = defaultdict(list)
        self.new_l = []
        self.current_k = 0
        P = PoolTranslate
        num = 0
        self.main_index =0

########################################################################
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

#################################################################


    def UTF_8_string(self):                 #01
        print("UTF_8_string  2+x bytes (variable)")

    def integer(self, di):                      #03
        print("Integer  4 bytes")
        print (di)

    def float(self):                        #04
        print("Float  4 bytes")

    def long(self):                         #5
        print("Long    8 bytes")

    def double(self):                       #6
        print("Double    8 bytes")

    def class_reference(self, di):              #7
        print(di[0])
        print("class reference    2 bytes")
        index = self.main_index
        print(self.main_index)

        self.main_index = int(di[0], 16)
        print (index)
        print(self.main_index)
        print (1)

        PoolTranslate.method_dict(self, self.dictionary, self.main_index)


    def string_reference(self):             #8
        print("Double    2 bytes")

    def field_reference(self):              #9
        print("Field Reference    4 bytes")

    def method_reference(self, di):             #10
        di2 = di
        index = 0
        list_len = len(di2)
        index = self.main_index
        print("Method Reference    4 bytes")
        #jsut testing if its the correct list
        print(di2[0])
        print(int(di2[1], 16))

        while index < list_len :
            self.main_index = di2[index]
            PoolTranslate.method_dict(self, self.dictionary, index)
            index += 1



    def interface_method_reference(self):   #11
        print("Interface Method Reference    4 bytes")

    def name_and_type_discriptor(self):     #12
        print("Name and Type Discriptor    4 bytes")

    def method_handle(self):                #15
        print("Method Handle    3 bytes")

    def method_type(self):                  #16
        print("Method Type    2 bytes")

    def dynamic(self):                      #17
        print("Dynamic    4 bytes")

    def invoke_dynamic(self):               #18
        print("Invoke Dynamic    4 bytes")

    def module(self):                       #19
        print("Module    2 bytes")

    def package(self):                      #20
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

    def method_dict(self, d, main_index):

        d_len = len(d.keys())
        print(self.main_index)
        if self.main_index == 0:
            index = int(self.main_index)
        else:
            index = int(self.main_index)
            print (index)

        #index = int(self.main_index, 16)
        index = index-1
        print(index)
        print("stuff")
        key_list = list(d.keys())
        print (key_list)
        #print (key_list[index-1])
        if self.main_index == 0:
            key_current = key_list[int(self.main_index)]
        else:
            key_current = key_list[int(self.main_index)-1]
        print(key_current)
        list_current = d[key_current]
        tag_byte = list_current[0]
        print (tag_byte)
        list_len = len(list_current)
        j = 1
        new_l = []
        while int(self.main_index) < d_len :
            #key_current = key_list[index]
            #list_current = d[key_current]
            #tag_byte = list_current[0]
            #list_len = len(list_current)
            #j = 1
            while j < list_len :
                new_l.append(list_current[j])
                j += 1
            #print(self.new_l)

            method = PoolTranslate.switcher.get(tag_byte, "invalid")
            # execute function
            return method(self,  new_l)





    def do_it(self):

        H = jvpm_opcodes.HeaderClass()
        T = PoolTranslate()
        temp = H.get_const_pool()
        l = temp[1]
        k = list(temp.keys())
        index = self.main_index

        T.method_dict(self.dictionary, self.main_index)


if '__main__' == __name__:
    o = PoolTranslate()
    o.do_it()
    #print(o.dictionary)