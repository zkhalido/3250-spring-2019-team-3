import sys
import packages
import argparse


if '__main__' == __name__:                  #pragma: no cover

    file_name = ("jvpm/javafiles/" + str(sys.argv[1]) + ".class")

    header_class_object = packages.jvpm_opcodes.HeaderClass(name = file_name)
    header_class_object.get_magic()
    header_class_object.get_minor()
    header_class_object.get_major()

    get_cp = header_class_object.get_const_pool()
    # print(n)
    p_translator = packages.pool_translate.PoolTranslate(get_cp, header_class_object.skips_in_constant_pool, name = file_name)

    pool = p_translator.translate_pool()
    # print(pool, "translated")

    access_flags = header_class_object.get_access_flags()
    # print(access_flags, "   access flags")

    this_class = header_class_object.get_this_class()
    # print(this_class, "   this class")

    super_class = header_class_object.get_super_class()
    # print(super_class, "   super class")

    get_ic = header_class_object.get_interfaces_count()
    # print(d, "   interfaces count")

    header_class_object.get_interface() # no method built yet but should just be index in constant pool

    e = header_class_object.get_field_count()
    # print(e, "   field count")

    header_class_object.get_field() # no method built yet but should just be variable table

    opcodes = header_class_object.get_methods_count()
    # print(opcodes, " - methods count       \n ", header_class_object.integer_method_count, " -int meth count")

    opcodes = header_class_object.get_methods(pool)
    # print("OpCodes:\n ", opcodes,    "** op codes **")

    # ********************************************************************************************

    dict_search_object = packages.jvpm_opcodes.OpCodes(opcodes, pool)
    dict_search_object.dict_search()
