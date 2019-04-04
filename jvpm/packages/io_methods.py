from .stack import Stack
from . import jvpm_methods

S = Stack()

class IoMethods():
    def __init__(self):
        # self.stack = Stack()
        self.VARIABLES = []
      
    def keyboard_in(self):
        """input from your keyboard"""
        A = jvpm_methods.OpCodeMethods()
        var1 = int(input("What's your first variable? "))
        S.push(var1)
        print("Your first variable is: " + str(var1))
        var2 = int(input("What's your second variable? "))
        S.push(var2)
        print("Your second variable is: " + str(var2))
        
        print("Stand back, I will now add " + str(var1) + " + " + str(var2) + ".")
        A.iadd()
        sum = var1 + var2
        print(str(var1) + " + " + str(var2) + " = ",str(sum))
        print(S.peek())
        print()
