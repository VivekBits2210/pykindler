import random, math
from itertools import chain
from unittest import TestCase, mock
from argparse import ArgumentParser
from pykindler.utils import bash_utils
from pykindler.constants import argument_dict, valid_extensions_for_conversion


class TestBashUtils(TestCase):
    def setUp(self) -> None:
        self.parser = bash_utils.construct_parser()

    def test_construct_parser(self):
        self.parser = bash_utils.construct_parser()
        self.assertIsInstance(
            self.parser, ArgumentParser, "parser object not the right instance!"
        )

    def test_load_arguments(self):
        self.args = bash_utils.load_arguments(
            self.parser, argument_dict
        )  # Should run without complaints
        self.assertEqual(True, True)

    def test_get_command_line_args(self):
        one_tenth_of_possibilities = math.ceil(
            (pow(2, len(argument_dict.keys()) - 1) / 10)
        )
        arg_list = []
        for key in argument_dict:
            option = "--" + key
            if len(argument_dict[key]) == 1:
                arg_list.append((option, "some_string"))
            else:
                arg_list.append((option,))

        for i in range(one_tenth_of_possibilities):
            arbitrary_size = random.randint(1, len(arg_list))
            arbitrary_choice_of_arguments = random.sample(arg_list, arbitrary_size)
            flat_argument_list = list(chain(*arbitrary_choice_of_arguments))
            bash_utils.get_commandline_args(
                flat_argument_list
            )  # Should run without complaints
            self.assertEqual(True, True)

    def test_check_commandline_args(self):
        arg_list_cases = {
            ("--folder", "some_string"): False,
            ("--folder", "some_string", "pykindler.utils.bash_utils.path.isdir"): False,
            ("--kindle", "valid@kindle.com"): True,
            ("--kindle", "notvalid@kindle.c"): False,
            ("--file", "some_string"): False,
            ("--file", "some_string", "pykindler.utils.bash_utils.path.isfile"): False,
            ("--ext", None): True,
            ("--ext", random.choice(valid_extensions_for_conversion)): True,
            ("--ext", "some_string"): False,
        }

        for arg_list_tuple in arg_list_cases:
            arg_list = list(arg_list_tuple)[:2]
            if len(arg_list_tuple) == 2:
                output = bash_utils.check_commandline_args(
                    bash_utils.get_commandline_args(arg_list)
                )
            else:
                with mock.patch(arg_list_tuple[2]) as mp:
                    mp.return_value = False
                    output = bash_utils.check_commandline_args(
                        bash_utils.get_commandline_args(arg_list)
                    )
            if arg_list_cases[arg_list_tuple]:
                self.assertEqual(output, None)
            else:
                self.assertIn("Error", output)

    @mock.patch("pykindler.utils.bash_utils.listdir", return_value=["f1", "f2", "f3"])
    def test_process_commandline_args(self, mock1):
        arg_dict = {
            (None, None, None): (None, None),
            ("/path/some_file", "/path/some_folder", None): (
                ["some_file"],
                "/path",
            ),
            ("/path/some_file", "/path/some_folder", "/path/to/downloads"): (
                ["some_file"],
                "/path",
            ),
            ("/path/some_file", "/path/some_folder", "/path/to/downloads"): (
                ["some_file"],
                "/path",
            ),
            (None, "/path/some_folder", "/path/to/downloads"): (
                ["f1", "f2", "f3"],
                "/path/some_folder",
            ),
            (None, None, "/path/to/downloads"): (
                ["f1", "f2", "f3"],
                "/path/to/downloads",
            ),
        }

        for arg_tuple in arg_dict:
            args = mock.MagicMock()
            args.file = arg_tuple[0]
            args.folder = arg_tuple[1]
            with mock.patch(
                "pykindler.utils.bash_utils.get_downloads_folder_location",
                return_value=arg_tuple[2],
            ):
                output = bash_utils.process_commandline_args(args)
                self.assertTupleEqual(arg_dict[arg_tuple], output)
