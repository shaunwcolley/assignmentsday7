import unittest
from grocerylist import *
from grocery_item import GroceryItem
from shopping_list import ShoppingList

#Following is not working,
#unclear on how to test functions that take in user input
class GrocerListTest(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList()
    def test_add_list(self):
        result = add_list()
        self.assertEqual(("HEB", "Produce"), result)

unittest.main()
