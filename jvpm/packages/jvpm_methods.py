"""Module with mothods to interacts with the stack and the CP."""
import numpy
from .stack import Stack
from . import pool_translate, jvpm_opcodes
# pylint: disable=R0201, R0904, W0613, C0111, C0123

# ****************************************************************************************

Stack = Stack()
VARIABLES = [0]

class OpCodeMethods():
    """CLass of methods that are called from the CP."""
    def __init__(self):
        """opcode_methods"""

    def aload_0(self, opcode, constantpool, argument):
        """(2a)Load a reference to the stack."""
        self.iconst_0(opcode, constantpool, argument)

    def aload_1(self, opcode, constantpool, argument):
        """(2b)Load a reference to stack."""

    def dup(self, opcode, constantpool, argument):
        """Doubles the top item on the stack."""
        var = Stack.peek()
        Stack.push(var)

    def iadd(self, opcode, constantpool, argument):
        """iadd: add two ints from the stack."""
        var2 = Stack.pop()
        var1 = Stack.pop()
        if type(var1) == numpy.int64 and type(var2) == numpy.int64:
            var2 = numpy.int64(var2)
            var1 = numpy.int64(var1)
            Stack.push(var1 + var2)
        else:
            var2 = numpy.float64(var2)
            var1 = numpy.float64(var1)
            Stack.push(var1 + var2)

    def next_int(self, opcode, constantpool, argument):
        """receive input from the keyboard."""
        var = input()
        if var.isdigit():
            var1 = numpy.int64(var)
            Stack.push(var1)
        else:
            var1 = numpy.float64(var)
            Stack.push(var1)

    def println(self, opcode, constantpool, argument):
        """print from the stack."""
        if Stack.peek() == 0:
            Stack.pop()
        print(str(Stack.pop()))

    def iand(self, opcode, constantpool, argument):
        """perform a bitwise AND on two integers."""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        Stack.push(var1 & var2)

    def iconst_m1(self, opcode, constantpool, argument):
        """load the int value -1 onto the stack."""
        Stack.push(-1)

    def iconst_0(self, opcode, constantpool, argument):
        """load the int value 0 onto the stack."""
        Stack.push(0)

    def iconst_1(self, opcode, constantpool, argument):
        """load the int value 1 onto the stack."""
        Stack.push(1)

    def iconst_2(self, opcode, constantpool, argument):
        """load the int value 2 onto the stack."""
        Stack.push(2)

    def iconst_3(self, opcode, constantpool, argument):
        """load the int value 3 onto the stack."""
        Stack.push(3)

    def iconst_4(self, opcode, constantpool, argument):
        """load the int value 4 onto the stack."""
        Stack.push(4)

    def iconst_5(self, opcode, constantpool, argument):
        """load the int value 5 onto the stack."""
        Stack.push(5)

    def idiv(self, opcode, constantpool, argument):
        """divide two integers."""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        Stack.push(var1 / var2)

    def iinc(self, opcode, constantpool, argument):
        """increment local variable."""

    def iload_0(self, opcode, constantpool, argument):
        """load an int value from local array variable[0]."""
        pushing0 = VARIABLES[0]
        Stack.push(pushing0)

    def iload_1(self, opcode, constantpool, argument):
        """load an int value from local array variable[1]."""
        pushing1 = VARIABLES[1]
        Stack.push(pushing1)

    def iload_2(self, opcode, constantpool, argument):
        """load an int value from local array variable[2]."""
        pushing2 = VARIABLES[2]
        Stack.push(pushing2)

    def iload_3(self, opcode, constantpool, argument):
        """load an int value from local array variable[3]."""
        pushing3 = VARIABLES[3]
        Stack.push(pushing3)

    def imul(self, opcode, constantpool, argument):
        """multiply two integers."""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        Stack.push(var1 * var2)

    def ineg(self, opcode, constantpool, argument):
        """negate int."""
        var1 = numpy.int32(Stack.pop())
        Stack.push(0 - var1)

    def ior(self, opcode, constantpool, argument):
        """bitwise int OR."""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        Stack.push(var1 | var2)

    def irem(self, opcode, constantpool, argument):
        """logical in remainder."""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        Stack.push(var1 % var2)

    def ishl(self, opcode, constantpool, argument):
        """int shift left."""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        Stack.push(var1 << var2)

    def ishr(self, opcode, constantpool, argument):
        """int arithmetic shift right."""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        Stack.push(var1 >> var2)

    def istore_0(self, opcode, constantpool, argument):
        """store int value into VARIABLE[0]."""
        popped = Stack.pop()
        VARIABLES.pop(0) # remove the assigned 0 from the [0]position
        VARIABLES.insert(0, popped)

    def istore_1(self, opcode, constantpool, argument):
        """store int value into VARIABLE[1]."""
        popped = Stack.pop()
        VARIABLES.insert(1, popped)

    def istore_2(self, opcode, constantpool, argument):
        """store int value into VARIABLE[2]."""
        popped = Stack.pop()
        VARIABLES.insert(2, popped)

    def istore_3(self, opcode, constantpool, argument):
        """store int value into VARIABLE[3.]"""
        popped = Stack.pop()
        VARIABLES.insert(3, popped)

    def isub(self, opcode, constantpool, argument):
        """int subtract"""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        Stack.push(var1 - var2)

    def iushr(self, opcode, constantpool, argument):
        """int logical shift right"""
        var2 = numpy.int32(Stack.pop())
        var1 = numpy.int32(Stack.pop())
        if var1 >= 0:
            Stack.push(var1 >> var2)
        else:
            Stack.push((var1 + 0x10000000) >> var2)

    def ixor(self, opcode, constantpool, argument):
        """xor"""
        variable2 = numpy.int32(Stack.pop())
        variable1 = numpy.int32(Stack.pop())
        Stack.push(variable1 ^ variable2)

    def i2b(self, opcode, constantpool, argument):
        """convert int to byte"""
        variable1 = Stack.pop()
        Stack.push(variable1.to_bytes(8, byteorder='big'))

    def i2c(self, opcode, constantpool, argument):
        """convert int to character"""
        variable1 = numpy.uint32(Stack.pop())
        Stack.push(chr(variable1))

    def i2f(self, opcode, constantpool, argument):
        """convert int to float"""
        variable1 = numpy.int32(Stack.pop())
        Stack.push(float(variable1))

    def i2l(self, opcode, constantpool, argument):
        """convert int to long"""
        variable1 = numpy.int32(Stack.pop())
        Stack.push(numpy.int64(variable1))

    def i2s(self, opcode, constantpool, argument):
        """convert int to short"""
        variable1 = numpy.int32(Stack.pop())
        Stack.push(numpy.int16(variable1))

    def i2d(self, opcode, constantpool, argument):
        """convert int to decimal"""
        variable1 = numpy.int32(Stack.pop())
        Stack.push(numpy.int64(variable1))

    def invalid(self, opcode, constantpool, argument):
        pass

    def ldc(self, opcode, constantpool, argument):
        Stack.push(pool_translate.TRANSLATED_STRINGS[2])

    def invokespecial(self, opcode, constantpool, argument):
        """coming soon"""

