from os import path, listdir


def get_commandline_args():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "--folder",
        help="folder to run conversion on (defaults to downloads if not specified)",
    )
    parser.add_argument(
        "--file",
        help="absolute file path for conversion, if you want a single file converted",
    )
    parser.add_argument(
        "--kindle",
        help="your Kindle email-id, books are auto-emailed to here after conversion",
    )
    parser.add_argument(
        "--email",
        help="your personal email-id, books are auto-emailed from here after conversion (use with --kindle for the first ever run, to store credentials)",
    )
    parser.add_argument(
        "--ext", help="extension to convert to (defaults to mobi if not specified)"
    )
    parser.add_argument(
        "--job",
        help="setups a twice-a-day conversion job for specified folder (or downloads)",
        action="store_true",
    )
    parser.add_argument(
        "--force",
        help="Convert without checking if it is a book or within safe size threshold (only extension check is performed)",
        action="store_true",
    )
    args = parser.parse_args()
    return args


def check_option_args_validity(args):
    from ..constants import valid_extensions_for_conversion
    import re

    is_dir = path.isdir(args.folder) if args.folder is not None else True
    is_email = (
        False
        if args.email is not None
        and not re.match(r"^[a-z0-9](\.?[a-z0-9]){5,}@g(oogle)?mail\.com$", args.email)
        else True
    )
    is_file = path.isfile(args.file) if args.file is not None else True
    is_extension = (
        False
        if args.ext is not None and args.ext not in valid_extensions_for_conversion
        else True
    )

    if not is_dir:
        return f"Error: {args.folder} is not an existing directory!"
    if not is_email:
        return f"Error: {args.email} is not a valid Kindle e-mail address!"
    if not is_file:
        return f"Error: {args.file} does not exist or is not a valid file!"
    if not is_extension:
        return f"Error: {args.ext} extension not present in {valid_extensions_for_conversion}"

    return None


def process_commandline_args(args):
    from .os_utils import get_downloads_folder_location

    if args.file is not None:
        file_list = [path.basename(args.file)]
        download_dir = path.split(args.file)[0]
        return file_list, download_dir
    if args.folder is not None:
        file_list = listdir(args.folder)
        return file_list, args.folder
    else:
        download_dir = get_downloads_folder_location()
        if download_dir is None:
            return None, None
        file_list = listdir(download_dir)
        return file_list, download_dir
