import unittest
from app.utils import greet_user

class TestUtils(unittest.TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user(), "Hello, Friend")  # Default value
        self.assertEqual(greet_user("Alice"), "Hello, New Person!")

if __name__ == "__main__":
    unittest.main()