import unittest
from mypackage.string_operations import to_upper, reverse_string

class TestStringOperations(unittest.TestCase):
    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

if __name__ == "__main__":
    unittest.main()
