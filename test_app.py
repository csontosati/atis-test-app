"""Partial unit tests for app.py — intentionally incomplete coverage."""

import unittest

from app import add, calculate, divide, grade, greet, subtract


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, World!")


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


class TestCalculate(unittest.TestCase):
    def test_calculate_add(self):
        self.assertEqual(calculate("add", 1, 2), 3)

    def test_calculate_unknown_op(self):
        with self.assertRaises(ValueError):
            calculate("power", 2, 3)


class TestGrade(unittest.TestCase):
    def test_grade_a(self):
        self.assertEqual(grade(95), "A")

    def test_grade_f(self):
        self.assertEqual(grade(40), "F")


if __name__ == "__main__":
    unittest.main()
