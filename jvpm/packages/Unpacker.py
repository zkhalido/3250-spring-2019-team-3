class Unpacker:
	def single_byte_unpack(self, n, current):
        info = format(n.data[current + 1], '02x')
        return info

	def two_byte_unpack(self, n, current):
        info = format(n.data[current + 1] + n.data[current + 2], '02x')
        return info

    def four_byte_unpack(self, n, current):
        info = n.data[11 + i + current] + n.data[12 + i + current] +
                    n.data[13 + i + current] + n.data[14 + i + current], '02x')
        return info

    def UTF8_unpack(self, n, current, length):
        for f in range (length):
            temp[i].append(format(n.data[13 + i + current + f], '02x'))
        current += (n.data[11 + i + current] + n.data[12 + i + current])
        current += 2