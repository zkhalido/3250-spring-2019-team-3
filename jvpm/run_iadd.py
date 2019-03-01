from stack import Stack

"""
Just an exammple program to test the instantiantion of 
jvpm_methods
"""


import stack

from jvpm_methods import OpCodeMethods


def Hello():

    s = stack.Stack()

    a = OpCodeMethods()
    a.stack.push(2)
    a.stack.push(2)

    a.iadd()
    v = a.stack.pop()
    print(v)


    a.stack.push(1)
    a.stack.push(2)

    a.token_dict("iadd")

    g = a.stack.pop()
    print(g)

    a.stack.push(g)
    a.stack.push(1)
    a.token_dict("iadd")
    l = a.stack.pop()
    print(l)



if '__main__' == __name__:
    Hello()