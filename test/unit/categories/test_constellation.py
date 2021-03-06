import unittest
from qual_id.categories.constellation import Constellation
from test.unit.utils.category_helper import CategoryHelper


class TestConstellation(unittest.TestCase):
    def setUp(self):
        self.constellation = Constellation()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.constellation)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
