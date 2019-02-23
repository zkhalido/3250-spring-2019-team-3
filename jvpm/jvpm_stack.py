class Stack:
    """Class that creates a Stack, with methods to interact with the Stack"""
    def __init__(self):
        self.things = []

    def is_empty(self):
        """test if Stack is empty"""
        return self.things == []

    def push(self, 1):
        """Put item on the stack"""
        self.things.append(1)

    def pop(self):
        """Take item off stack"""
        return self.things.pop()

    def peek(self):
        """Look at item on top of stack"""
        return self.things[len(self.things)-1]

    def size(self):
        """Tells how many items are on the stack"""
        return len(self.things)
        
