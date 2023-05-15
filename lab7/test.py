__author__ = "Artem Solbonov"

import unittest
import mod

class TestOfSum(unittest.TestCase):
    """Test class for methods that checks the received amount for correctness,
    inherited from unittest.TestCase"""

    def test_sum_input(self):
        """Test method that checks input parameters"""
        res = mod.find_sum(30, 70)
        self.assertEqual(res, "Incorrect numbers")


    def test_sum_result(self):
        """Test method that checks sum result for correctness"""
        res = mod.find_sum(100, 50)
        self.assertEqual(res, 24.474392232063654)