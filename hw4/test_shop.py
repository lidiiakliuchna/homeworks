from unittest import TestCase, main
import shop as main_functions


class TestMainProgram(TestCase):
    # Use string slice to get "tap" out of "practice"
    def test_string_slice(self):
        self.assertEqual(main_functions.slice_practice(), "tap")

    # Is within range
    def test_is_within_range(self):
        self.assertFalse(main_functions.is_within_range(3, 5, 7))
        self.assertTrue(main_functions.is_within_range(5, 1, 10))
        self.assertTrue(main_functions.is_within_range(0, -1, 1))
        self.assertTrue(main_functions.is_within_range(-3, -5, 0))

    # Test Even
    def test_even_number(self):
        self.assertTrue(main_functions.is_even(2))

    def test_odd_number(self):
        self.assertFalse(main_functions.is_even(5))


class TestRedOrBlueFunction(TestCase):
    def test_odd_numbers(self):
        expected = 'Red'
        result = main_functions.red_or_blue(num=3)
        self.assertEqual(expected, result)

    def test_even_greater_than_twenty(self):
        expected = 'Blue'
        result = main_functions.red_or_blue(num=54)
        self.assertEqual(expected, result)

    def test_range_6_to_20(self):
        expected = 'Red'
        result = main_functions.red_or_blue(num=12)
        self.assertEqual(expected, result)

    def test_out_of_range(self):
        with self.assertRaises(AssertionError):
            main_functions.red_or_blue(-1)


if __name__ == '__main__':
    main()
