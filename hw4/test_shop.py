from unittest import TestCase, mock
import unittest
import shop
from shop import greeting, yes_money, no_money
class TestVerifyItem(TestCase):

    def test_item_exists(self):
        self.assertTrue(yes_money('lamp')




if __name__ == '__main__':
    unittest.main()
