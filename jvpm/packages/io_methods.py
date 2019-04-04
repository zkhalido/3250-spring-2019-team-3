from .stack import Stack
from . import jvpm_methods

class IoMethods():
    def __init__(self):
        """input-output"""
        io_dict = {}
      
    def keyboard_add(self, argument):
        """input from your keyboard"""
        A = jvpm_methods.OpCodeMethods()
        # 3 dictionaries based on the opcode passed from the main. 
        # 1 dict for the method, 1 for the operation, 1 for the sign.
        io_dict = {"iadd": A.iadd, "isub": A.isub, "imul": A.imul, "idiv": A.idiv}
        method = io_dict.get(argument, "invalid")
        math_dict = {"iadd": "add", "isub": "subtract", "imul": "multiply", "idiv": "divide"}
        math = math_dict.get(argument, "invalid")
        sign_dict = {"iadd": "+", "isub": "-", "imul": "*", "idiv": "/"}
        sign = sign_dict.get(argument, "invalid")
        
        print("We will " + " " + math + " " + " your two inputs."
              
        #use A to call the math method.
        # A = jvpm_methods.OpCodeMethods()
        var1 = int(input("What's your first variable? "))
        jvpm_methods.S.push(var1)
        print("Your first variable is: " + str(var1))
        var2 = int(input("What's your second variable? "))
        jvpm_methods.S.push(var2)
        print("Your second variable is: " + str(var2))
        
#         # 3 dictionaries based on the opcode passed from the main. 
#         # 1 dict for the method, 1 for the operation, 1 for the sign.
#         io_dict = {"iadd": A.iadd, "isub": A.isub, "imul": A.imul, "idiv": A.idiv}
#         method = io_dict.get(argument, "invalid")
#         math_dict = {"iadd": "add", "isub": "subtract", "imul": "multiply", "idiv": "divide"}
#         math = math_dict.get(argument, "invalid")
#         sign_dict = {"iadd": "+", "isub": "-", "imul": "*", "idiv": "/"}
#         sign = sign_dict.get(argument, "invalid")
        
        print("Stand back, I will now " + math + " " + str(var1) + " " + sign + " " + str(var2) + ".")
        method()
        print(str(var1) + " " + sign + " " + str(var2) + " = " + str(jvpm_methods.S.peek()))
        print()
