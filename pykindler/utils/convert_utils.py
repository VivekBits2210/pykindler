from os import path


def trigger_conversion(absolute_file_path, processed_dir, convert_dir, extension):
    from subprocess import check_output
    from os import rename

    filename = path.basename(absolute_file_path)
    print(f"Beginning conversion: {filename}")
    converted_file_name = filename[: filename.rfind(".")] + "." + extension
    converted_file_path = path.join(convert_dir, converted_file_name)
    check_output(["ebook-convert", absolute_file_path, converted_file_path])
    rename(absolute_file_path, path.join(processed_dir, filename))
    print(f"Completed Conversion: {converted_file_name}")
    return converted_file_path
