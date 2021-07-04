from re import L
import unittest
from unittest.case import skip
from pykindler.utils import *


class TestUtils(unittest.TestCase):
    def test_check_option_args_validity(self):
        from os import path

        argument_dict = {
            (None, None, None, None): True,
            (None, "", None, None): False,
            (None, "str@gmail.com", None, None): False,
            (None, "valid_email_format@gmail.com", None, None): False,
            (None, "valid_email_format@gmail.com", "/homie", None): False,
            (None, "genuinevalidformat@gmail.com", "/home", None): False,
            (None, None, "/homie", None): False,
            (None, None, "/home", None): False,
            ("/home", None, None, None): True,
            ("/home", None, path.abspath(__file__), None): True,
            (
                "/home",
                "validformat2210@gmail.com",
                path.abspath(__file__),
                None,
            ): True,
            (
                "/home",
                "validformat2210@gmail.com",
                path.abspath(__file__),
                "epu",
            ): False,
            (
                "/home",
                "validformat2210@gmail.com",
                path.abspath(__file__),
                "epub",
            ): True,
            (
                "/home",
                "validformat2210@gmail.com",
                path.abspath(__file__),
                "mobi",
            ): True,
            (
                "/home",
                "validformat2210@gmail.com",
                path.abspath(__file__),
                "azw3",
            ): True,
        }
        for arg_tuple, output in argument_dict.items():
            if output:
                self.assertEqual(check_option_args_validity(*arg_tuple), None)
            else:
                self.assertNotEqual(check_option_args_validity(*arg_tuple), None)

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
        self.assertTrue(job_string.startswith("* */12 * * * pykindler-run"))
        self.assertEqual(num_jobs, 1)

    # TODO: Install glib in pipeline before running this test
    @skip
    def test_get_downloads_folder_location(self):
        import sys
        from os.path import isdir

        self.assertNotEqual(get_downloads_folder_location(), None)
        self.assertTrue(isdir(get_downloads_folder_location()))
        sys.modules["glib"] = None
        sys.modules["pgi"] = None
        # TODO: Learn how to accurately fake absence of modules
        # self.assertEqual(get_downloads_folder_location(), None)

    def test_is_word_english(self):
        english_words = ["word", "delicious", "apple", "book", "entertainment"]
        not_english_words = ["kabooboo", "flimflong", "plumbus", "usukusuku"]
        for word in english_words:
            self.assertTrue(is_word_english(word))
        for word in not_english_words:
            self.assertFalse(is_word_english(word))

    def test_clean_file_name(self):
        arg_dict = {
            "40U93JFDSDdfofile xyz.mobi": ("jfdsddfofile", "mobi"),
            "file)$#)@!($*#@!)$(*#@$name     24-23940324#_@%(.pdf": (
                "file name",
                "pdf",
            ),
            "in 2004, we met the dude.epub": ("in we met the dude", "epub"),
        }
        for word, output in arg_dict.items():
            print("OUT", clean_file_name(word))
            self.assertTupleEqual(clean_file_name(word), output)

    def test_make_required_directories(self):
        # TODO I'm not sure how to test this utility
        self.assertTrue(True)

    def test_email_book(self):
        # TODO I'm not sure how to test this utility
        self.assertTrue(True)
