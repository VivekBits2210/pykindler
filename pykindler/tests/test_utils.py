from re import L
import unittest
from ..utils import *


class TestUtils(unittest.TestCase):
    def test_check_option_args_validity(self):
        from os import path

        argument_dict = {
            (None, None, None): True,
            (None, "", None): False,
            (None, "str@gmail.com", None): False,
            (None, "valid_email_format@gmail.com", None): True,
            (None, "valid_email_format@gmail.com", "/homie"): False,
            (None, None, "/homie"): False,
            (None, None, "/home"): False,
            ("/home", None, None): True,
            ("/home", None, path.dirname(path.abspath(__file__))): True,
            (
                "/home",
                "valid_email_format@gmail.com",
                path.dirname(path.abspath(__file__)),
            ): True,
        }
        for arg_tuple, output in argument_dict.items():
            self.assertEqual(check_option_args_validity(*arg_tuple), output)

    def test_setup_cron_job(self):
        from crontab import CronTab

        cron = CronTab(user=True)
        num_jobs = 0
        job_string = ""
        setup_cron_job("\home")
        for job in cron:
            if "pykindler-run" in str(job):
                job_string = str(job)
                num_jobs += 1

        for job in cron:
            if "pykindler-run -d \home" in str(job):
                cron.remove(job)
        cron.write()
        self.assertTrue(str(job).startswith("* */12 * * * pykindler-run"))
        self.assertEqual(num_jobs, 1)

    def test_get_downloads_folder_location(self):
        import sys
        from os.path import isdir

        self.assertNotEqual(get_downloads_folder_location, None)
        self.assertTrue(isdir(get_downloads_folder_location))
        sys.modules["glib"] = None
        sys.modules["pgi"] = None
        self.assertEqual(get_downloads_folder_location, None)

    def test_is_word_english(self):
        english_words = ["word", "delicious", "apple", "book", "entertainment"]
        not_english_words = ["kabooboo", "flimflong", "plumbus", "usukusuku"]
        for word in english_words:
            self.assertTrue(is_word_english(word))
        for word in not_english_words:
            self.assertFalse(is_word_english(word))

    def test_clean_file_name(self):
        arg_dict = {
            "40U93JFDSDdfofile xyz": "ujfdsddfofile xyz",
            "file)$#)@!($*#@!)$(*#@$name     24-23940324#_@%(": "filename",
            "in 2004, we met the dude": "in we met the dude",
        }
        for word, output in arg_dict.items():
            self.assertEqual(clean_file_name(word), output)

    def test_make_required_directories(self):
        # TODO I'm not sure how to test this utility
        self.assertTrue(True)

    def test_email_book(self):
        # TODO I'm not sure how to test this utility
        self.assertTrue(True)
