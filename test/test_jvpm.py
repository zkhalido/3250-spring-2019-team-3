import unittest

from unittest.mock import mock_open, patch, call
from jvpm import packages

import sys
from collections import deque, defaultdict


class UnittestHeader(unittest.TestCase):

    def setUp(self):
        m = mock_open(read_data='CAFEBABE00000036000F')
        with patch(__name__ + '.open', m):
            self.cf = packages.jvpm_opcodes.HeaderClass()



 