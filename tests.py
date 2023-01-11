import unittest
from functions import divide
from functions import my_func
from functions import your_func
from functions import show_user_data
from functions import my_gen


class TestMyFuncs(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(divide(9, 3), 3)

    def test_not_equal(self):
        self.assertNotEqual(divide(9, 3), 'none')

    def test_true(self):
        self.assertTrue(type(my_func(8, 11, 2)) == str)

    def test_false(self):
        self.assertFalse(my_func(8, 11, 2) == str)

    def test_is(self):
        self.assertIs(my_func, your_func)

    def test_not_is(self):
        self.assertIsNot(my_func, show_user_data)

    def test_in(self):
        self.assertIn('Istanbul,', (show_user_data(
            surname='Smith',
            phone='+0(101)0111010',
            name='Jeffrey',
            email="jeffrey.smith@gb.com",
            current_city='Istanbul',
            birthday='04.24.1996')).split(' '))

    def test_not_in(self):
        self.assertNotIn('Moscow,', (show_user_data(
            surname='Smith',
            phone='+0(101)0111010',
            name='Jeffrey',
            email="jeffrey.smith@gb.com",
            current_city='Istanbul',
            birthday='04.24.1996')).split(' '))

    def test_instance(self):
        self.assertIsInstance(my_gen, list)

    def test_not_is_instance(self):
        self.assertNotIsInstance(my_gen, tuple)
