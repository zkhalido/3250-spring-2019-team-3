import unittest
from unittest.mock import mock_open, patch, Mock, call

from stack import Stack
from jvpm_methods import OpCodeMethods
from jvpm_opcodes import OpCodes

import jvpm_dict
import jvpm_opcodes
import jvpm_methods
import sys

################################################################################
#cj branch start of test_2                                                     #
################################################################################

class Test_More_Jvpm_opcodes (unittest.TestCase):

    def test_dict_search(self):

        L = jvpm_opcodes.OpCodes()
        L.opcodes =['06', '3c', '04', '3d', '1b', '1c', '82', '3e']
        sys.stdout = unittest.mock.Mock()
        L.dict_search(self)
        sys.stdout.assert_has_calls(

            [call.write('iconst_3'), call.write('\n'),
            call.write('ran iconst_3'), call.write('\n'),
            call.write('istore_1'), call.write('\n'),
            call.write('ran istore_1'), call.write('\n'),
            call.write('iconst_1'), call.write('\n'),
            call.write('ran iconst_1'), call.write('\n'),
            call.write('istore_2'), call.write('\n'),
            call.write('ran istore_2'), call.write('\n'),
            call.write('iload_1'), call.write('\n'),
            call.write('ran iload_1'), call.write('\n'),
            call.write('iload_2'), call.write('\n'),
            call.write('ran iload_2'), call.write('\n'),
            call.write('ixor'), call.write('\n'),
            call.write('ran ixor'), call.write('\n'),
            call.write('istore_3'), call.write('\n'),
            call.write('ran istore_3'), call.write('\n'), call.write('\n')]
        )
