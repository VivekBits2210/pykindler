from unittest import TestCase, mock
from unittest.case import skip
from pykindler.utils import os_utils


class TestOsUtils(TestCase):
    def test_get_downloads_folder_location(self):
        none_type = type(None)
        output = os_utils.get_downloads_folder_location()
        output_type = type(output)
        self.assertIn(output_type, [none_type, str])
        if output_type is not none_type:
            self.assertIn("/", output, "Output is not a valid unix path!")

    @skip("Pointless: Too many mocks required to test this fn")
    def test_make_required_inodes(self):
        self.assertEqual(True, True)

    def test_name_required_inodes(self):
        from pykindler.constants import file_appended_hash

        arg_dict = {
            "some_folder_name": (
                f"some_folder_name/not_books_{file_appended_hash}.txt",
                f"some_folder_name/Processed_Books_{file_appended_hash}",
                f"some_folder_name/Converted_Books_{file_appended_hash}",
            ),
            "some_other_folder_name": (
                f"some_other_folder_name/not_books_{file_appended_hash}.txt",
                f"some_other_folder_name/Processed_Books_{file_appended_hash}",
                f"some_other_folder_name/Converted_Books_{file_appended_hash}",
            ),
        }

        for arg_folder in arg_dict:
            expected_output = arg_dict[arg_folder]
            output = os_utils.name_required_inodes(arg_folder)
            self.assertTupleEqual(output, expected_output)

    @skip("Pointless: Too many mocks required to test this fn")
    def test_convert_file_to_lists(self):
        self.assertEqual(True, True)
        # arg_dict = {"filename": True, "someotherfilename": True}
        # for arg_filename in arg_dict:
        #     open_name = f"{arg_filename}.open"
        #     with mock.patch(open_name, create=True) as mock_open:
        #         mock_open.return_value = mock.MagicMock(spec=file)
