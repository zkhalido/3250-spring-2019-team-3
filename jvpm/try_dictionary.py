import jvpm_dict

from jvpm_dict import get_opcode


def test_dictionary():

    word = get_opcode("91")


    print(word)

if '__main__' == __name__:
    test_dictionary()