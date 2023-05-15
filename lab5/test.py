__author__ = "Artem Solbonov"

import unittest
import mod

class TestArrayActions(unittest.TestCase):
    """Test class for methods that communicate with array, inherited from unittest.TestCase"""

    def test_array_length(self):
        """Test function that checking the correctness of calculating the length of an array"""
        arr = [] # empty array
        length = 5 # array length
        mod.filling_array(arr, length) # array filling
        self.assertEqual(len(arr),length) # assertEqual(a, b) checks that a == b


    def test_array_for_integers(self):
        """Test function that checks whether the array numbers are natural"""
        arr = [] # empty array
        length = 5 # array length
        mod.filling_array(arr, length) # array filling
        for i in range(len(arr)):
            self.assertGreaterEqual(arr[i],0) # assertGreaterEqual(a,b) checks a >= b


    def test_degree(self):
        """A function that checks the degree for correctness"""
        # empty arrays
        arr1 = [] 
        arr2 = [] 
        # arrays filling
        mod.filling_array(arr1, 5)
        mod.filling_array(arr2, 5)
        # second array elements exponentiation
        mod.calc_degree(arr2, 2)
        # range 1-5, because 1**any degree will be always 1
        for i in range(1, 5):
            self.assertNotEqual(arr1[i], arr2[i])