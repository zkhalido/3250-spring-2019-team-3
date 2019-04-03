import packages

if '__main__' == __name__:                  #pragma: no cover

    # **********************************************************************************************

    print('\n1) ___Parse, pull, and assign Header bytecodes:___')           #pragma: no cover
    H = packages.jvpm_opcodes.HeaderClass()               #pragma: no cover
    H.get_magic()                   #pragma: no cover
    H.get_minor()                   #pragma: no cover
    H.get_major()                   #pragma: no cover
    H.get_const_pool_count()        #pragma: no cover

    # **********************************************************************************************

    print('\n2) ___Parse, pull, and assign method bytecodes to an array, search imported '      #pragma: no cover
          '\n  opcode dictionary for bytecode and pull opcode. If found, send opcode to'        #pragma: no cover
          '\n  imported method dictionary to implement the method:___')                         #pragma: no cover

    O = packages.jvpm_opcodes.OpCodes()               #pragma: no cover
    print(H.get_const_pool())   #pragma: no cover
    #O.dict_search() will need to pass through the oject that holds all the methods
    # also need to have actual constant that are held in the object with the opcall methods
