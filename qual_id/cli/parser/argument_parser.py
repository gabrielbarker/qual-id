from argparse import ArgumentParser as ArgParser, Namespace, Action
from .command import Command
from qual_id.groups import GroupFactory
from qual_id.groups.all import All


class ArgumentParser:
    def __init__(self):
        self._parser = ArgumentParser._create_parser()

    def parse(self, arguments) -> Namespace:
        return self._parser.parse_args(arguments)

    @staticmethod
    def _create_parser() -> ArgParser:
        parser = ArgumentParser._create_main_parser()
        ArgumentParser._create_info_subparser(parser)
        return parser

    @staticmethod
    def _create_main_parser() -> ArgParser:
        description = "Qual ID: generate random qualitative ID's"
        parser = ArgParser(prog="qid", description=description)
        ArgumentParser._add_main_arguments_to(parser)
        parser.set_defaults(command=Command.MAIN)
        return parser

    @staticmethod
    def _create_info_subparser(main_parser) -> None:
        subparsers = main_parser.add_subparsers(title="sub-commands")
        description = "Qual ID info: get info on Qual ID elements"
        parser = subparsers.add_parser(
            "info", description=description, help="info --help", aliases=["i"]
        )
        ArgumentParser._add_info_arguments_to(parser)
        parser.set_defaults(command=Command.INFO)

    @staticmethod
    def _add_main_arguments_to(parser) -> None:
        parser.add_argument(
            "-c",
            "--categories",
            action=ArgumentParser.RequiredLength,
            nargs="+",
            choices=list(All.info()),
            metavar="CATEGORY",
        )
        parser.add_argument(
            "-g",
            "--group",
            default="all",
            choices=list(GroupFactory.info()),
            metavar="GROUP",
        )
        parser.add_argument(
            "-f", "--format", default="csv", choices=["csv", "json"], metavar="FORMAT"
        )
        parser.add_argument("-n", "--number", default=1, type=int)

    @staticmethod
    def _add_info_arguments_to(parser) -> None:
        parser.add_argument(
            "-c",
            "--category",
            nargs="?",
            default=False,
            choices=list(All.info()),
            metavar="CATEGORY",
        )
        parser.add_argument(
            "-g",
            "--group",
            nargs="?",
            default=False,
            choices=list(GroupFactory.info()),
            metavar="GROUP",
        )
        parser.add_argument("-f", "--format", action="store_true")

    class RequiredLength(Action):
        MINIMUM = 1
        MAXIMUM = 5

        def __call__(self, parser, args, values, option_string=None):
            if not (self.MINIMUM <= len(values) <= self.MAXIMUM):
                parser.error(self._get_error_message())
            setattr(args, self.dest, values)

        def _get_error_message(self):
            template = 'argument "{arg}" requires between {min} and {max} arguments'
            return template.format(arg=self.dest, min=self.MINIMUM, max=self.MAXIMUM)
