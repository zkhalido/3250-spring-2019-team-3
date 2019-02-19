import unittest
import sys
import jvpm.jvpm
from unittest.mock import Mock, call

class TestJvpm(unittest.TestCase):
    def test_jvpm(self):
        sys.stdout = unittest.mock.Mock()
        jvpm.jvpm.HeaderClass.PullMagic()
        sys.stdout.assert_has_calls(
            [call.write('cafebabe')]
        )
