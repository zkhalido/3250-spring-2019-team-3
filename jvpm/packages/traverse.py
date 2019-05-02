"""Module that traverses the CP"""
from collections import defaultdict
from bitstring import ConstBitStream
from CPInfo import ConstInfo
# pylint: disable=C0111, C0122, R0201, W0611

# *****************************************************************************

class HeaderClass():

    def __init__(self):
        self.data = ConstBitStream(filename='jvpm/javafiles/testSaveVar.class')

    def get_magic(self):
        magic = self.data.read('hex:32')
        return magic

    def get_minor(self):
        return self.data.read('hex:16')

    def get_major(self):
        return self.data.read('hex:16')

    def get_const_pool_count(self):
        return self.data.read('uint:16')

    def get_const_pool(self):
        constants_pool = defaultdict(list)
        constants_pool[0].append("base")
        const_pool_count = self.get_const_pool_count()
        const_pool_count -= 1
        i = 1  # does nothing
        while i <= const_pool_count:
            constant = ConstInfo().read(self.data)
            print(constant, "**********constant")
            constants_pool[i].append(constant)
            print(i, "                   IIIIIIIIIII                ")
            print(constant[0], "#############constant [0]  ######")
            if constant[0] == "06" or constant[0] == "05":
                print("              skiiiiiiiiiiiipppppp ")
                i += 1
            i += 1
            print(self.data.bytepos, "@@@@@@@@@@@@  byte pos   @@@@@@@@")
        print(constants_pool, "&&&&&&&&&&&     consts pool   &&&&&&&&&&&&&")
        return constants_pool

    def get_access_flags(self):
        return self.data.read('uint:16')

    def get_this_class(self):
        return self.data.read('uint:16')

    def get_super_class(self):
        return self.data.read('uint:16')

    def get_interfaces_count(self):
        return self.data.read('uint:16')


    def get_interfaces(self):
        interface_class_names = []
        return interface_class_names

    def get_fields_count(self):
        return

    def get_fields(self):
        return

    def get_methods_count(self):
        return

    def get_methods(self):
        return

    def get_attributes_count(self):
        return

    def get_attributes(self):
        return

    # *****************************************************************************

if '__main__' == __name__:
    HEADERS = HeaderClass()
    print(HEADERS.get_magic())
    print(HEADERS.get_minor(), "minor%%%%")
    print(HEADERS.get_major(), "$$$$$$$$major")
    HEADER_POOL = HEADERS.get_const_pool()
    
    # *****************************************************************************
