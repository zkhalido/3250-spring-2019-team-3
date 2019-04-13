from collections import defaultdict


class ReadAttribute():



    def get_code_attribute(self, methods_table, reader_location, data, op_codes, method_index, pool):
        add_one_byte = 1
        attribute_table = []
        values_to_return= []

        ############### attribute name index
        attribute_table.append(format((data[reader_location]), "02x"))
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        print(format((data[reader_location]), "02x"))
        print(format((data[reader_location+1]), "02x"))

        ################## attribute length
        attribute_table.append(format((data[reader_location + 2]), "02x"))
        attribute_table.append(format((data[reader_location + 3]), "02x"))
        attribute_table.append(format((data[reader_location + 4]), "02x"))
        attribute_table.append(format((data[reader_location + 5]), "02x"))

        attribute_length = (data[reader_location + 2]) + (data[reader_location + 3]) \
                           + (data[reader_location + 4]) \
                           + (data[reader_location + 5])
        reader_location += 6
        print(attribute_length, "   attribute length")
        ################# max stack
        attribute_table.append(format((data[reader_location]), "02x"))  # max stack
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        reader_location += 2
        ###############   max locals
        attribute_table.append(format((data[reader_location]), "02x"))  # max locals
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        reader_location += 2
        ###################  code length
        attribute_table.append(format((data[reader_location]), "02x")) # code length
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        attribute_table.append(format((data[reader_location + 2]), "02x"))
        attribute_table.append(format((data[reader_location + 3]), "02x"))
        code_length = (data[reader_location]) + (data[reader_location + add_one_byte]) \
                      + (data[reader_location + 2]) + (data[reader_location + 3])
        reader_location += 4

        #################  opc odes
        print(reader_location, "          reader location")
        print(code_length,  "     code length")
        i = 0
        while i < code_length:
            op_codes.append(format((data[reader_location]), "02x"))
            attribute_table.append(format((data[reader_location]), "02x"))
            i += 1
            reader_location += 1

        #reader_location += code_length
        print(reader_location, "          $$$reader location")

        print(code_length, "   code length")
        print(op_codes, "  opcodes")
        #############  exception table length
        exception_table_length = (data[reader_location]) + (data[reader_location + add_one_byte])
        print(exception_table_length, "   exception table length")

        attribute_table.append(format((data[reader_location]), "02x")) # exception table length
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        print( format((data[reader_location]), "02x") )
        print( format((data[reader_location+1]), "02x") )
        print("exception table length")
        reader_location += 2


        ############## exception table
        #if exception_table_length > 0:
        for x in range(exception_table_length):
            print("    @@@@@@@@@@@in exception table")
            attribute_table.append(format((data[reader_location]), "02x"))  # start pc
            attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
            reader_location += 2
            attribute_table.append(format((data[reader_location]), "02x"))  # end pc
            attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
            reader_location += 2
            attribute_table.append(format((data[reader_location]), "02x"))  # handler pc pc
            attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
            reader_location += 2
            attribute_table.append(format((data[reader_location]), "02x"))  # catch type
            attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
            reader_location += 2


        #i = 0
        #while i < exception_table_length:
            #attribute_table.append(format((data[reader_location + i]), "02x"))
            #reader_location += 1
            #i += 1

        ############## attribute count
        attribute_table.append(format((data[reader_location]), "02x"))  # attribute count
        attribute_table.append(format((data[reader_location + add_one_byte]), "02x"))
        next_attribute_count = (data[reader_location]) + (data[reader_location + add_one_byte])
        #reader_location += 2


        print (next_attribute_count, "            next attribute count")

        tag_location = (data[reader_location+2]) + (data[reader_location + 3])
        print(tag_location, " ^^^^^^^^^^^^^^^^^^tag L")
        tag = pool[tag_location]
        print(tag, "             %%%%%%%%%%%%%%% tagarino")
        reader_location += 2

        # attribute_table.append(format((self.data[self.reader_location + 6]), "02x"))
        methods_table[method_index].append(attribute_table)
        for x in range(next_attribute_count):
            reader_location = ReadAttribute.get_attribute(self, tag, methods_table, reader_location, data, op_codes, method_index, pool)


        #if next_attribute_count > 0:
            #print("   in if____________________________")
            #ReadAttribute.get_code_attribute(self, methods_table, reader_location, data, op_codes, method_index)


        print(reader_location, "reader location after 1 call")
        return reader_location

        # self.reader_location += 6



    def get_line_number_table(self, methods_table, reader_location, data, op_codes, method_index, pool):
        line_number_table = []
        ##################    name index
        line_number_table.append(format((data[reader_location]), "02x"))
        line_number_table.append(format((data[reader_location + 1]), "02x"))

        ##################### attribute length
        line_number_table.append(format((data[reader_location + 2]), "02x"))
        line_number_table.append(format((data[reader_location + 3]), "02x"))
        line_number_table.append(format((data[reader_location + 4]), "02x"))
        line_number_table.append(format((data[reader_location + 5]), "02x"))
        attribute_length = (data[reader_location + 2]) + (data[reader_location + 3]) \
                           + (data[reader_location + 4]) + (data[reader_location + 5])
        reader_location += 6

        ############### line number table length
        line_number_table.append(format((data[reader_location]), "02x"))
        line_number_table.append(format((data[reader_location + 1]), "02x")) # not sure if this is correct for line number table length i jsut read 4 more
        line_number_table_length = ((data[reader_location])+ (data[reader_location + 1]))

        print(format((data[reader_location]), "02x"))
        print(format((data[reader_location+1]), "02x"))
        print(line_number_table_length, "++++++++++++++++line number table length++++++++++++++++++")
        reader_location += 2


        #line_number_table = ((data[reader_location])+ (data[reader_location + 1]))
        for x in range(line_number_table_length):
            ########### start pc
            line_number_table.append(format((data[reader_location]), "02x"))
            line_number_table.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2

            ########### line number
            line_number_table.append(format((data[reader_location]), "02x"))
            line_number_table.append(format((data[reader_location + 1]), "02x"))
            reader_location += 2
            print ("in for***************")


        #line_number_table.append(format((data[reader_location]), "02x"))
        #line_number_table.append(format((data[reader_location + 1]), "02x"))
        #reader_location += 2

        #line_number_table.append(format((data[reader_location]), "02x"))
        #line_number_table.append(format((data[reader_location + 1]), "02x"))

        #reader_location += 2

        print(line_number_table, "   line number  table")
        print(reader_location, "         reader location line number table")
        methods_table[method_index].append(line_number_table)
        print(reader_location, "         reader l")

        return reader_location

    def get_source_file(self, methods_table, reader_location, data, op_codes, method_index, pool):
        x=0


    switcher = {
        "Code": get_code_attribute,  # 2+x bytes
        "LineNumberTable": get_line_number_table,  # 4 bytes
        "SourceFile": get_source_file,
    }


    def get_attribute(self, tag, methods_table, reader_location, data, op_codes, method_index, pool):
        print(reader_location,  "------------------------------- in switcher")
        print(tag, "           t ag")

        method = ReadAttribute.switcher.get(tag, "invalid")
        return method(self, methods_table, reader_location, data, op_codes, method_index, pool)
