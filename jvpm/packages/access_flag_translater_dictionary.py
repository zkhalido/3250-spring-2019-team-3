class AccessFlagTranslater:
    def translate_access_flag(access_flag_value):
        access_flag = {
            0001 : "ACC_PUBLIC",
            0002 : "ACC_PRIVATE",
            0004 : "ACC_PROTECTED",
            0008 : "ACC_STATIC",
            0010 : "ACC_FINAL",
            0020 : "ACC_SUPER",
            0200 : "ACC_INTERFACE",
            0400 : "ACC_ABSTRACT",
            1000 : "ACC_SYNTHETIC",
            2000 : "ACC_ANNOTATION",
            4000 : "ACC_ENUM"
        }
        return access_flag
