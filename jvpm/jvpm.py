from collections import namedtuple
from bitstring import ConstBitStream


HeaderInformation = namedtuple("HeaderInformation", "magic minor_version major_version")

def PullHeader():
    x = ConstBitStream(filename='test.class')
    header_magic = x.read(32).hex
    header_minor = x.read(16).hex
    header_major = x.read(16).hex
    header_const_pool_count = x.read(16).hex
    headerCPInfo = (int(header_const_pool_count, 16)-1)
    header_access_flag = x.read(16).hex
    header_this_class = x.read(16).hex
    header_super_class = x.read(16).hex
    header_interfaces_count = x.read(16).hex
    header_interfaces = [None] * int(header_interfaces_count, 16)
    header_fields_count = x.read(16).hex
    header_fields = [None] * int(header_fields_count, 16)
    header_methods_count = x.read(16).hex
    header_methods = [None] * int(header_methods_count, 16)
    header_attributes_count = x.read(16).hex
    header_attributes = [None] * int(header_attributes_count, 16)
    print header_magic
    print header_minor
    print header_major
    print header_const_pool_count
    print headerCPInfo
    print header_access_flag
    print header_this_class
    print header_super_class
    print header_interfaces_count
    print header_interfaces
    print header_fields_count
    # print header_fields
    print header_methods_count
    print header_methods
    # print header_attributes_count
    print header_attributes

	

if '__main__' == __name__:
    PullHeader()
