# """import the unittest"""
# import unittest
"""Read bit stream."""
from bitstring import ConstBitStream
import jvpm_dict    # import external opcode dictionary
import jvpm_methods
from jvpm_methods import OpCodeMethods # import external method dictionary

# pylint: disable = W0105, C0122, R0903

# **************************************************************************************************

class HeaderClass():
    """Class that parses the header data from .class file and assigns values to variables."""
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        print("\nMagic: ", magic)
        return magic

    def get_minor(self):
        print("Minor: ", self.data[4] + self.data[5])
        return self.data[4] + self.data[5]

    def get_major(self):
        print("Major: ", self.data[6] + self.data[7])
        return self.data[6] + self.data[7]

    def get_const_pool_count(self):
        print("Contant Pool Count: ", self.data[8] + self.data[9] - 1)
        return self.data[8] + self.data[9]

# **************************************************************************************************

class OpCodes():

    """Parse Opcodes into an array from the .class file, search the external dictionary of
    opcodes, and implement the methods using the external dictionary of methods"""
    def __init__(self):
        # List of the test1.java(math) opcodes.
#         self.opcodes = ['04', '3c', '05', '3d', '1b', '1c', '60', '1c', '68', '1c', '6c', '1c',
#                         '64', '3e']
        self.opcodes = ['06', '3c', '04', '3d', '1b', '1c', '82', '3e']
#        self.opcodes = ['06', '3c', '1b', '74', '3e']

        """


        METHOD GOES HERE TO FIND OPCODES FROM ANY .CLASS FILE AND SAVE TO self.opcodes LIST.



        """

    def dict_search(self):
        """
        Search the jvpm.dict.py(dictionary) file for the bytecode/opcode translation and
        implement if found.

	    Hex to Opcode from imported opcode dictionary - jvpm_dict,
        implemented using imported method dictionary - jvpm_methods.
        """
        #print("\nBytecodes from the .class file: " + str(self.opcodes))

        index = 0
        jvMethodsIn = OpCodeMethods()
        while index < len(self.opcodes):
            opcall = jvpm_dict.get_opcode(self.opcodes[index])

            #print("Bytecode " + self.opcodes[index] + ' = Opcode: ' + opcall)

            print (opcall) # just to see what opcall is passed through
            jvMethodsIn.token_dict(opcall)
            index += 1
        print()
        # return

# **************************************************************************************************

if '__main__' == __name__:

    # **********************************************************************************************

    print('\n1) ___Parse, pull, and assign Header bytecodes:___')
    H = HeaderClass()
    H.get_magic()
    H.get_minor()
    H.get_major()
    H.get_const_pool_count()

    # **********************************************************************************************

    print('\n2) ___Parse, pull, and assign method bytecodes to an array, search imported '
          '\n  opcode dictionary for bytecode and pull opcode. If found, send opcode to'
          '\n  imported method dictionary to implement the method:___')

    O = OpCodes()
    O.dict_search()


