import unittest

from unittest.mock import mock_open, patch

import jvpm_opcodes


class UnittestHeader(unittest.TestCase):
    def setUp(self):
        m = mock_open(read_data='CAFEBABE00000036000F')
        with patch(__name__ + '.open', m):
            self.cf = jvpm_opcodes.HeaderClass()

    def test_magic(self):
        self.assertEqual(self.cf.pull_magic(), 'cafebabe')
        self.assertEqual(self.cf.pull_minor(), 0)
        self.assertEqual(self.cf.pull_major(), 54)
        self.assertEqual(self.cf.pull_const_pool_count(), 14)





'''
class UnittestHeader1(unittest.TestCase):
     """unittest to test method outputs"""
     def setUp(self):
         """instantiate an instance of HeaderClass"""
         self.test = HeaderClass()

     def test_magic(self):
         """method to test the pull_magic output"""
         self.test.pull_magic()
         """the comparison"""
         self.assertEqual(self.test.header_magic, 'cafebabe')
         print('<<<< passed header_magic, ' + self.test.header_magic + ' = cafebabe >>>>\n')

     def test_minor(self):
         """method to test the pull_minor output"""
         known_minor = 0
         """call methods in order, including the desired method, to acquire value."""
         self.test.pull_magic()
         self.test.pull_minor()
         """the comparison"""
         self.assertEqual(self.test.header_minor, 0)
         print(f'<<<< passed header_minor, {self.test.header_minor} = {known_minor} >>>>\n')

     def test_major(self):
         """method to test the pull_major output"""
         known_major = 54
         """call methods in order, including the desired method, to acquire value."""
         self.test.pull_magic()
         self.test.pull_minor()
         self.test.pull_major()
         """the comparison"""
         self.assertEqual(self.test.header_major, 54)
         print(f'<<<< passed header_major, {self.test.header_major} = {known_major} >>>>\n')

     def test_pool_count(self):
         """method to test the pull_const_pool_count output"""
         known_pool_count = 14
         """call methods in order, including the desired method, to acquire value."""
         self.test.pull_magic()
         self.test.pull_minor()
         self.test.pull_major()
         self.test.pull_const_pool_count()
         """the comparison"""
         self.assertEqual(self.test.header_const_pool_count, 14)
         print(f'< passed poolCount, {self.test.header_const_pool_count} = {known_pool_count} >\n')
'''

'''
class TestOpCodes(unittest.TestCase):
    def test_not_implmented(self):
        self.assertEqual(jvpm.OpCodes().interpret(0), 'not implemented')
        with self.assertRaises(KeyError):
            jvpm.OpCodes().interpret(1)
'''