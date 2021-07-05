#!/usr/bin/env python
import sys
from pykindler.utils.bash_utils import (
    get_commandline_args,
    check_commandline_args,
    process_commandline_args,
)
from pykindler.utils.cron_utils import setup_cron_job
from pykindler.convertor import process_and_convert_books
from os import path


def client():
    args = get_commandline_args(sys.argsv[1:])
    msg = check_commandline_args(args)
    if msg is not None:
        print(msg)
        sys.exit(2)
    else:
        file_list, download_dir = process_commandline_args(args)
        if file_list is None and download_dir is None:
            print("Error: Unable to detect downloads folder, please specify --folder")
            sys.exit(2)

        if args.job is True:
            setup_cron_job(args)

        if args.ext is None:
            args.ext = "mobi"

        process_and_convert_books(file_list, download_dir, args)
        print("Exiting...")
        sys.exit()
