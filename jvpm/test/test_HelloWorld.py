import unittest
import sys
import jvpm.HelloWorld
from unittest.mock import Mock, call

class TestHelloWorld(unittest.TestCase):
    def test_HelloWorld(self):
        sys.stdout = unittest.mock.Mock()
        jvpm.HelloWorld.HelloWorld()
        sys.stdout.assert_has_calls(
            [call.write('Hello world'), call.write('\n'),
            call.write('Marc Inouye'), call.write('\n'),
            call.write('Zack Khalidov'), call.write('\n'),
            call.write('Robert Kupfner'), call.write('\n'),
	    call.write('Dominick Licciardi'), call.write('\n'),
            call.write('Ezequiel Lopez - dev zeke'), call.write('\n'),
            call.write('Chris Johnson'), call.write('\n'),
            call.write('Gil Leibovich'), call.write('\n')]
        )
