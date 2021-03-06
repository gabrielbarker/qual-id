import unittest
from qual_id.category import Category
from test.unit.utils.category_helper import CategoryHelper


class TestCategoryHelper(unittest.TestCase):
    def setUp(self):
        self.category = None

    def test__get_values_error_message__with_valid_category__returns_empty_string(self):
        self.category = MockCategoryWithValidGetValuesMethod()
        error_message = CategoryHelper.get_values_error_message(self.category)
        self.assertEqual(error_message, "")

    def test__get_values_error_message__with_invalid_category_due_to_spaces__returns_error_messages(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_Spaces()
        error_message = CategoryHelper.get_values_error_message(self.category)
        expected_message = "contains invalid strings: value a, value b, value c"
        self.assertEqual(error_message, expected_message)

    def test__get_values_error_message__with_invalid_category_due_to_dashes__returns_error_messages(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_Dashes()
        error_message = CategoryHelper.get_values_error_message(self.category)
        expected_message = "contains invalid strings: value-a, value-b, value-c"
        self.assertEqual(error_message, expected_message)

    def test__get_values_error_message__with_invalid_category_due_to_empty_list__returns_error_messages(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_Empty()
        error_message = CategoryHelper.get_values_error_message(self.category)
        expected_message = "should return non-empty list"
        self.assertEqual(error_message, expected_message)

    def test__get_values_error_message__with_invalid_category_due_to_repeats__returns_error_messages(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_Repeats()
        error_message = CategoryHelper.get_values_error_message(self.category)
        expected_message = "contains repeats: valueb"
        self.assertEqual(error_message, expected_message)

    def test__get_values_error_message__with_invalid_category_due_to_non_alphabetical__returns_error_messages(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_NonAlphabetical()
        error_message = CategoryHelper.get_values_error_message(self.category)
        expected_message = "should be in alphabetical order"
        self.assertEqual(error_message, expected_message)

    def test__get_values_error_message__with_invalid_category_due_to_uppercase__returns_error_messages(
        self,
    ):
        self.category = MockCategoryWithInvalidGetValuesMethod_Uppercase()
        error_message = CategoryHelper.get_values_error_message(self.category)
        expected_message = "contains uppercase strings: valueA, valueB, valueC"
        self.assertEqual(error_message, expected_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()


class MockCategoryWithValidGetValuesMethod(Category):
    def get_values(self):
        return [
            "valuea",
            "valueb",
            "valuec",
        ]


class MockCategoryWithInvalidGetValuesMethod_Spaces(Category):
    def get_values(self):
        return [
            "value a",
            "value b",
            "value c",
        ]


class MockCategoryWithInvalidGetValuesMethod_Dashes(Category):
    def get_values(self):
        return [
            "value-a",
            "value-b",
            "value-c",
        ]


class MockCategoryWithInvalidGetValuesMethod_Empty(Category):
    def get_values(self):
        return []


class MockCategoryWithInvalidGetValuesMethod_Repeats(Category):
    def get_values(self):
        return [
            "valuea",
            "valueb",
            "valueb",
        ]


class MockCategoryWithInvalidGetValuesMethod_NonAlphabetical(Category):
    def get_values(self):
        return [
            "valuec",
            "valuea",
            "valueb",
        ]


class MockCategoryWithInvalidGetValuesMethod_Uppercase(Category):
    def get_values(self):
        return [
            "valueA",
            "valueB",
            "valueC",
        ]
