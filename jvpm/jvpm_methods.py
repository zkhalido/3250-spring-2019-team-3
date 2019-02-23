
def method1():
    print("called function 1")

def method2():
    print("called function 2")

def method3():
    print("called function 3")

tokenDict = {"iconst_m1":method1, "istore_1":method2, "iinc":method3}

def get_methods(opcode):
    ''' Retrieve byte code from dictionary and return byte code '''
    return tokenDict[opcode]
