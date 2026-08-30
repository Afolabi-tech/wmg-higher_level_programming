#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_single(self):
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_default(self):
        self.assertEqual(max_integer(), None)

    def test_max_integer_mixed(self):
        self.assertEqual(max_integer([1, -5, 3, -2, 0]), 3)

    def test_max_integer_all_same(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)


if __name__ == '__main__':
    unittest.main()
