import packages

if '__main__' == __name__:                  #pragma: no cover

    H = packages.jvpm_opcodes.HeaderClass(name = "jvpm/javafiles/AddTwo.class")               #pragma: no cover
    H.get_magic()                   #pragma: no cover
    H.get_minor()                   #pragma: no cover
    H.get_major()                   #pragma: no cover

    P = packages.pool_translate.PoolTranslate(name ="jvpm/javafiles/AddTwo.class")                 #pragma: no cover
    N = P.translate_pool()                   #pragma: no cover
    X = packages.pool_methods.TagTranslate()#pragma: no cover
    
    packages.jvpm_opcodes.OpCodes().dict_search()
    
    