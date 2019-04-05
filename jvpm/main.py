import packages

if '__main__' == __name__:                  #pragma: no cover

    # **********************************************************************************************

    print('\n___Parse, pull, and assign header Bytecodes:___')
    H = packages.jvpm_opcodes.HeaderClass()               #pragma: no cover
    H.get_magic()                   #pragma: no cover
    H.get_minor()                   #pragma: no cover
    H.get_major()                   #pragma: no cover
    print("Constant Pool Count: " + str(H.get_const_pool_count() - 1))

    # **********************************************************************************************

    print('\n___Retrieve Constant Pool from .class, translate, and print to console:___')

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
    
    print('\n___Parse, pull, and implement method Opcodes from .class file.'
          ' Take input from the keybaord:___')

    packages_opcodes = packages.jvpm_opcodes.OpCodes()
    print()
    packages_opcodes.dict_search()

    # **********************************************************************************************

    print('\n___Print Hello World!:___\n')

    
    
    
    
    
    
    
    
    print("_____________________________ ") 

    # **********************************************************************************************
