#!/usr/bin/python3
"""max_integer module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_MaxAtEnd(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_MaxAtStart(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_MaxAtMiddle(self):
        self.assertEqual(max_integer([3, 5, 2, 1]), 5)

    def test_NegativeNumber(self):
        self.assertEqual(max_integer([3, 5, -2, 1]), 5)
        self.assertEqual(max_integer([-3, -5, -2, -1]), -1)

    def test_EmptyList(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2]), 2)
