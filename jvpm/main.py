import packages
import webbrowser

if '__main__' == __name__:                  #pragma: no cover

    H = packages.jvpm_opcodes.HeaderClass()               #pragma: no cover
    H.get_magic()                   #pragma: no cover
    H.get_minor()                   #pragma: no cover
    H.get_major()                   #pragma: no cover

    P = packages.pool_translate.PoolTranslate("jvpm/javafiles/AddTwo.class")                 #pragma: no cover
    N = P.translate()                   #pragma: no cover
    X = packages.pool_methods.TagTranslate()#pragma: no cover
    
    packages.jvpm_opcodes.OpCodes().dict_search()
    
    