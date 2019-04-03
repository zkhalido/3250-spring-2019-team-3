"""Read bit stream."""
#from bitstring import ConstBitStream
from pip._vendor.distlib.compat import raw_input

import jvpm_dict    # import external opcode dictionary
from collections import defaultdict
import jvpm_methods
from stack import Stack
#from jvpm_methods import OpCodeMethods # import external method dictionary

# **************************************************************************************************

class HeaderClass():
    """Class that parses the header data from .class file and assigns values to variables."""
   #name = raw_input('Type the name of the file with class extension --')
    def __init__(self, name = "test.class"):
        #self.name = "test.class"#raw_input('Type the name of the file with class extension --')
        with open(name, 'rb') as binary_file:
            self.data = binary_file.read()
            self.temp_2 = defaultdict(list)

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
        #c = ("Contant Pool Count: ", self.data[8] + self.data[9] - 1)
        #print(c)

        #print("Contant Pool Count: ", self.data[8] + self.data[9] - 1)

        return self.data[8] + self.data[9]
    
    def get_const_pool(self):
        temp = defaultdict(list)
        position = 0
        count = self.get_const_pool_count() - 1
        for i in range(count):
            # Pulling class info
            if self.data[10 + i + position] == 7:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                position += 2
            # Field Ref
            elif self.data[10 + i + position] == 9:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # Method Ref
            elif self.data[10 + i + position] == 10:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # Interface Method Ref
            elif self.data[10 + i + position] == 11:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # String
            elif self.data[10 + i + position] == 8:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                position += 4
            # Integer
            elif self.data[10 + i + position] == 3:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position] + 
                    self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # Float
            elif self.data[10 + i + position] == 4:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position] + 
                    self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # Long
            elif self.data[10 + i + position] == 5:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position] + 
                    self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                temp[i].append(format(self.data[15 + i + position] + self.data[16 + i + position] + 
                    self.data[17 + i + position] + self.data[18 + i + position], '02x'))
                position += 8
            # Double
            elif self.data[10 + i + position] == 6:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position] + 
                    self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                temp[i].append(format(self.data[15 + i + position] + self.data[16 + i + position] + 
                    self.data[17 + i + position] + self.data[18 + i + position], '02x'))
                position += 8
            # Name and Type
            elif self.data[10 + i + position] == 12:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
            # Utf_8
            elif self.data[10 + i + position] == 1:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                for f in range (self.data[11 + i + position] + self.data[12 + i + position]):
                    temp[i].append(format(self.data[13 + i + position + f], '02x'))
                position += (self.data[11 + i + position] + self.data[12 + i + position])
                position += 2
                
            # Method Handle
            elif self.data[10 + i + position] == 15:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position], '02x'))
                temp[i].append(format(self.data[12 + i + position] + self.data[13 + i + position], '02x'))
                position += 3
            # Method Type
            elif self.data[10 + i + position] == 16:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                position += 2
            # Invoke Dynamic
            elif self.data[10 + i + position] == 18:
                temp[i].append(format(self.data[10 + i + position], '02x'))
                temp[i].append(format(self.data[11 + i + position] + self.data[12 + i + position], '02x'))
                temp[i].append(format(self.data[13 + i + position] + self.data[14 + i + position], '02x'))
                position += 4
        self.temp_2 = temp
        # print(self.temp_2)
        # print(self.temp_2[0])
        return temp

# **************************************************************************************************

class OpCodes():

    """Parse Opcodes into an array from the .class file, search the external dictionary of
    opcodes, and implement the methods using the external dictionary of methods"""
    def __init__(self):
        self.opcodes = ['04', '3c', '05', '3d', '1b', '1c', '60', '1c', '68', '1c', '6c', '1c',
                        '64', '3e']
        # self.opcodes = []


        """


        METHOD GOES HERE TO FIND OPCODES FROM ANY .CLASS FILE AND SAVE TO self.opcodes LIST.



        """
        
    # I duplicated this method for testing from the commented out method below it
    # because it wouldn't work to find the opcodes, now it works. If you need the 
    # other one, just comment out this one. Thx. 4-3-19
    def dict_search(self):
      print(self.opcodes)
      index = 0

      while index < len(self.opcodes):
          opcall = jvpm_dict.get_opcode(self.opcodes[index])
          print(opcall) # just to see what opcall is passed through
          jvpm_methods.OpCodeMethods().token_dict(opcall)
          index += 1
      print()  

#     def dict_search(self, jvMethodsIn):
#         print(self.opcodes)
#         index = 0

#         while index < len(self.opcodes):
#             opcall = jvpm_dict.get_opcode(self.opcodes[index])

#             print (opcall) # just to see what opcall is passed through

#             jvMethodsIn.token_dict(opcall)
#             index += 1
#         print()


# **************************************************************************************************

if '__main__' == __name__:                  #pragma: no cover

    # **********************************************************************************************

    print('\n1) ___Parse, pull, and assign Header bytecodes:___')
    H = HeaderClass()               #pragma: no cover
    H.get_magic()                   #pragma: no cover
    H.get_minor()                   #pragma: no cover
    H.get_major()                   #pragma: no cover
    H.get_const_pool_count()        #pragma: no cover

    # **********************************************************************************************

    print('\n2) ___Parse, pull, and assign method bytecodes to an array, search imported '      
          '\n  opcode dictionary for bytecode and pull opcode. If found, send opcode to'        
          '\n  imported method dictionary to implement the method:___\n')                         

    O = OpCodes()         
    O.dict_search()
    
    # **********************************************************************************************
    
    print('\n3) ___Retrieve the Constant Pool from the .class file and print to console:___\n')                       

    print(H.get_const_pool())
    
    # **********************************************************************************************
    
    print('\n4) ___Print Hello World!:___\n')
    
    
    
    # **********************************************************************************************
    
    print('\n5) ___Take input from the keyboard and add 2 numbers:___\n')
    
    
    
    # **********************************************************************************************
