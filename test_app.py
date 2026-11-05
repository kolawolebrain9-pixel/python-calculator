import unittest
import app


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)
        self.assertEqual(app.add(-1, 1), 0)
        self.assertEqual(app.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(app.subtract(10, 5), 5)
        self.assertEqual(app.subtract(-1, -1), 0)
        self.assertEqual(app.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(app.multiply(3, 4), 12)
        self.assertEqual(app.multiply(-2, 3), -6)
        self.assertEqual(app.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(app.divide(10, 2), 5)
        self.assertEqual(app.divide(9, 2), 4.5)
        self.assertEqual(app.divide(5, 0), "Error: Division by zero")


if __name__ == "__main__":
    unittest.main()

