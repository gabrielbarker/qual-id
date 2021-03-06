import unittest
from qual_id.categories.cake import Cake
from test.unit.utils.category_helper import CategoryHelper


class TestCake(unittest.TestCase):
    def setUp(self):
        self.cake = Cake()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.cake)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
