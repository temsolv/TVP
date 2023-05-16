__author__ = "Artem Solbonov"

import unittest
import mod

class TestArrayActions(unittest.TestCase):
    """Test class for methods that communicate with array, inherited from unittest.TestCase"""

    def test_array_length(self):
        """Test method that checking the correctness of calculating the length of an array"""
        # empty array
        arr = []
        # array length
        length = 5
        # array filling
        mod.fill_array(arr, length)
        # assertEqual(a, b), checks that a == b
        self.assertEqual(len(arr),length)


    def test_aliquot(self):
        """Test method that checks the correctness of the found multiple and non-multiple numbers"""
        arr = [1, 5, 6, 15, 18] # unsorted array
        aliqout_arr = [6, 18] # array that satisfy the 3,5 aliquot conditions

        # find selected aliquots
        arr = mod.find_aliquot(arr, 3, 5)
        
        # two arrays equality comparing
        self.assertListEqual(arr, aliqout_arr)