import packages

if '__main__' == __name__:                  #pragma: no cover

    H = packages.jvpm_opcodes.HeaderClass(name = "jvpm/javafiles/testFloat.class")               #pragma: no cover
    #H.get_magic()                   #pragma: no cover
    #H.get_minor()                   #pragma: no cover
    #H.get_major()                   #pragma: no cover
    n = H.get_const_pool()
    print(n)
    p_translator = packages.pool_translate.PoolTranslate(name = "jvpm/javafiles/testFloat.class")
    pool = p_translator.translate_pool()
    print(pool)

    a = H.get_access_flags()
    print(a, "   access flags")

    b = H.get_this_class()
    print(b, "   this class")

    c = H.get_super_class()
    print(c, "   super class")

    d = H.get_interfaces_count()
    print(d, "   interfaces count")

    H.get_interface() # no method built yet but should just be index in constant pool

    e = H.get_field_count()
    print(e, "   field count")

    H.get_field() # no method built yet but should just be variable table

    f = H.get_methods_count()
    print(f, "   methods count", H.integer_method_count, "   int meth count")

    #H.get_methods(pool)

    f = H.get_methods(pool)
    print(f, "   ** op codes **")







    #P = packages.pool_translate.PoolTranslate(name ="jvpm/javafiles/AddTwo.class")                 #pragma: no cover
    #N = P.translate_pool()                   #pragma: no cover
    #X = packages.pool_methods.TagTranslate()#pragma: no cover
    
    #packages.jvpm_opcodes.OpCodes().dict_search()
