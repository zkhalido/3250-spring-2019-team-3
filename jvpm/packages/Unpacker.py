class Unpacker:

	def single_byte_unpack(self, n, position):
        info = format(n.data[current + 1], '02x')
        return info

	def two_byte_unpack(self, n, position):
        info = format(n.data[current + 1] + n.data[current + 2], '02x')
        return info
n
    def four_byte_unpack(self, n, position):
        info = n.data[11 + i + position] + n.data[12 + i + position] +
                    n.data[13 + i + position] + n.data[14 + i + position], '02x')
        return info

    def double_part_tuple(self, n, position):
        info = format(n.data[current + 1] + n.data[current + 2], '02x')
        info2 = format(n.data[current + 3] + n.data[current + 4], '02x')
        temp = (idNum, info, info2)
        return temp

    def UTF8_tuple(self, n, position, length):
        for f in range (length):
            temp[i].append(format(n.data[13 + i + position + f], '02x'))
        position += (n.data[11 + i + position] + n.data[12 + i + position])
        position += 2