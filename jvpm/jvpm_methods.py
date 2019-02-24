# These 63 methods will eventually Implement the opcode commands.
def method1():
    print("called method 1 from jvpm_methods.py module using iconst_m1")

def method2():
    print("called method 2 from jvpm_methods.py module using istore_1")

def method3():
    print("called method 3 from jvpm_methods.py module using iinc")

"""DICTIONARY OF METHODS"""
def opcode_methods(argument):
    tokenDict = {
        "iconst_m1": method1,          # load the int value -1 onto the stack
        "istore_1": method2,           # store int value into variable 1
        "iinc": method3,               # increment local variable #index by signed byte const
         "i2b": method4,              # convert an int into a byte
#         "i2c": method5,              # convert an int into a character
#         "i2d": method6,              # convert an int into a double
#         "i2f": method7,              # convert an int into a float
#         "i2l": method8,              # convert an int into a long
#         "i2s": method9,              # convert an int into a short
#         "iadd": method10,            # add two ints
#         "iaload": method11,          # load an int from an array
#         "iand": method12,            # perform a bitwise AND on two integers
#         "iastore": method13,         # store an int into an array
#         "iconst_0": method14,        # load the int value 0 onto the stack
#         "iconst_1": method15,        # load the int value 1 onto the stack
#         "inconst_2": method16,        # load the int value 2 onto the stack
#         "inconst_3": method17,       # load the int value 3 onto the stack
#         "inconst_4": method18,       # load the int value 4 onto the stack
#         "iconst_5": method19,        # load the int value 5 onto the stack
#         "idiv": method20,            # divide two integers
#         "if_acmpeq": method21,       # if references are equal branch to instruction
#         "if_acmpene": method22,      # if references are not equal branch to instruction
#         "if_icmpeq": method23,       # if ints are equal, branch
#         "if_icmpge": method24,       # if value1 >= value2, branch
#         "if_icmpgt": method25,       # if value1 > value2, branch
#         "if_icmple": method26,       # if value1 <= value 2, branch
#         "if_icmplt": method27,       # if value1 < value2, branch
#         "if_icmpne": method28,       # if value1 != value2, branch
#         "ifeq": method29,            # if value is 0, branch
#         "ifge": method30,            # if value >= 0, branch
#         "ifgt": method31,            # if value > 0, branch
#         "ifle": method32,            # if value <= 0, branch
#         "iflt": method33,            # if value < 0, branch
#         "ifne": method34,            # if value != 0 , branch
#         "ifnonnull": method35,       # if value is not null, branch
#         "ifnull": method36,          # if value is null, branch
#         "iload": method37,           # load an int value from a local variabl #index
#         "iload_0": method38,         # load an int value from local variable 0
#         "iload_1": method39,         # load an int value from local variable 1
#         "iload_2": method40,         # load an int value from local variable 2
#         "iload_3": method41,         # load an int value from local variable 3
#         "impdep1": method42,         # reserved for implementation dependent operations, should not appear in any class
#         "impdep2": method43,         # reserved for implementation dependent operations, should not appear
#         "imul": method44,            # multiply two integers
#         "ineg": method45,            # negate int
#         "instanceof": method46,      # determines if objectref is of a given type
#         "invokedynamic": method47,   # invoke a dynamic method and puts the result on the stack
#         "invokeinterface": method48, # invoke an interface method on object objectref and puts results on the stack
#         "invokespecial": method49,   # invoke instance method on objectref and puts result on the stack
#         "invokestatic": method50,    # invoke static method and puts result on the stack
#         "invokevirtual": method51,   # invoke virtual method on objectref and puts result on the stack
#         "ior": method52,             # bitwise int OR
#         "irem": method53,            # logical in remainder
#         "ireturn": method54,         # returner an integer from a method
#         "ishl": method55,            # int shift left
#         "ishr": method56,            # int arithmetic shift right
#         "istore": method57,          # store int value into variable #index
#         "istore_0": method58,        # store int value into variable 0
#         "istore_2": method59,        # store int value into variable 2
#         "istore_3": method60,        # store int value into variable 3
#         "isub": method61,            # int subtract
#         "iushr": method62,           # int logical shift right
#         "ixor": method63             # xor
    }
    # get the method name from the tokenDict dictionary
    method = tokenDict.get(argument, lambda: "Invalid opcode")
    # Call the Method.
    method()
    
def method4():
    print('method4')
                                
# def get_methods(opcode):
#     ''' Retrieve method name from dictionary of opcodes '''
#     return tokenDict[opcode]
