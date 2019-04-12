from collections import defaultdict


class ReadAttribute():



    def get_code_attribute(self, methods_table, reader_location, data, op_codes, method_index):
        add_one_byte = 1
        attribute_table = []
        values_to_return= []


        attribute_table.append(format((data[reader_location]), "02x"))
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        attribute_table.append(format((data[reader_location + 2]), "02x"))
        attribute_table.append(format((data[reader_location + 3]), "02x"))
        attribute_table.append(format((data[reader_location + 4]), "02x"))
        attribute_table.append(format((data[reader_location + 5]), "02x"))
        attribute_length = (data[reader_location + 2]) + (data[reader_location + 3]) \
                           + (data[reader_location + 4]) \
                           + (data[reader_location + 5])
        reader_location += 6
        print(attribute_length, "   attribute length")
        attribute_table.append(format((data[reader_location]), "02x"))  # max stack
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        reader_location += 2
        attribute_table.append(format((data[reader_location]), "02x"))  # max locals
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        reader_location += 2
        attribute_table.append(format((data[reader_location]), "02x"))
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        attribute_table.append(format((data[reader_location + 2]), "02x"))
        attribute_table.append(format((data[reader_location + 3]), "02x"))
        code_length = (data[reader_location]) + (data[reader_location + add_one_byte]) \
                      + (data[reader_location + 2]) \
                      + (data[reader_location + 3])
        reader_location += 4
        print(reader_location, "          reader location")
        print(code_length,  "     code length")
        i = 0
        while i < code_length:
            op_codes.append(format((data[reader_location]), "02x"))
            attribute_table.append(format((data[reader_location]), "02x"))
            i += 1
            reader_location += 1

        #reader_location += code_length
        print(code_length, "   code length")
        print(op_codes, "  opcodes")
        exception_table_length = (data[reader_location]) + (data[reader_location + add_one_byte])
        attribute_table.append(format((data[reader_location]), "02x"))  # max locals
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        reader_location += 2
        print(exception_table_length, "   exception table length")
        i = 0
        while i < exception_table_length:
            attribute_table.append(format((data[reader_location + i]), "02x"))
            reader_location += 1
            i += 1

        # attribute_table.append(format((self.data[self.reader_location + 6]), "02x"))
        methods_table[method_index].append(attribute_table)
        methods_table[method_index].append(format((data[reader_location]), "02x"))
        methods_table[method_index].append(format((data[reader_location+1]), "02x"))
        next_attribute_count = (data[reader_location]) + (data[reader_location + add_one_byte])
        print (next_attribute_count, "            next attribute count")


        print(reader_location, "reader location after 1 call")
        return reader_location

        # self.reader_location += 6



    def get_line_number_table(self, methods_table, reader_location, data, op_codes, method_index):
        line_number_table = []
        line_number_table.append(format((data[reader_location]), "02x"))
        line_number_table.append(format((data[reader_location + 1]), "02x"))
        line_number_table.append(format((data[reader_location + 2]), "02x"))
        line_number_table.append(format((data[reader_location + 3]), "02x"))
        line_number_table.append(format((data[reader_location + 4]), "02x"))
        line_number_table.append(format((data[reader_location + 5]), "02x"))
        attribute_length = (data[reader_location + 2]) + (data[reader_location + 3]) \
                           + (data[reader_location + 4]) + (data[reader_location + 5])
        reader_location += 6

        line_number_table.append(format((data[reader_location]), "02x"))
        line_number_table.append(format((data[reader_location + 1]), "02x")) # not sure if this is correct for line number table length i jsut read 4 more
        reader_location += 2

        line_number_table.append(format((data[reader_location]), "02x"))
        line_number_table.append(format((data[reader_location + 1]), "02x"))
        reader_location += 2

        line_number_table.append(format((data[reader_location]), "02x"))
        line_number_table.append(format((data[reader_location + 1]), "02x"))

        reader_location += 2

        print(line_number_table, "   line number  table")
        print(reader_location, "         reader location line number table")
        methods_table[method_index].append(line_number_table)
        print(reader_location, "         reader l")

        return reader_location

    switcher = {
        "Code": get_code_attribute,  # 2+x bytes
        "LineNumberTable": get_line_number_table,  # 4 bytes
    }


    def get_attribute(self, tag, methods_table, reader_location, data, op_codes, method_index):
        print(reader_location,  "------------------------------- in switcher")
        print(tag, "           t ag")

        method = ReadAttribute.switcher.get(tag, "invalid")
        return method(self, methods_table, reader_location, data, op_codes, method_index)
