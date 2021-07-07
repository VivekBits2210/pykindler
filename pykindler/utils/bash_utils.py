from os import path, listdir
from ..constants import argument_dict


def construct_parser():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    for argument, info in argument_dict.items():
        help = info[0]
        action = info[1] if len(info) > 1 else None
        if action is None:
            parser.add_argument("--" + argument, help=help)
        else:
            parser.add_argument("--" + argument, help=help, action=action)


def get_commandline_args(args):
    parser = construct_parser()
    args = parser.parse_args(args)
    return args


def check_commandline_args(args):
    from ..constants import valid_extensions_for_conversion
    import re

    is_dir = path.isdir(args.folder) if args.folder is not None else True
    is_kindle = (
        False
        if args.kindle is not None and not args.kindle.endswith("@kindle.com")
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
    if not is_kindle:
        return f"Error: {args.kindle} is not a valid Kindle e-mail address!"
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
