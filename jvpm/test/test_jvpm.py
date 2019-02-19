import sys
import jvpm.jvpm
import unittest

#tests jvpm file method outputs
class TestClassFile(unittest.TestCase):
    def setUp(self):
        self.cf = HeaderClass()

    def test_magic(self):
        self.assertEqual(self.cf.PullMagic(), 'cafebabe')
        print("unittestmagic: ", self.cf.PullMagic())

    def test_minor(self):
        self.assertEqual(self.cf.PullMinor(), 0)
        print("unittestprintminor :", self.cf.PullMinor())

    def test_major(self):
        self.assertEqual(self.cf.PullMajor(), 54)
        print("unittestprintmajor: ", self.cf.PullMajor())

    def test_PoolCount(self):
        self.assertEqual(self.cf.PullConstPoolCount(), 15)
        print("unittestprintpool: ", self.cf.PullConstPoolCount())

if __name__ == '__main__':
    unittest.main()
