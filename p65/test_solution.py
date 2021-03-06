from unittest import TestCase
from p65.Solution import Solution
__author__ = 'tcsong'


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_is_empty_false(self):
    self.assertFalse(self.sol.isNumber(""))

  def test_is_zero_true(self):
    self.assertTrue(self.sol.isNumber("0"))

  def test_is_integer_true(self):
    self.assertTrue(self.sol.isNumber("12321"))
    self.assertTrue(self.sol.isNumber("-321312"))
    self.assertTrue(self.sol.isNumber("0"))
    self.assertTrue(self.sol.isNumber("12321371283721937821937281937"))
    self.assertTrue(self.sol.isNumber("-321893212321371283721937821937281937"))

    self.assertFalse(self.sol.isNumber("-0"))
    self.assertFalse(self.sol.isNumber("--1"))
    self.assertFalse(self.sol.isNumber("-12fs21"))
    self.assertFalse(self.sol.isNumber("x12fs"))

  def test_trim_spaces(self):
    self.assertTrue(self.sol.isNumber(" 0 "))

    self.assertFalse(self.sol.isNumber(" 1 23"))

  def test_float_numbers(self):
    self.assertTrue(self.sol.isNumber("1.2"))
    self.assertTrue(self.sol.isNumber("123.2321"))
    self.assertTrue(self.sol.isNumber("-123.2321"))
    self.assertTrue(self.sol.isNumber("0.2321"))
    self.assertTrue(self.sol.isNumber("0.2321"))
    self.assertTrue(self.sol.isNumber("-0.2321"))
    self.assertTrue(self.sol.isNumber("-0.00000001"))

    self.assertFalse(self.sol.isNumber("-0.00000000"))
    self.assertFalse(self.sol.isNumber("0.00000000x"))
    self.assertFalse(self.sol.isNumber("\t\20.00000000x"))

  def test_power(self):
    self.assertTrue(self.sol.isNumber("2e5"))
    self.assertTrue(self.sol.isNumber("2e15"))
    self.assertTrue(self.sol.isNumber("2e-15"))
    self.assertTrue(self.sol.isNumber("2e-253213213"))

    self.assertFalse(self.sol.isNumber("2e25feaf3213213"))

  def test_example(self):
    self.assertTrue(self.sol.isNumber("0"))
    self.assertTrue(self.sol.isNumber(" 0.1 "))
    self.assertTrue(self.sol.isNumber("2e10"))

    self.assertFalse(self.sol.isNumber("abc"))
    self.assertFalse(self.sol.isNumber("1 a"))

  def test_failed_cases(self):
    self.assertTrue(self.sol.isNumber('.1'))
    self.assertTrue(self.sol.isNumber('01'))
    self.assertTrue(self.sol.isNumber('-01'))

    self.assertTrue(self.sol.isNumber('3.'))
    self.assertTrue(self.sol.isNumber('3.e-2'))
    self.assertTrue(self.sol.isNumber('32133.e3212'))
    self.assertFalse(self.sol.isNumber('.'))

    self.assertTrue(self.sol.isNumber('+.8'))
