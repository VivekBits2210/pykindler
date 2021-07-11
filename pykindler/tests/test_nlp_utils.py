import math
import random
import unittest
from unittest import mock
from unittest.case import skip
from pykindler.utils import nlp_utils


class TestNlpUtils(unittest.TestCase):
    @mock.patch("pykindler.utils.nlp_utils.enchant")
    def test_is_word_english(self, mp):
        mp.Dict("en_US").check = lambda x: True
        self.assertEqual(nlp_utils.is_word_english("some_word"), True)

    def test_is_token_good(self):
        from pykindler.constants import bad_tokens

        arg_dict = {
            "longword": True,
            "": False,
            "N": False,
            "he": (False, False),
            "he": (True, True),
        }

        for i in range(math.ceil(len(bad_tokens) / 2)):
            arg_dict[random.choice(bad_tokens)] = False

        for arg_token in arg_dict:
            with mock.patch("pykindler.utils.nlp_utils.is_word_english") as mp:
                dict_output = arg_dict[arg_token]
                expected_output = (
                    dict_output if type(dict_output) is not tuple else dict_output[0]
                )
                mp.return_value = (
                    True if type(dict_output) is not tuple else dict_output[1]
                )
                output = nlp_utils.is_token_good(arg_token)
                self.assertEqual(output, expected_output)

    def test_clean_file_name(self):
        arg_dict = {
            "439021ujref+32-4rei23er.txt": ("ujref er", "txt"),
            "hidfsc #()@there.pdf": ("hidfsc there", "pdf"),
        }

        for arg_filename in arg_dict:
            output = nlp_utils.clean_file_name(arg_filename)
            expected_output = arg_dict[arg_filename]
            self.assertTupleEqual(output, expected_output)
