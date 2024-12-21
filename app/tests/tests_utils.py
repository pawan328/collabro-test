import unittest
from app.utils import greet_user

class TestUtils(unittest.TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user("Alice"), "Hello, Alice!")
        self.assertEqual(greet_user("World"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()