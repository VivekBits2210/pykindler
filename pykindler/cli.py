#!/usr/bin/env python
import sys, getopt
from pykindler.utils import (
    check_option_args_validity,
    setup_cron_job,
    get_downloads_folder_location,
)
from pykindler.convertor import process_and_convert_books
from os import listdir, path


def main():
    argv = sys.argv[1:]
    usage = """
    pykindler-run 
    [-d <custom folder to run on (defaults to your downloads folder if you don't specify)>] 
    [-f <absolute file path to convert, if you'd like just one file converted>] 
    [-e <kindle email id>] 
    [-x <custom extension to convert to (defualts to mobi if you don't specify)>] 
    [-c Y (if you want a twice-a-day conversion job for the specified downloads folder)]
    """
    try:
        opts, args = getopt.getopt(argv, "hd:f:e:c:x:")
    except getopt.GetoptError:
        print(f"Usage: {usage}")
        sys.exit(2)
    dwd = email = file = None
    extension = "mobi"
    cron = False
    for opt, arg in opts:
        if opt == "-h":
            print(f"Usage: {usage}")
            sys.exit()
        if opt == "-f":
            file = arg
        elif opt == "-d":
            dwd = arg
        elif opt == "-e":
            email = arg
        elif opt == "-c" and arg == "Y":
            cron = True
        elif opt == "-x":
            extension = arg
    msg = check_option_args_validity(dwd, email, file, extension)
    if msg is not None:
        print(msg)
        sys.exit(2)
    else:
        if cron is True:
            setup_cron_job(dwd)
        download_dir = get_downloads_folder_location() if dwd is None else dwd
        if download_dir is None:
            print(
                "Error: Could not detect your downloads folder, please enter it manually via -d"
            )
            sys.exit(2)
        file_list = listdir(download_dir)
        if file is not None:
            file_list = [path.basename(file)]
            download_dir = path.split(file)[0]
        process_and_convert_books(file_list, download_dir, extension)
        print("Exiting...")
        sys.exit()
