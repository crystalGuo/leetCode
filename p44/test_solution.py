from unittest import TestCase
from p44.Solution import Solution

__author__ = 'tcsong'


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_isSimpleEqual(self):
    self.assertTrue(self.sol.isMatch("", ""))
    self.assertTrue(self.sol.isMatch("123", "123"))
    self.assertFalse(self.sol.isMatch("321", "123"))

