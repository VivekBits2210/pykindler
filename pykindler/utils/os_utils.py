# Finds your downloads location
from os import makedirs, path
from ..constants import file_appended_hash


def get_downloads_folder_location():
    try:  # GTK2
        import glib

        downloads_dir = glib.get_user_special_dir(glib.USER_DIRECTORY_DOWNLOAD)
    except (ModuleNotFoundError, AttributeError) as e:  # GTK3
        try:
            from pgi.repository import GLib

            downloads_dir = GLib.get_user_special_dir(
                GLib.UserDirectory.DIRECTORY_DOWNLOAD
            )
        except (ModuleNotFoundError, AttributeError) as e:  # GTK3
            downloads_dir = None
    return downloads_dir


def make_required_inodes(dir_list, file_list):
    for directory in dir_list:
        if not path.exists(directory):
            makedirs(directory)
    for file in file_list:
        if not path.exists(file):
            open(file, "a").close()


def name_required_inodes(folder):
    not_books_file = path.join(folder, f"not_books_{file_appended_hash}.txt")
    processed_dir = path.join(folder, f"Processed_Books_{file_appended_hash}")
    convert_dir = path.join(folder, f"Converted_Books_{file_appended_hash}")
    return not_books_file, processed_dir, convert_dir


def convert_file_to_list(file):
    try:
        line_list = open(file, "r").read().splitlines()
    except FileNotFoundError:
        line_list = []
    return line_list
