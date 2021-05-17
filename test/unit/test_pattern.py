import unittest
import random
from qual_id.pattern import Pattern
from unittest.mock import Mock, call, patch


class TestPattern(unittest.TestCase):
    CATEGORY_KEYS = ["first_category", "second_category"]
    CATEGORY_VALUES = ["first_category_value", "second_category_value"]
    PATTERN = "-".join(CATEGORY_KEYS[:2])
    RANDOM_KEY = "random"

    def test__random__pattern__returns_qual_id(self):
        category_names = TestPattern.CATEGORY_KEYS
        mock_collection = self.get_mock_collection()
        pattern = Pattern(category_names, mock_collection)
        
        result = pattern.random()

        self.assertEqual("-".join([self.CATEGORY_VALUES[0]] * 2), result)

    def test__initialisation__pattern__correctly_calls_get_on_collection(self):
        category_names = TestPattern.CATEGORY_KEYS
        mock_collection = self.get_mock_collection()
        
        pattern = Pattern(category_names, mock_collection)

        expected_calls = [call(self.CATEGORY_KEYS[0]), call(self.CATEGORY_KEYS[1])]
        self.assertEqual(expected_calls, mock_collection.get.call_args_list)

    def test__initialisation__pattern_with_randoms__correctly_calls_get_on_collection(
        self,
    ):
        category_names = [self.RANDOM_KEY] * 2
        mock_collection = self.get_mock_collection()
        mock_collection.random.return_value = self.CATEGORY_KEYS[0]
        
        pattern = Pattern(category_names, mock_collection)

        expected_calls = [call(self.CATEGORY_KEYS[0]), call(self.CATEGORY_KEYS[0])]
        self.assertEqual(expected_calls, mock_collection.get.call_args_list)

    def get_mock_collection(self):
        mock = Mock()
        mock.random.return_value = self.mock_category()
        mock.get.return_value = self.mock_category()
        mock.invalid.return_value = []
        return mock

    def mock_category(self):
        mock = Mock()
        mock.random.return_value = self.CATEGORY_VALUES[0]
        return mock


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
