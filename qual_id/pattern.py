from random import choice
from qual_id.category_map import CategoryMap


class Pattern:
    __random_key = "random"

    def __init__(self, pattern_string, category_map):
        self.__categories = [p for p in pattern_string.split("-") if p != ""]
        self.__category_map = category_map
        self.__replace_randoms()

    def get_categories(self):
        return [self.__category_map.get(category) for category in self.__categories]

    def error(self):
        if not self.__valid_number_of_categories():
            return "number of categories should be between 1 and 5"
        invalid = self.__category_map.invalid(self.__categories)
        if invalid:
            return "invalid categories: %s" % (invalid)
        return False

    def __valid_number_of_categories(self):
        return 0 < len(self.__categories) < 6

    def __replace_randoms(self):
        self.__categories = [self.__replace_random(x) for x in self.__categories]

    def __replace_random(self, category):
        if category == Pattern.__random_key:
            return self.__random_category()
        return category

    def __random_category(self):
        return choice(self.__category_map.categories())
