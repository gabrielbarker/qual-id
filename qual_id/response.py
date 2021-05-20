from qual_id.config import Config
from qual_id.validators import Validator
from qual_id.groups import GroupFactory
from qual_id.pattern import Pattern


class Response:
    def __init__(self, args):
        self._config = Config(args)

    def get_response_obj(self):
        response_obj = {}
        validator = Validator(self._config)
        validator.validate()

        if validator.is_valid():
            response_obj["data"] = self.get_qual_ids()
        else:
            response_obj["error"] = validator.error_message()
        return self.__format_response(response_obj)

    def get_qual_ids(self):
        group = GroupFactory.get(self._config.get_group())
        pattern = Pattern(self._config.get_categories(), group)
        return [pattern.random() for _ in range(self._config.get_number())]

    def __format_response(self, response_obj):
        if self._config.get_format() == "csv":
            return self.__data_or_error(response_obj)
        return response_obj

    def __data_or_error(self, response_obj):
        if "data" in response_obj:
            return ",".join(response_obj["data"])
        return response_obj["error"]
