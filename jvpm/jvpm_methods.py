"""import stack.py"""
import stack
# These 63 methods will eventually Implement all the opcode commands.
# Method 4 - 63 is below the Dictionary, ONLY BUILD THE METHODS NOT COMMENTED OUT.
# pylint: disable = W0603, C0330

S = stack.Stack()
VARIABLE_0 = ''
VARIABLE_1 = ''
VARIABLE_2 = ''
VARIABLE_3 = ''

# According to the JVPM documentation Zach posted to Slack, 
# we need to use a local array's[] index values when using MATH with iload and istore.
# Therefore, I'm transitioning the 4 above variables to the below array.
variables = []

 # load the int value -1 onto the stack
def iconst_m1():
    """iconst_m1: load the int value -1 onto the stack"""
    S.push(-1)
    print("iconst_m1: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

# store int value into VARIABLE 1
def istore_1():
    """istore_1: store int value into VARIABLE 1"""
    global VARIABLE_1
    VARIABLE_1 = S.pop()
    popped = VARIABLE_1
    variables.insert(0, 0)
    variables.insert(1, popped)
    print("istore_1: Popped " + str(popped) +
          " from Stack and stored in variables[1] in jvpm_methods.py.")

def iinc():
    """iinc: increment local variable #index by signed byte const"""
    global VARIABLE_1
    VARIABLE_1 += 1
    S.push(VARIABLE_1)
    print("iinc: Increment VARIABLE_1 to " + str(VARIABLE_1) +
          " and push to Stack in jvpm_methods.py.")
    print("Top of Stack is now " + str(S.peek()) + ".")

# ****************************************************************************************

def opcode_methods(argument):
    """DICTIONARY OF METHODS, FOR SPRINT 3 ONLY BUILD THE METHODS NOT COMMENTED OUT."""
    token_dict = {
        "iconst_m1": iconst_m1,        # load the int value -1 onto the stack
        "istore_1": istore_1,         # store int value into VARIABLE 1
        "iinc": iinc,             # increment local variable #index by signed byte const
#         "i2b": i2b,              # convert an int into a byte
#         "i2c": i2c,              # convert an int into a character
#         "i2d": i2d,              # convert an int into a double
#         "i2f": i2f,              # convert an int into a float
#         "i2l": i2l,              # convert an int into a long
#         "i2s": i2s,              # convert an int into a short
        "iadd": iadd,            # add two ints
#         "iaload": method11,          # load an int from an array
        "iand": method12,            # perform a bitwise AND on two integers
#         "iastore": iastore,         # store an int into an array
        "iconst_0": iconst_0,        # load the int value 0 onto the stack
        "iconst_1": iconst_1,        # load the int value 1 onto the stack
        "iconst_2": iconst_2,        # load the int value 2 onto the stack
        "iconst_3": iconst_3,        # load the int value 3 onto the stack
        "iconst_4": iconst_4,        # load the int value 4 onto the stack
        "iconst_5": iconst_5,        # load the int value 5 onto the stack
        "idiv": idiv,            # divide two integers
#         "if_acmpeq": if_acmpeq,       # if references are equal branch to instruction
#         "if_acmpene": if_acmpene,      # if references are not equal branch to instruction
#         "if_icmpeq": if_icmpeq,       # if ints are equal, branch
#         "if_icmpge": if_icmpge,       # if value1 >= value2, branch
#         "if_icmpgt": if_icmpgt,       # if value1 > value2, branch
#         "if_icmple": if_icmple,       # if value1 <= value 2, branch
#         "if_icmplt": if_icmplt,       # if value1 < value2, branch
#         "if_icmpne": if_icmpne,       # if value1 != value2, branch
#         "ifeq": ifeq,            # if value is 0, branch
#         "ifge": ifge,            # if value >= 0, branch
#         "ifgt": ifgt,            # if value > 0, branch
#         "ifle": ifle,            # if value <= 0, branch
#         "iflt": iflt,            # if value < 0, branch
#         "ifne": ifne,            # if value != 0 , branch
#         "ifnonnull": ifnonnull,       # if value is not null, branch
#         "ifnull": ifnull,          # if value is null, branch
#         "iload": iload,           # load an int value from a local variabl #index
#         "iload_0": iload_0,         # load an int value from local variable 0
         "iload_1": iload_1,         # load an int value from local variable 1
         "iload_2": iload_2,         # load an int value from local variable 2
#         "iload_3": iload_3,         # load an int value from local variable 3
#         "impdep1": impdep1,         # reserved for implementation dependent operations,
#                                      # should not appear in any class
#         "impdep2": impdep2,         # reserved for implementation dependent operations,
#                                      # should not appear
        "imul": imul,            # multiply two integers
        "ineg": method45,            # negate int
#         "instanceof": instanceof,      # determines if objectref is of a given type
#         "invokedynamic": invokedynamic,   # invoke a dynamic method and puts the result on the stack
#         "invokeinterface": invokeinterface, # invoke an interface method on object object ref and
#                                      # puts results on the stack
#         "invokespecial": invokespecial,   # invoke instance method on objectref and
#                                      # puts result on the stack
#         "invokestatic": invokestatic,    # invoke static method and puts result on the stack
#         "invokevirtual": invokevirtual,   # invoke virtual method on objectref and
#                                      # puts result on the stack
        "ior": method52,             # bitwise int OR
        "irem": method53,            # logical in remainder
#         "ireturn": ireturn,         # returner an integer from a method
        "ishl": method55,            # int shift left
        "ishr": method56,            # int arithmetic shift right
        "istore": istore,          # store int value into variable #index
        "istore_0": istore_0,        # store int value into variable 0
        "istore_2": istore_2,        # store int value into variable 2
        "istore_3": istore_3,        # store int value into variable 3
        "isub": isub,            # int subtract
        "iushr": method62,           # int logical shift right
        "ixor": method63             # xor
    }
    # get the method name from the token_dict dictionary
    method = token_dict.get(argument, lambda: "Invalid opcode")
    # Call the Method.
    method()

# ****************************************************************************************

# def i2b():
#     print('i2b')

# def i2c():
#     print('i2c')

# def i2d():
#     print('i2d')

# def i2f():
#     print('i2f')

# def i2l():
#     print('i2l')

# def i2s():
#     print('i2s')

def iadd():
    """iadd: add two ints"""
#     global VARIABLE_1
#     global VARIABLE_2
#     S.push(VARIABLE_1 + VARIABLE_2)
#     print("> iadd: Added (VARIABLE_1 = " + str(VARIABLE_1) + ") + (VARIABLE_2 = " +
#           str(VARIABLE_2) + ") and pushed to Stack.")
#     print(">>>> Top of Stack is now " + str(S.peek()) + ".")
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 + var2)
    print("> iadd: Popped (" + str(var1) + ") and (" + str(var2) + 
          ") from the Stack, assigned to local variables, \nadded the two," 
          " and pushed result back to Stack.")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

