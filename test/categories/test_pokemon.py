import unittest
from qual_id.categories.pokemon import Pokemon
from test.utils.category_helper import CategoryHelper

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pokemon = Pokemon()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.pokemon)
        self.assertTrue(error_message == "", error_message)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()