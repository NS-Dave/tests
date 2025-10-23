#!/usr/bin/env python3
"""
Tests for the hello_world module.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts', 'python'))

from hello_world import greet
import unittest


class TestHelloWorld(unittest.TestCase):
    """Test cases for hello world functions."""

    def test_greet_default(self):
        """Test greet with default parameter."""
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_with_name(self):
        """Test greet with custom name."""
        self.assertEqual(greet("Copilot"), "Hello, Copilot!")
        self.assertEqual(greet("Test"), "Hello, Test!")


if __name__ == '__main__':
    unittest.main()
