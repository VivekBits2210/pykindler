from os import path, rename
from subprocess import CalledProcessError, run
from .constants import *
from .utils import trigger_conversion
from .os_utils import make_required_inodes, name_required_inodes, convert_file_to_list
from .nlp_utils import clean_file_name
import logging

logger = logging.getLogger(__name__)


def process_and_convert_books(file_list, folder, args):
    logger.info(f"Processing on folder: {folder}")
    not_books_file, processed_dir, convert_dir = name_required_inodes(folder)
    make_required_inodes([convert_dir, processed_dir], [not_books_file])

    not_book_list = convert_file_to_list(not_books_file)
    not_book_writer = open(not_books_file, "a")

    for filename in file_list:
        absolute_file_path = path.join(folder, filename)

        if args.force and True in set(
            filename.endswith(extension) for extension in extension_list
        ):
            trigger_conversion(absolute_file_path, processed_dir, convert_dir, args.ext)
            continue

        # Move specified extension files as is
        if filename.endswith("." + args.ext):
            rename(absolute_file_path, path.join(convert_dir, filename))
            continue

        # If we looked at this file on last run, ignore
        if filename in not_book_list:
            logger.info(f"File: {filename} ignored, as it was ignored on last run")
            continue

        # Ignore hidden files
        if filename.startswith("."):
            continue

        # Don't convert files which are too big
        file_size_in_mb = path.getsize(absolute_file_path) / 1e6
        if file_size_in_mb > conversion_threshold_in_mb:
            logger.info(
                f"File: {filename} ignored, violates size threshold: {file_size_in_mb} MB > {conversion_threshold_in_mb} MB"
            )
            continue

        if True in set(filename.endswith(extension) for extension in extension_list):
            logger.info(f"Looking at: {filename}")
            cleaned_file_name, ext = clean_file_name(filename)

            # Don't convert small word names, metadata search messes up these
            if len(cleaned_file_name.split()) <= 2:
                logger.info("File name has less than 3 words, ignoring...")
                continue

            # Filter out non-books using calibre's metadata bash calls
            try:
                run(metadata_command(cleaned_file_name), check=True)
                trigger_conversion(
                    absolute_file_path, processed_dir, convert_dir, args.ext
                )
            except CalledProcessError:
                logger.info(f"Not a book: {filename}")
                not_book_writer.write(filename + "\n")
                continue

    # Cleanup
    not_book_writer.close()

    logger.info(
        f"Finished processing folder: {folder}.\n Please check folders {processed_dir} and Converted_Books_{convert_dir} for your books! "
    )
