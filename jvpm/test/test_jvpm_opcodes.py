"""unittest for jvpm_opcodes.py"""
import unittest
# Unittest to test the output of the HeaderClass() methods.
# python3 -m unittest jvpm_opcodes.py
# We have a warning about an unclosed file but no errors.
'''
class UnittestHeader(unittest.TestCase):
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
# **************************************************************************************************