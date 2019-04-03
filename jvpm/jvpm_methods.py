#import stack
from stack import Stack
S = Stack()
VARIABLES = [0]
import numpy

#S = stack.Stack()

# ****************************************************************************************
class OpCodeMethods():

    def __init__(self):
        # self.stack = Stack()
        self.VARIABLES = []

    def iadd(self):
        """iadd: add two ints"""
        var2 = numpy.int32(self.stack.pop())
        var1 = numpy.int32(self.stack.pop())
        self.stack.push(var1 + var2)

    def iand(self):
        """perform a bitwise AND on two integers"""
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 & var2)

    def iconst_m1(self):
        """load the int value -1 onto the stack"""
        self.stack.push(-1)

    def iconst_0(self):
        """load the int value 0 onto the stack"""
        self.stack.push(0)

    def iconst_1(self):
        """load the int value 1 onto the stack"""
        S.push(1)
        print("ran iconst_1")
        print(S.peek())
        

    def iconst_2(self):
        """load the int value 2 onto the stack"""
        S.push(2)
        print("ran iconst_2")
        print(S.peek())

    def iconst_3(self):
        """load the int value 3 onto the stack"""
        self.stack.push(3)
        print("ran iconst_3")

    def iconst_4(self):
        """load the int value 4 onto the stack"""
        self.stack.push(4)

    def iconst_5(self):
        """load the int value 5 onto the stack"""
        self.stack.push(5)

    def idiv(self):
        """divide two integers"""
        var2 = numpy.int32(self.stack.pop())
        var1 = numpy.int32(self.stack.pop())
        self.stack.push(var1 / var2)

    def iinc(self):
        """increment local variable"""
        print("iinc: not needed for this sprint")

    def iload_0(self):
        """load an int value from local array variable[0]"""
        pushing = VARIABLES[0]
        S.push(pushing)

    def iload_1(self):
        """load an int value from local array variable[1]"""
        pushing = VARIABLES[1]
        S.push(pushing)
        print("ran iload_1")

    def iload_2(self):
        """load an int value from local array variable[2]"""
        pushing2 = VARIABLES[2]
        S.push(pushing2)
        print("ran iload_2")

    def iload_3(self):
        """load an int value from local array variable[3]"""
        pushing3 = self.VARIABLES[3]
        self.stack.push(pushing3)

    def imul(self):
        """multiply two integers"""
        var2 = numpy.int32(self.stack.pop())
        var1 = numpy.int32(self.stack.pop())
        self.stack.push(var1 * var2)

    def ineg(self):
        """negate int"""
        var1 = self.stack.pop()
        self.stack.push(0 - var1)

    def ior(self):
        """bitwise int OR"""
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 | var2)

    def irem(self):
        """logical in remainder"""
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 % var2)

    def ishl(self):
        """int shift left"""
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 << var2)

    def ishr(self):
        """int arithmetic shift right"""
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 >> var2)

    def istore_0(self):
        """store int value into VARIABLE[0]"""
        popped = self.stack.pop()
        #self.VARIABLES.pop(0) # remove the assigned 0 from the [0]position
        self.VARIABLES.insert(0, popped)
        print("ran istore_0")

    def istore_1(self):
        """store int value into VARIABLE[1]"""
        popped = S.pop()
        VARIABLES.insert(1, popped)
        print("ran istore_1")

    def istore_2(self):
        """store int value into VARIABLE[2]"""
        popped = S.pop()
        VARIABLES.insert(2, popped)
        print("ran istore_2")
        print(VARIABLES)

    def istore_3(self):
        """store int value into VARIABLE[3]"""
        popped = self.stack.pop()
        self.VARIABLES.insert(3, popped)
        print("ran istore_3")

    def isub(self):
        """int subtract"""
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        self.stack.push(var1 - var2)

    def iushr(self):
        """int logical shift right"""
        var2 = self.stack.pop()
        var1 = self.stack.pop()
        if var1 >= 0:
            self.stack.push(var1 >> var2)
        else:
            self.stack.push((var1 + 0x10000000) >> var2)

    def ixor(self):
        """xor"""
        variable2 = self.stack.pop()
        variable1 = self.stack.pop()
        self.stack.push(variable1 ^ variable2)
        print("ran ixor")

    def i2b(self):
        """convert int to byte"""
        variable1 = self.stack.pop()
        # int.to_bytes(length, byteorder, *, signed=False)
        self.stack.push(variable1.to_bytes(8, byteorder='big'))
        print("ran i2b")

    def i2c(self):
        """convert int to character"""
        variable1 = self.stack.pop()
        # chr = Return a string of one character whose ASCII code is the integer i
        # chr(i)
        self.stack.push(chr(variable1))
        print("ran i2c")

    def i2f(self):
        """convert int to float"""
        variable1 = self.stack.pop()
        # float([x])
        self.stack.push(float(variable1))
        print("ran i2f")

    def i2l(self):
        """convert int to long"""
        variable1 = self.stack.pop()
        # long(x, base=10)
        self.stack.push(int(variable1))
        print("ran i2l")

    def i2s(self):
        """convert int to short"""
        variable1 = self.stack.pop()
        # hex(x & mask)
        self.stack.push(hex(variable1 & 0xffff))
        print("ran i2s")

    def i2d(self):
        """convert int to decimal"""


    # Array of arguments from the main for istore and iload
    switcher = {

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
    }
    
    def token_dict(self, argument):
        # get function from spinner
        method = OpCodeMethods.switcher.get(argument, "invalid")
        # execute function
        return method(self)