# ****************************************************************************************

    dictionary = {

        "aload_0": aload_0,
        "aload_1": aload_1,
        "astore_1": istore_1,
        "dup": dup,
        "iadd": iadd,  # add two ints
        "iand": iand,  # perform a bitwise AND on two integers
        "iconst_m1": iconst_m1,  # load the int value -1 onto the stack
        "iconst_0": iconst_0,  # load the int value 0 onto the stack
        "iconst_1": iconst_1,  # load the int value 1 onto the stack
        "iconst_2": iconst_2,  # load the int value 2 onto the stack
        "iconst_3": iconst_3,  # load the int value 3 onto the stack
        "iconst_4": iconst_4,  # load the int value 4 onto the stack
        "iconst_5": iconst_5,  # load the int value 5 onto the stack
        "idiv": idiv,  # divide two integers
        "iinc": iinc,  # increment local variable #index by signed byte const
        "iload_0": iload_0,  # load an int value from local array variable[0]
        "iload_1": iload_1,  # load an int value from local array variable[1]
        "iload_2": iload_2,  # load an int value from local variable[2]
        "iload_3": iload_3,  # load an int value from local variable[3]
        "imul": imul,  # multiply two integers
        "ineg": ineg,  # negate int
        "ior": ior,  # bitwise int OR
        "irem": irem,  # logical in remainder
        "ishl": ishl,  # int shift left
        "ishr": ishr,  # int arithmetic shift right
        "istore": istore_3,  # store int value into variable #index
        "istore_0": istore_0,  # store int value into VARIABLE[0]
        "istore_1": istore_1,  # store int value into VARIABLE[1]
        "istore_2": istore_2,  # store int value into VARIABLE[2]
        "istore_3": istore_3,  # store int value into VARIABLE[3]
        "isub": isub,  # int subtract
        "iushr": iushr,  # int logical shift right
        "ixor": ixor,  # xor
        "i2b" : i2b, # int to byte
        "i2c" : i2c, # int to char
        "i2d" : i2d, # int to double
        "i2f" : i2f, # int to float
        "i2l" : i2l, # int to long
        "i2s" : i2s, # int to short
        "java/util/Scanner.nextInt:()I": next_int,
        "java/io/PrintStream.println:(I)V": println,
        "java/io/PrintStream.println:(Ljava/lang/String;)V": println,
        "invalid": invalid,
        "ldc": ldc,
        "invokespecial": invokespecial
    }

# ****************************************************************************************

    def token_dict(self, argument, opcode, constantpool):
        """dictionary search"""
        method = OpCodeMethods.dictionary.get(argument, "invalid")
        if type(method) == str:
            method = OpCodeMethods.dictionary.get(method)

        return method(self, opcode, constantpool, argument)

# ****************************************************************************************
