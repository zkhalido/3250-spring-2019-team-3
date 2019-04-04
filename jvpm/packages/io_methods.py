class IoMethods():
    def __init__(self):
        # self.stack = Stack()
        self.VARIABLES = []
      
    def keyboard_in(self):
        """input from your keyboard"""
        var1 = input("What's your first variable? ")
        print("Your first variable is: " + var1)
        var2 = input("What's your second variable? ")
        print("So, you are ready to add " + var1 + " + " + var2)
        sum = var1 + var2
        print(var1 + " + " + var2 + " = ",sum)
    
