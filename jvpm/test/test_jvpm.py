import unittest
import sys
import jvpm
from unittest.mock import Mock, call

class TestClassFile(unittest.TestCase):
	def setUp(self):
		m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x00\x36\x00\x0F')
		with patch(__name__ + '.open', m):
			self.cf = ClassFile()

	def test_magic(self):
		self.assertEqual(self.cf.get_magic(), 'CAFEBABE')
		print("unittestmagic", self.cf.get_magic())

	def test_minor(self):
		self.assertEqual(self.cf.get_minor(), 0)
		print("unittestprintminor", self.cf.get_minor())

	def test_major(self):
		self.assertEqual(self.cf.get_major(), 54)
		print("unittestprintmajor", self.cf.get_major())

	def test_PoolCount(self):
		self.assertEqual(self.cf.get_poolCount(), 15)
		print("unittestprintpool", self.cf.get_poolCount())

class TestOpCodes(unittest.TestCase):
	def setUp(self):
		m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x00\x36\x00\x0F')
		with patch(__name__ + '.open', m):
			self.cf = OpCodes()

	def test_interpret(self, value):
		self.assertEqual(self.cf.interpret(1), 'aconst_null')

	def test_not_implmented(self):
		self.assertEqual(OpCodes().interpret(1), 'aconst_null')
		with self.assertRaises(KeyError):
			OpCodes().interpret(1)
