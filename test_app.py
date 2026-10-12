import unittest
from app import add, greet

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_greet(self):
        self.assertEqual(greet("Arnav"), "Hello, Arnav!")

if __name__ == "__main__":
    unittest.main()