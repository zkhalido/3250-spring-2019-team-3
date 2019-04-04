import packages

if '__main__' == __name__:                  #pragma: no cover

    # **********************************************************************************************

    print('\n1) ___Parse, pull, and assign Header bytecodes:___')
    H = packages.jvpm_opcodes.HeaderClass()               #pragma: no cover
    H.get_magic()                   #pragma: no cover
    H.get_minor()                   #pragma: no cover
    H.get_major()                   #pragma: no cover
    print("Constant Pool Count: " + str(H.get_const_pool_count() - 1))

    # **********************************************************************************************

    print('\n2) ___Parse, pull, and assign method bytecodes to an array, search imported '
          '\n  opcode dictionary for bytecode and pull opcode. If found, send opcode to'
          '\n  imported method dictionary to implement the method:___\n')

    O = packages.jvpm_opcodes.OpCodes()
    O.dict_search()

    # **********************************************************************************************

    print('\n3) ___Retrieve Constant Pool from .class, translate, and print to console:___')

    # print(H.get_const_pool())

    P = packages.pool_translate.PoolTranslate()                 #pragma: no cover
    N = P.translate()                   #pragma: no cover
    X = packages.pool_methods.TagTranslate()#pragma: no cover
    print()                             #pragma: no cover
    print(N)                            #pragma: no cover
    print()                             #pragma: no cover
    for key in N:                       #pragma: no cover
        i = 1                            #pragma: no cover
        if (N[key][0]) == "01":         #pragma: no cover
            print(key, " ", X.token_dict(N[key][0]), "\t\t\t", N[key][len(N[key]) - 1])
        else:
            print(key, " ", X.token_dict(N[key][0]), "\t\t\t", N[key])

    # **********************************************************************************************

    print('\n4) ___Print Hello World!:___\n')


    # **********************************************************************************************

    print('\n5) ___Take input from the keyboard and add 2 numbers:___\n')

    K = packages.io_methods.IoMethods()
    K.keyboard_math("iadd")


    # **********************************************************************************************
