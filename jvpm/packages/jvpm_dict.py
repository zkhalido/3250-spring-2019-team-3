"""
jvpm_dict
Method finds bytecode in dictionary and returns opcode
"""

# ****************************************************************************************

JVPM_DICT = {
    "2a": "aload_0",
    "2b": "aload_1",
    "4c": "astore_1",
    "91": "i2b",             # convert an int into a byte
    "92": "i2c",             # convert an int into a character
    "87": "i2d",             # convert an int into a double
    "86": "i2f",             # convert an int into a float
    "85": "i2l",             # convert an int into a long
    "93": "i2s",             # convert an int into a short
    "60": "iadd",            # add two ints
    "2e": "iaload",          # load an int from an array
    "7e": "iand",            # perform a bitwise AND on two integers
    "4f": "iastore",         # store an int into an array
    "02": "iconst_m1",       # load the int value -1 onto the stack
    "03": "iconst_0",        # load the int value 0 onto the stack
    "04": "iconst_1",        # load the int value 1 onto the stack
    "05": "iconst_2",        # load the int value 2 onto the stack
    "06": "iconst_3",        # load the int value 3 onto the stack
    "07": "iconst_4",        # load the int value 4 onto the stack
    "08": "iconst_5",        # load the int value 5 onto the stack
    "6c": "idiv",            # divide two integers
    "a5": "if_acmpeq",       # if references are equal branch to instruction
    "a6": "if_acmpene",      # if references are not equal branch to instruction
    "9f": "if_icmpeq",       # if ints are equal, branch
    "a2": "if_icmpge",       # if value1 >= value2, branch
    "a3": "if_icmpgt",       # if value1 > value2, branch
    "a4": "if_icmple",       # if value1 <= value 2, branch
    "a1": "if_icmplt",       # if value1 < value2, branch
    "a0": "if_icmpne",       # if value1 != value2, branch
    "99": "ifeq",            # if value is 0, branch
    "9c": "ifge",            # if value >= 0, branch
    "9d": "ifgt",            # if value > 0, branch
    "9e": "ifle",            # if value <= 0, branch
    "9b": "iflt",            # if value < 0, branch
    "9a": "ifne",            # if value != 0 , branch
    "c7": "ifnonnull",       # if value is not null, branch
    "c6": "ifnull",          # if value is null, branch
    "84": "iinc",            # increment local variable #index by signed byte const
    "15": "iload",           # load an int value from a local variabl #index
    "1a": "iload_0",         # load an int value from local variable 0
    "1b": "iload_1",         # load an int value from local variable 1
    "1c": "iload_2",         # load an int value from local variable 2
    "1d": "iload_3",         # load an int value from local variable 3
    "fe": "impdep1",         # reserved for implementation dependent operations,
                             # should not appear in any class
    "ff": "impdep2",         # reserved for implementation dependent operations, should not appear
    "68": "imul",            # multiply two integers
    "74": "ineg",            # negate int
    "c1": "instanceof",      # determines if objectref is of a given type
    "ba": "invokedynamic",   # invoke a dynamic method and puts the result on the stack
    "b9": "invokeinterface", # invoke an interface method on object objectref and
                             # puts results on the stack.
    "b7": "invokespecial",   # invoke instance method on objectref and puts result on the stack
    "b8": "invokestatic",    # invoke static method and puts result on the stack
    "b6": "invokevirtual",   # invoke virtual method on objectref and puts result on the stack
    "80": "ior",             # bitwise int OR
    "70": "irem",            # logical in remainder
    "ac": "ireturn",         # returner an integer from a method
    "78": "ishl",            # int shift left
    "7a": "ishr",            # int arithmetic shift right
    "36": "istore",          # store int value into variable #index
    "3b": "istore_0",        # store int value into variable 0
    "3c": "istore_1",        # store int value into variable 1
    "44": "istore_1",        #store float value into variable 1
    "3d": "istore_2",        # store int value into variable 2
    "45":  "istore_2",        # store float value in variable 2
    "3e": "istore_3",        # store int value into variable 3
    "46": "istore_3",        # store float value into variable 3
    "64": "isub",            # int subtract
    "7c": "iushr",           # int logical shift right
    "82": "ixor",            # xor
    "59": "dup",             # duplicates the top of the stack
    "8a": "i2d",
    "89": "i2f",
    "88": "i2i",
    "61": "iadd",
    "2f": "iaload",
    "7f": "iand",
    "50": "iastore",
    "94": "icmp",
    "09": "iconst_0",
    "0a": "iconst_1",
    "12": "ldc",
    "13": "idc_w",
    "14": "idc2_w",
    "6d": "idiv",
    "16": "iload",
    "1e": "iload_0",
    "1f": "iload_1",
    "20": "iload_2",
    "21": "iload_3",
    "69": "imul",
    "75": "ineg",
    "81": "ior",
    "71": "irem",
    "ad": "ireturn",
    "79": "ishl",
    "7b": "ishr",
    "37": "istore",
    "3f": "istore_0",
    "40": "istore_1",
    "41": "istore_2",
    "42": "istore_3",
    "65": "isub",
    "7d": "iushr",
    "83": "ixor"
    }

# ****************************************************************************************

def get_opcode(byte_code):
    """ Return opcode from given byte code, or an error message if not found """
    try:
        opcode = JVPM_DICT[byte_code]
    except KeyError:
        opcode = "Byte code not found!"
    return opcode

# ****************************************************************************************
