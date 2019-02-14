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
            call.write('We are team 3 and our names are...\n'), call.write('\n'),
            call.write('Marc Inouye - Dev Team'), call.write('\n'),
            call.write('Zack Khalidov - Dev Team'), call.write('\n'),
            call.write('Robert Kupfner - Dev Team'), call.write('\n'),
	    call.write('Dominick Licciardi - SCRUM Master'), call.write('\n'),
            call.write('Ezequiel Lopez - Dev Team'), call.write('\n'),
            call.write('Chris Johnson - Product Owner'), call.write('\n'),
            call.write('Gil Leibovich - Dev Team'), call.write('\n')]
        )
 
