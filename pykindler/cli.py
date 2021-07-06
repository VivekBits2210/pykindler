#!/usr/bin/env python
import sys
from pykindler.utils.bash_utils import (
    get_commandline_args,
    check_commandline_args,
    process_commandline_args,
)
from .utils.cron_utils import setup_cron_job
from .utils.email_utils import *
from .convertor import process_and_convert_books
from os import path


def client():
    args = get_commandline_args(sys.argv[1:])
    error_message = check_commandline_args(args)
    if error_message is not None:
        print(error_message)
        sys.exit(2)

    file_list, download_dir = process_commandline_args(args)
    if file_list is None and download_dir is None:
        print("Error: Unable to detect downloads folder, please specify --folder")
        sys.exit(2)

    if args.job is True:
        setup_cron_job(args)

    if args.ext is None:
        args.ext = "mobi"

    if bool(args.email is None) != bool(args.kindle is None):
        print("Error: To auto-email, please provide both --email and --kindle")
        sys.exit(2)

    try:
        session_object = GmailSession(args.email) if args.email is not None else None
        print("Credentials are valid! Books will be e-mailed after conversion...\n")
    except OSError:
        print("Error: Please enter valid e-mail credentials!")
        sys.exit(2)

    converted_file_list = process_and_convert_books(file_list, download_dir, args)
    if args.email is not None:
        print("\n Auto-emailing books to Kindle...")
        send_a_bunch_of_files_to_kindle(
            session_object, converted_file_list, args.email, args.kindle
        )

    print("Exiting...")
    sys.exit()
