"""
Testing helper functions
"""
import unittest
from sample import add, reverse

class TestSampleMethods(unittest.TestCase):
    """
    Test harness
    """
    def test_add(self):
        """
        Testing add function
        """
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(-4, 7), 3)
    def test_reverse(self):
        """
        Testing reverse function
        """
        self.assertEqual(reverse("Hello World!"), "!dlroW olleH")
        self.assertEqual(reverse([1,2,3]), [3,2,1])
        self.assertEqual(reverse("racecar"), "racecar")

if __name__ == '__main__':
    unittest.main()
