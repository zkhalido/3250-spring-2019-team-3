from collections import defaultdict
from . import jvpm_opcodes, pool_methods

super_index = 0
class PoolTranslate:

    def __init__(self):
        self.dictionary = defaultdict(list)
        #global g_dict
        #g_dict = defaultdict(list)
        H = jvpm_opcodes.HeaderClass(name ="jvpm/javafiles/tester.class")
        self.dictionary = H.get_const_pool()
        self.byte_list_count = len(self.dictionary.keys())
        global new_l
        new_l = []
        self.current_k = 0
        self.main_index =0
        self.super_index = 0
        dictLen = len(self.dictionary)
        i = 0
        self.vals = ["0"]
        while i < dictLen:
            new_l.append("0")
            self.vals.append("0")
            i += 1


#################################################################


    def UTF_8_string(self, di,super_index):                 #01
        print("UTF_8_string  2+x bytes (variable)")
        self.super_index = super_index

        newLen = len(di)

        L = len(di)
        i = 1
        dtext =""
        while i < L :
            int1 = int(di[i], 16)
            int2 = (int1).to_bytes(1, byteorder='big')
            ctext = int2.decode("utf-8", "ignore")
            dtext += ctext
            i += 1

        new_l[self.super_index-1] = dtext
        return dtext

    def integer(self):                      #03
        #self.super_index = super_index
        print("Integer  4 bytes")

    def float(self):                        #04
        print("Float  4 bytes")

    def long(self):                         #5
        print("Long    8 bytes")

    def double(self):                       #6
        print("Double    8 bytes")

    def class_reference(self, di, super_index):              #7
        print("class reference           4 bytes")

        self.super_index = super_index
        index = self.main_index

        self.main_index = int(di[0], 16)


        r = PoolTranslate.method_dict(self, self.dictionary, self.main_index, self.super_index)
        new_l[self.super_index-1] = r
        return r


    def string_reference(self):             #8
        print("String Reference    2 bytes")

    def field_reference(self):              #9
        print("Field Reference    4 bytes")

    def method_reference(self, di, super_index):             #
        print("Method Reference    4 bytes")
        self.super_index = super_index
        di2 = di
        index = 0
        list_len = len(di2)

        M = ""
        C = ""
        J = 0

        while index < list_len :
            self.main_index = di2[index]

            if self.main_index != 0:
                self.main_index = int(self.main_index, 16)

            M = PoolTranslate.method_dict(self, self.dictionary, index, super_index)
            index += 1
            if J < 1:
                M = M + "."
            J += 1
            C  += M
        new_l[self.super_index - 1] = C


    def interface_method_reference(self):   #11
        print("Interface Method Reference    4 bytes")

    def name_and_type_discriptor(self, di, super_index):     #12
        self.super_index = super_index
        print("Name and Type Discriptor    4 bytes")

        di2 = di
        index = 0
        list_len = len(di2)

        M = ""
        C = ""
        J = 0

        while index < list_len :
            self.main_index = di2[index]
            if self.main_index != 0:
                self.main_index = int(self.main_index, 16)
            M = PoolTranslate.method_dict(self, self.dictionary, index, self.super_index)
            index += 1
            if J < 1:
                M = M + ":"
            J += 1
            C  += M


        new_l[self.super_index-1] = C

        return C


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

    def method_dict(self, d, main_index, super_index):

        self.super_index = super_index

        d_len = len(d.keys())
        if type(main_index) == str :
            self.main_index = int(main_index)
        if self.main_index == 0:
            index = int(self.main_index)
        else:
            index = int(self.main_index)-1  # dont think this is doing anything


        key_list = list(d.keys())
        key_current = key_list[int(self.main_index)-1]
        list_current = d[key_current]
        tag_byte = list_current[0]
        list_len = len(list_current)
        j = 1
        new_li = []
        while int(index) < d_len :

            while j < list_len :
                new_li.append(list_current[j])
                j += 1


            method = PoolTranslate.switcher.get(tag_byte, "invalid")

            return method(self,  new_li, self.super_index)







    def translate(self ):

        H = jvpm_opcodes.HeaderClass()
        T = PoolTranslate()
        temp = H.get_const_pool()
        #if d != None:
            #temp = d
            #self.dictionary = temp
        l = temp[1]
        k = list(temp.keys())
        index = self.main_index
        #self.dictionary = temp
        L = len(self.dictionary)
        i = 1
        self.main_index = 1


        while i <= self.byte_list_count :

            self.main_index = str(self.main_index)
            self.super_index =i

            T.method_dict(self.dictionary, self.main_index, self.super_index)
            self.main_index = int(self.main_index)
            i += 1
            self.main_index = i
        x = 0
        new_dict = self.dictionary
        while x < len(new_l):
            new_dict[x].append(new_l[x])
            x += 1

        return new_dict
    """
    def print_pool(dictionary):
        H = PoolTranslate
        l = len(dictionary)
        i = 0
        i2 =0
        while i < l :
            H.name_tostring(dictionary[i][i2])
            val_len = dictionary[i]
    """


if '__main__' == __name__:              #pragma: no cover
    o = PoolTranslate()                 #pragma: no cover

    n = o.translate()                   #pragma: no cover
    x = packages.pool_methods.TagTranslate()#pragma: no cover
    #j = x.token_dict("0a")             #pragma: no cover
    #print(n)                           #pragma: no cover
    print()                             #pragma: no cover
    #print(n.key[0])                    #pragma: no cover
    print(n)                            #pragma: no cover
    print()                             #pragma: no cover

    #print(j)                           #pragma: no cover
    i = 1                               #pragma: no cover


    for key in n:                       #pragma: no cover
        i =1                            #pragma: no cover
        #while i < len(n[key]) :        #pragma: no cover
            #a = []                     #pragma: no cover
            #a.append(n[key][i])        #pragma: no cover
            #i += 1                     #pragma: no cover

        if (n[key][0]) == "01":         #pragma: no cover
            #print (" a ", a)           #pragma: no cover
            print(key, " ", x.token_dict(n[key][0]), "\t\t\t", n[key][len(n[key])-1])   #pragma: no cover

        else:       #pragma: no cover
            print(key, " ", x.token_dict(n[key][0]), "\t\t\t", n[key])  #pragma: no cover
