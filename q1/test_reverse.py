import unittest
import reverse

class TestCase(unittest.TestCase):

    def test_reverse(self):
        str = ['AL', 'the', 'Cat']
        self.assertEqual(reverse.str_reverse(str), "Cat the AL ")