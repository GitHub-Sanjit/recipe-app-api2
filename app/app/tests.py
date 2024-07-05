"""
Sample Tests
"""

from django.test import SimpleTestCase  # type: ignore

from app import calc


class CalcTests(SimpleTestCase):
    """Test the clac module."""

    def test_add_numbers(self):
        """Test Adding Number togather."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test Subtract Numbers ."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
