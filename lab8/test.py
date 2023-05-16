__author__ = "Artem Solbonov"

import unittest
import mod

class TestArrayFunctionsCase(unittest.TestCase):
    """Test class for methods that communicate with array, inherited from unittest.TestCase"""


    def test_fill_list_size(self):
        """Test method that checks input parameters"""
        num = []
        length = 10 # list length

        # filling list with random numbers
        mod.fill_list(num)

        # compare 
        self.assertEqual(len(num), length)

    
    def test_find_even(self):
        """Test method that checks finded evens elements for correctness"""
        # Test array
        arr = [[3, 4],
               [7, 8]]
        
        evens = [3, 8] #  Array with elements with even indexes

        # Find elements with even indexes
        new_arr = mod.find_even(arr)

        # Compare lists
        self.assertListEqual(new_arr, evens)


    def test_compare_even(self):
        """Test method that checks equality at elements from even array, to nums list"""
        nums = [7, 3]
        even_arr = [4, 6, 7, 9, 3]

        # List of equal elements
        equal = mod.compare_even(even_arr, nums)

        # Compare list elements
        self.assertListEqual(equal, nums)


    def test_replace_equal(self):
        """Test method that checks replacement correctness"""
        replc = [2, 5] # List with elements to replace

        unreplc_matr = [
            [1, 3, 5],
            [6, 4, 2]
        ]

        expected_matr = [
            [1, 3, 0],
            [6, 4, 9]
        ]

        # Repalce elements in matrix by zero
        mod.replace_equal(replc, unreplc_matr)

        # Compare list elements
        self.assertListEqual(expected_matr, expected_matr)

