

def name_tostring(self, argument):
    pool_dict = {
        "01": "UTF_8_string",
        "03": "integer",
        "04": "float",
        "05": "long",
        "06": "double",
        "07": "class_reference",
        "08": "string_reference",
        "09": "field_reference",
        "0a": "method_reference",
        "0b": "interface_method_reference",
        "0c": "name_and_type_descriptor",
        "0f": "method_handle",
        "10": "method_type",
        "11": "dynamic",
        "12": "invoke_dynamic",
        "13": "module",
        "14": "package",
    }
    return pool_dict.get(argument, "invalid")



