from collections import defaultdict
import jvpm_opcodes
#import jvpm.pool_tag_translate
import pool_tag_names

super_index = 0
class PoolTranslater:

    def __init__(self):

        jvpm_opcodes_obj = jvpm_opcodes.HeaderClass(name = "testSaveVar.class")
        self.pulled_constant_pool = defaultdict(list)
        self.pulled_constant_pool = jvpm_opcodes_obj.get_const_pool()
        self.byte_list_length = len(self.pulled_constant_pool.keys())
        self.key_list = list(self.pulled_constant_pool.keys())
        print(self.key_list)
        self.translated_pool = []
        self.current_pool_list = []
        self.constant_pool_index = 0
        self.current_pool_index = 0
        self.counter = 0
        self.pool_list_index = 0
        self.constant_pool_length = len(self.pulled_constant_pool)
        self.translated_pool = ["0"] * self.constant_pool_length
        self.super_index = 0

    def UTF_8_string(self, sub_list):                 #01
        print("utf8 string")
        print(sub_list)
        index = 1
        complete_string = ""
        while index < len(sub_list):
            byte_to_translate = int(sub_list[index], 16)
            translated_byte = (byte_to_translate).to_bytes(1, byteorder='big')
            converted_text = translated_byte.decode("utf-8", "ignore")
            complete_string += converted_text
            index += 1
        self.translated_pool[self.current_pool_index] = complete_string
        print(complete_string, " complete string")
        return complete_string



    def integer(self, sub_list):                      #03
        print("Integer  4 bytes")
        print(sub_list)

    def float(self, sub_list):                        #04
        print("Float  4 bytes")
        print(sub_list)

    def long(self, sub_list):                         #5
        print("Long    8 bytes")
        print(sub_list)

    def double(self, sub_list):                       #6
        print("Double    8 bytes")
        print(sub_list)

    def class_reference(self, sub_list):              #7
        print("class reference    4 bytes")
        print(sub_list)

        index = 0

        pulled_string = ""
        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            print (index, "  index")
            new_index = int(sub_list[index], 16)-1
            print(new_index, "new index")

            pulled_string = PoolTranslater.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1
            if len(sub_list) >1:

                if strings_to_combine < 1:
                    pulled_string = pulled_string + "."
                strings_to_combine += 1
                complete_string += pulled_string
            else:
                complete_string = pulled_string

        return complete_string


        #returned_string = PoolTranslater.method_dict(self,)


    def string_reference(self, sub_list):             #8
        print("String Reference   2 bytes")
        print(sub_list)
        index = 0

        pulled_string = ""
        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            print(index, "  index")
            new_index = int(sub_list[index], 16) - 1
            print(new_index, "new index")

            pulled_string = PoolTranslater.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1
            if len(sub_list) > 1:

                if strings_to_combine < 1:
                    pulled_string = pulled_string + "."
                strings_to_combine += 1
                complete_string += pulled_string
            else:
                complete_string = pulled_string

        return complete_string




    def field_reference(self, sub_list):              #9
        print("Field Reference    4 bytes")
        print (sub_list)

        index = 0

        pulled_string = ""
        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            print(index, "  index")
            new_index = int(sub_list[index], 16) - 1
            print(new_index, "new index")

            pulled_string = PoolTranslater.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1
            if len(sub_list) > 1:

                if strings_to_combine < 1:
                    pulled_string = pulled_string + "."
                strings_to_combine += 1
                complete_string += pulled_string
            else:
                complete_string = pulled_string

        return complete_string


    def method_reference(self, sub_list):             #10
        print(sub_list)
        print("Method Reference    4 bytes")
        #new_index = int(sub_list[0], 16)

        index = 0

        pulled_string = ""
        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            print (index, "  index")
            new_index = int(sub_list[index], 16)-1


            pulled_string = PoolTranslater.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1

            if strings_to_combine < 1:
                pulled_string = pulled_string + "."
            strings_to_combine += 1
            complete_string += pulled_string

        return complete_string






    def interface_method_reference(self, sub_list):   #11
        print("Interface Method Reference    4 bytes")
        print(sub_list)


    def name_and_type_discriptor(self, sub_list):     #12
        print("Name and Type Discriptor    4 bytes")
        print(sub_list)

        index = 0

        pulled_string = ""
        complete_string = ""
        strings_to_combine = 0

        while index < len(sub_list):
            print (index, "  index")
            new_index = int(sub_list[index], 16)-1

            pulled_string = PoolTranslater.method_dict(self, self.pulled_constant_pool, new_index)
            index += 1
            if strings_to_combine < 1:
                pulled_string = pulled_string + ":"
            strings_to_combine += 1
            complete_string += pulled_string

        return complete_string




    def method_handle(self, sub_list):                #15
        print("Method Handle    3 bytes")
        print(sub_list)
        type = {
            1 : "REF_getField",
            2 : "REF_getStatic",
            3 : "REF_putField",
            4 : "REF_putStatic",
            5 : "REF_invokeVirtual",
            8 : "REF_newInvokeSpecial",
            6 : "REF_invokeStatic",
            7 : "REF_invokeSpecial",
            9 : "REF_invokeInterface"
        }
        x = type[1]
        print(x)


    def method_type(self, sub_list):                  #16
        print("Method Type    2 bytes")
        print(sub_list)


    def dynamic(self, sub_list):                      #17
        print("Dynamic    4 bytes")
        print(sub_list)


    def invoke_dynamic(self, sub_list):               #18
        print("Invoke Dynamic    4 bytes")
        print(sub_list)


    def module(self, sub_list):                       #19
        print("Module    2 bytes")
        print(sub_list)


    def package(self, sub_list):                      #20
        print("Package    2 bytes")
        print(sub_list)



    switcher = {

        "01": UTF_8_string,                 # 2+x bytes
        "03": integer,                      # 4 bytes
        "04": float,                        # 4 bytes
        "05": long,                         # 8 bytes
        "06": double,                       # 8 bytes
        "07": class_reference,              # 2 bytes
        "08": string_reference,             # 2 bytes
        "09": field_reference,              # 4 bytes
        "0a": method_reference,             # 4 bytes
        "0b": interface_method_reference,   # 4 bytes
        "0c": name_and_type_discriptor,     # 4 bytes
        "0f": method_handle,                # 3 bytes
        "10": method_type,                  # 2 bytes
        "11": dynamic,                      # 4 bytes
        "12": invoke_dynamic,               # 4 bytes
        "13": module,                       # 2 bytes
        "14": package,                      # 2 bytes

    }

    def method_dict(self, constant_pool, current_index):
        #print(current_index, "current index")           #############################
        #print(self.key_list, " key list")           #############################


        #current_key = self.key_list[int(current_index)]
        current_key = current_index
        current_list = constant_pool[current_key]
        current_list_length = len(current_list)
        sub_list = []
        print(current_list, "current list")
        tag_byte = current_list[0]

        j = 1
        while j < current_list_length:
            sub_list.append(current_list[j])
            j += 1

        method = PoolTranslater.switcher.get(tag_byte, "invalid")

        return method(self, sub_list)



    def translate_pool(self):
        pool_translater = PoolTranslater()
        pool_index = 0

        while pool_index < self.constant_pool_length:

            self.translated_pool[pool_index] = pool_translater.method_dict(self.pulled_constant_pool, pool_index)
            pool_index += 1

        return self.translated_pool





if '__main__' == __name__:              #pragma: no cover

    P = PoolTranslater()
    #P.method_handle(P.pulled_constant_pool)
    print(P.pulled_constant_pool)
    print(P.constant_pool_length)
    print(P.translated_pool)

    P.translate_pool()
    print(P.translated_pool, "translated pool")
    print()
    print(len(P.translated_pool), "tp len")




