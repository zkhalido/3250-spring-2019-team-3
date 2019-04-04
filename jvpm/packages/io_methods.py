from .stack import Stack
from . import jvpm_methods

class IoMethods():
    def __init__(self):
        """input-output"""
      
    def keyboard_add(self, argument):
        """input from your keyboard"""
        #use A to call the iadd method.
        A = jvpm_methods.OpCodeMethods()
        var1 = int(input("What's your first variable? "))
        jvpm_methods.S.push(var1)
        print("Your first variable is: " + str(var1))
        var2 = int(input("What's your second variable? "))
        jvpm_methods.S.push(var2)
        print("Your second variable is: " + str(var2))
        
        io_dict = {"iadd": iadd}
        #method = io_dict.get(argument, "invalid")
        
        print("Stand back, I will now add " + str(var1) + " + " + str(var2) + ".")
        A.iadd()
        print(str(var1) + " + " + str(var2) + " = " + str(jvpm_methods.S.peek()))
        
        # A.method()
        print()
