from collections import namedtuple
from bitstring import ConstBitStream


HeaderInformation = namedtuple("HeaderInformation", "magic minor_version major_version")

def PullHeader():
	x = ConstBitStream(filename='test.class')
	b = x.read(32).hex
	print(b)

	

if '__main__' == __name__:
	PullHeader()