# def method11():
#     print('method11')

def method12():
    """description"""
    print('method12')

# def iastore():
#     print('iastore')

def iconst_0():
    """iconst_0: load the int value 0 onto the stack"""
    S.push(0)
    print("iconst_0: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

def iconst_1():
    """iconst_1: load the int value 1 onto the stack"""
    S.push(1)
    print("iconst_1: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

# load the int value 2 onto the stack
def iconst_2():
    """iconst_2: load the int value 2 onto the stack"""
    S.push(2)
    print("iconst_2: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

def iconst_3():
    """iconst_3: load the int value 3 onto the stack"""
    S.push(3)
    print("iconst_3: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

def iconst_4():
    """iconst_4: load the int value 4 onto the stack"""
    S.push(4)
    print('"iconst_4: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py."')

def iconst_5():
    """iconst_5: load the int value 5 onto the stack"""
    S.push(5)
    print('"iconst_5: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py."')

def idiv():
    """idiv: divide two numbers"""
#     global VARIABLE_1
#     global VARIABLE_2
#     S.push(VARIABLE_1 / VARIABLE_2)
#     print("> idiv: Divided (VARIABLE_1 = " + str(VARIABLE_1) + ") / (VARIABLE_2 = " +
#           str(VARIABLE_2) + ") and pushed to Stack.")
#     print(">>>> Top of Stack is now " + str(S.peek()) + ".")
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 / var2)
    print("> idiv: Popped (" + str(var1) + ") and (" + str(var2) + 
          ") from the Stack, assigned to local variables, \ndivided the two," 
          " and pushed result back to Stack.")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

# def if_acmpeq():
#     print('if_acmpeq')

# def if_acmpene():
#     print('if_acmpene')

# def if_icmpeq():
#     print('if_icmpeq')

# def if_icmpge():
#     print('if_icmpge')

# def if_icmpgt():
#     print('if_icmpgt')

# def if_icmple():
#     print('if_icmple')

# def if_icmplt():
#     print('if_icmplt')

# def if_icmpne():
#     print('if_icmpne')

# def ifeq():
#     print('ifeq')

# def ifge():
#     print('ifge')

# def ifgt():
#     print('ifgt')

# def ifle():
#     print('ifle')

# def iflt():
#     print('iflt')

# def ifne():
#     print('ifne')

# def ifnonnull():
#     print('ifnonnull')

# def ifnull():
#     print('ifnull')

# def iload():
#     print('iload')

# def iload_0():
#     print('iload_0')

def iload_1():
    pushing = variables[1]
    S.push(pushing)
    print('iload_1: Push variables[1] to Stack')

def iload_2():
    pushing = variables[2]
    S.push(pushing)
    print('iload_2: Push variables[2] to Stack')

# def iload_3():
#     print('iload_3')

# def impdep1():
#     print('impdep1')

# def impdep2():
#     print('impdep2')

def imul():
    """imul: multiply two integers"""
#     global VARIABLE_1
#     global VARIABLE_2
#     S.push(VARIABLE_1 * VARIABLE_2)
#     print("> imul: Multipied (VARIABLE_1 = " + str(VARIABLE_1) + ") * (VARIABLE_2 = " +
#           str(VARIABLE_2) + ") and pushed to Stack.")
#     print(">>>> Top of Stack is now " + str(S.peek()) + ".")
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 * var2)
    print("> imul: Popped (" + str(var1) + ") and (" + str(var2) + 
          ") from the Stack, assigned to local variables, \nmultiplied the two," 
          " and pushed result back to Stack.")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

def method45():
    """description here"""
    print('method45')

# def instanceof():
#     print('instanceof')

# def invokedynamic():
#     print('invokedynamic')

# def invokeinterface():
#     print('invokeinterface')

# def invokespecial():
#     print('invokespecial')

# def invokestatic():
#     print('invokestatic')

# def invokevirtual():
#     print('invokevirtual')

def method52():
    """description here"""
    print('method52')

def method53():
    """description here"""
    print('method53')

# def ireturn():
#     print('ireturn')

def method55():
    """description here"""
    print('method55')

def method56():
    """description here"""
    print('method56')

def istore():
    """istore: store int value into array[in]"""
    print('method57')

def istore_0():
    """istore_0: store int value into VARIABLE 0"""
    global VARIABLE_0
    VARIABLE_0 = S.pop()
    print("istore_0: Popped " + str(VARIABLE_0) +
          " from Stack and stored in VARIABLE_0 in jvpm_methods.py.")

    # istore_1 is at the top

def istore_2():
    """istore_2: store int value into VARIABLE 2"""
    global VARIABLE_2
    VARIABLE_2 = S.pop()
    popped = VARIABLE_2
    variables.insert(2, popped)
    print("istore_2: Popped " + str(popped) +
          " from Stack and stored in variables[2] in jvpm_methods.py.")

def istore_3():
    """istore_3: store int value into VARIABLE 3"""
    global VARIABLE_3
    VARIABLE_3 = S.pop()
    popped = VARIABLE_3
    variables.insert(3, popped)
    print("istore_3: Popped " + str(popped) +
          " from Stack and stored in variables[3] in jvpm_methods.py," 
          "\n>> From the test1.java file 'c = a (?) b', therefore c = " + str(popped))
    print(">>>> Top of Stack is now " + str(S.size()) + ".")

def isub():
    """isub: subtract two ints"""
#     global VARIABLE_1
#     global VARIABLE_2
#     S.push(VARIABLE_1 - VARIABLE_2)
#     print("> isub: Subtracted (VARIABLE_1 = " + str(VARIABLE_1) + ") - (VARIABLE_2 = " +
#           str(VARIABLE_2) + ") and pushed to Stack.")
#     print(">>>> Top of Stack is now " + str(S.peek()) + ".")
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 - var2)
    print("> isub: Popped (" + str(var1) + ") and (" + str(var2) + 
          ") from the Stack, assigned to local variables, \nsubtracted the two," 
          " and pushed result back to Stack.")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

def method62():
    """description here"""
    print('method62')

def method63():
    """description here"""
    print('method63')
