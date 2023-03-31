from unittest import TestCase, mock
import unittest
import shop
from shop import *
class Test1(unittest.TestCase):
    def not_in_shop(self):
        self.assertAlmostEqual(all_in_shop(items),answer)


    def test_input_value(self):
        self.assertRaises(TypeError, all_in_shop(), True)





if __name__ == '__main__':
    unittest.main()
