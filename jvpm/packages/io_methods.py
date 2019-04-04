class IoMethods():
    def __init__(self):
        # self.stack = Stack()
        self.VARIABLES = []
      
    def keyboard_in(self):
        """input from your keyboard"""
        var1 = int(input("What's your first variable? "))
        print("Your first variable is: " + str(var1))
        var2 = int(input("What's your second variable? "))
        print("So, you are ready to add " + str(var1) + " + " + str(var2))
        sum = var1 + var2
        print(str(var1) + " + " + str(var2) + " = ",str(sum))
    
