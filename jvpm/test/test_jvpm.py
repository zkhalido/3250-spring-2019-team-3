import sys
import unittest

import jvpm_opcodes
from unittest.mock import Mock, call, patch, mock_open

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

class TestOpCodes(unittest.TestCase):
	def test_not_implmented(self):
		self.assertEqual(jvpm.OpCodes().interpret(0), 'not implemented')
		with self.assertRaises(KeyError):
			jvpm.OpCodes().interpret(1)
