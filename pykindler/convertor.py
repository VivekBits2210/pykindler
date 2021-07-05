from os import path, rename
from subprocess import CalledProcessError, check_output
from .constants import *
from .utils.convert_utils import trigger_conversion
from .utils.os_utils import (
    make_required_inodes,
    name_required_inodes,
    convert_file_to_list,
)
from .utils.nlp_utils import clean_file_name


def process_and_convert_books(file_list, folder, args):
    print(f"Processing on folder: {folder}")
    not_books_file, processed_dir, convert_dir = name_required_inodes(folder)
    make_required_inodes([convert_dir, processed_dir], [not_books_file])

    not_book_list = convert_file_to_list(not_books_file)
    not_book_writer = open(not_books_file, "a")

    converted_files = []

    for filename in file_list:
        absolute_file_path = path.join(folder, filename)

        if args.force and True in set(
            filename.endswith(extension) for extension in extension_list
        ):
            converted_file_path = trigger_conversion(
                absolute_file_path, processed_dir, convert_dir, args.ext
            )
            converted_files.append(converted_file_path)
            continue

        # Move specified extension files as is
        if filename.endswith("." + args.ext):
            rename(absolute_file_path, path.join(convert_dir, filename))
            converted_files.append(path.join(convert_dir, filename))
            continue

        # If we looked at this file on last run, ignore
        if filename in not_book_list:
            print(f"File: {filename} ignored, as it was ignored on last run")
            continue

        # Ignore hidden files
        if filename.startswith("."):
            continue

        # Don't convert files which are too big
        file_size_in_mb = path.getsize(absolute_file_path) / 1e6
        if file_size_in_mb > conversion_threshold_in_mb:
            print(
                f"File: {filename} ignored, violates size threshold: {file_size_in_mb} MB > {conversion_threshold_in_mb} MB"
            )
            continue

        if True in set(filename.endswith(extension) for extension in extension_list):
            print(f"Looking at: {filename}")
            cleaned_file_name, ext = clean_file_name(filename)

            # Don't convert small word names, metadata search messes up these
            if len(cleaned_file_name.split()) <= 2:
                print("File name has less than 3 words, ignoring...")
                continue

            # Filter out non-books using calibre's metadata bash calls
            try:
                # run(metadata_command(cleaned_file_name), check=True)
                check_output(metadata_command(cleaned_file_name))
                converted_file_path = trigger_conversion(
                    absolute_file_path, processed_dir, convert_dir, args.ext
                )
                converted_files.append(converted_file_path)
            except CalledProcessError:
                print(f"Not a book: {filename}")
                not_book_writer.write(filename + "\n")
                continue

    # Cleanup
    not_book_writer.close()

    print(
        f"Finished processing folder: {folder}.\n Please check folders {processed_dir} and {convert_dir} for your books! "
    )

    return converted_files
