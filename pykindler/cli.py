#!/usr/bin/env python
import sys
import logging
from pykindler.utils.bash_utils import (
    get_commandline_args,
    check_option_args_validity,
    process_commandline_args,
)
from pykindler.utils.cron_utils import setup_cron_job
from pykindler.convertor import process_and_convert_books
from os import path

logger = logging.getLogger(__name__)


def client():
    args = get_commandline_args()
    msg = check_option_args_validity(args)
    if msg is not None:
        logger.error(msg)
        sys.exit(2)
    else:
        file_list, download_dir = process_commandline_args(args)
        if file_list is None and download_dir is None:
            logger.error(
                "Error: Unable to detect downloads folder, please specify --folder"
            )
            sys.exit(2)

        if args.job is True:
            setup_cron_job(args)

        process_and_convert_books(file_list, download_dir, args)
        logger.info("Exiting...")
        sys.exit()
