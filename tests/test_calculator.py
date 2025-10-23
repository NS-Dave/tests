#!/usr/bin/env python3
"""
Tests for the calculator module.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts', 'python'))

from calculator import add, subtract, multiply, divide
import unittest


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add(self):
        """Test addition."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        """Test division."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(10, 3), 3.333333, places=5)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
