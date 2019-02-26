import stack
# These 63 methods will eventually Implement all the opcode commands.
# Method 4 - 63 is below the Dictionary, ONLY BUILD THE METHODS NOT COMMENTED OUT.
S = stack.Stack()
variable_1 = ''
variable_2 = ''

 # load the int value -1 onto the stack
def method1():
    """iconst_m1: load the int value -1 onto the stack"""
    S.push(-1)
    print("Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py using iconst_m1.")

# store int value into variable 1
def method2():
    """istore_1: store int value into variable 1"""
    global variable_1
    variable_1 = S.peek()
    S.pop()
    print("Popped " + str(variable_1) + 
          " from Stack and stored in variable_1 in jvpm_methods.py using istore_1.")

def method3():
    """iinc: increment local variable #index by signed byte const"""
    global variable_1
    variable_1 += 1
    S.push(variable_1)
    print("Increment variable_1 to " + str(variable_1) + 
          " and push to Stack in jvpm_methods.py using iinc.")
    print("Top of Stack is now " + str(S.peek()) + ".")

# ****************************************************************************************

"""DICTIONARY OF METHODS, FOR SPRINT 3 ONLY BUILD THE METHODS NOT COMMENTED OUT."""
def opcode_methods(argument):
    tokenDict = {
        "iconst_m1": method1,        # load the int value -1 onto the stack
        "istore_1": method2,         # store int value into variable 1
        "iinc": method3,             # increment local variable #index by signed byte const
#         "i2b": method4,              # convert an int into a byte
#         "i2c": method5,              # convert an int into a character
#         "i2d": method6,              # convert an int into a double
#         "i2f": method7,              # convert an int into a float
#         "i2l": method8,              # convert an int into a long
#         "i2s": method9,              # convert an int into a short
        "iadd": method10,            # add two ints
#         "iaload": method11,          # load an int from an array
        "iand": method12,            # perform a bitwise AND on two integers
#         "iastore": method13,         # store an int into an array
        "iconst_0": method14,        # load the int value 0 onto the stack
        "iconst_1": method15,        # load the int value 1 onto the stack
        "iconst_2": method16,        # load the int value 2 onto the stack
        "iconst_3": method17,        # load the int value 3 onto the stack
        "iconst_4": method18,        # load the int value 4 onto the stack
        "iconst_5": method19,        # load the int value 5 onto the stack
        "idiv": method20,            # divide two integers
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
#         "impdep1": method42,         # reserved for implementation dependent operations, 
#                                      # should not appear in any class
#         "impdep2": method43,         # reserved for implementation dependent operations, 
#                                      # should not appear
        "imul": method44,            # multiply two integers
        "ineg": method45,            # negate int
#         "instanceof": method46,      # determines if objectref is of a given type
#         "invokedynamic": method47,   # invoke a dynamic method and puts the result on the stack
#         "invokeinterface": method48, # invoke an interface method on object objectref and puts results on the stack
#         "invokespecial": method49,   # invoke instance method on objectref and puts result on the stack
#         "invokestatic": method50,    # invoke static method and puts result on the stack
#         "invokevirtual": method51,   # invoke virtual method on objectref and puts result on the stack
        "ior": method52,             # bitwise int OR
        "irem": method53,            # logical in remainder
#         "ireturn": method54,         # returner an integer from a method
        "ishl": method55,            # int shift left
        "ishr": method56,            # int arithmetic shift right
        "istore": method57,          # store int value into variable #index
        "istore_0": method58,        # store int value into variable 0
        "istore_2": method59,        # store int value into variable 2
        "istore_3": method60,        # store int value into variable 3
        "isub": method61,            # int subtract
        "iushr": method62,           # int logical shift right
        "ixor": method63             # xor
    }
    # get the method name from the tokenDict dictionary
    method = tokenDict.get(argument, lambda: "Invalid opcode")
    # Call the Method.
    method()

# ****************************************************************************************

# def method4():
#     print('method4')

# def method5():
#     print('method5')

# def method6():
#     print('method6')

# def method7():
#     print('method7')

# def method8():
#     print('method8')

# def method9():
#     print('method9')

def method10():
    """add two ints"""
    global variable_1
    global variable_2
    S.push(variable_1 + variable_2)
    print("Added " + variable_1 + " and " + variable_2 + " and pushed to Stack.")

# def method11():
#     print('method11')

def method12():
    print('method12')

# def method13():
#     print('method13')

def method14():
    """iconst_0: load the int value 0 onto the stack"""
    S.push(0)
    print("Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py using iconst_0.")

def method15():
    """iconst_1: load the int value 1 onto the stack"""
    S.push(1)
    print("Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py using iconst_1.")

# load the int value 2 onto the stack
def method16():
    """iconst_2: load the int value 2 onto the stack"""
    S.push(2)
    print("Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py using iconst_2.")

def method17():
    """iconst_3: load the int value 3 onto the stack"""
    S.push(3)
    print("Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py using iconst_3.")

def method18():
    """iconst_4: load the int value 4 onto the stack"""
    S.push(4)
    print('"Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py using iconst_4."')

def method19():
    """iconst_5: load the int value 5 onto the stack"""
    S.push(5)
    print('"Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py using iconst_5."')

def method20():
    """description here"""
    print('method20')

# def method21():
#     print('method21')

# def method22():
#     print('method22')

# def method23():
#     print('method23')

# def method24():
#     print('method24')

# def method25():
#     print('method25')

# def method26():
#     print('method26')

# def method27():
#     print('method27')

# def method28():
#     print('method28')

# def method29():
#     print('method29')

# def method30():
#     print('method30')

# def method31():
#     print('method31')

# def method32():
#     print('method32')

# def method33():
#     print('method33')

# def method34():
#     print('method34')

# def method35():
#     print('method35')

# def method36():
#     print('method36')

# def method37():
#     print('method37')

# def method38():
#     print('method38')

# def method39():
#     print('method39')

# def method40():
#     print('method40')

# def method41():
#     print('metho415')

# def method42():
#     print('method42')

# def method43():
#     print('method43')

def method44():
    """multiply two integers"""
    S.push(S.pop() * S.pop())
    print('method44')

def method45():
    """description here"""
    print('method45')

# def method46():
#     print('method46')

# def method47():
#     print('method47')

# def method48():
#     print('method48')

# def method49():
#     print('method49')

# def method50():
#     print('method50')

# def method51():
#     print('method51')

def method52():
    """description here"""
    print('method52')

def method53():
    """description here"""
    print('method53')

# def method54():
#     print('method54')

def method55():
    """description here"""
    print('method55')

def method56():
    """description here"""
    print('method56')

def method57():
    """description here"""
    print('method57')

def method58():
    """description here"""
    print('method58')

def method59():
    """istore_2: store int value into variable 2"""
    global variable_2
    variable_2 = S.peek()
    S.pop()
    print("Popped " + str(variable_2) + 
          " from Stack and stored in variable_2 in jvpm_methods.py using istore_2.")

def method60():
    """description here"""
    print('method60')

def method61():
    """description here"""
    print('method61')

def method62():
    """description here"""
    print('method62')

def method63():
    """description here"""
    print('method63')
