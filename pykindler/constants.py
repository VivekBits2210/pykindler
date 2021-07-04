def configure_file_locations(custom_dir=None):
    global downloads_dir, not_books_file, temp_metadata_file, processed_dir, temp_metadata_file, processed_dir, convert_dir
    from os import path
    from .utils import get_downloads_folder_location

    downloads_dir = get_downloads_folder_location() if custom_dir is None else custom_dir #TODO: Check if custom_dir is a valid location first
    not_books_file = path.join(downloads_dir, "not_books.txt")
    temp_metadata_file =  path.join(downloads_dir,"temp_metadata_storage.opf")
    processed_dir = path.join(downloads_dir,'Processed_Books')
    convert_dir = path.join(downloads_dir,'Converted_Books')

downloads_dir = not_books_file = temp_metadata_file = processed_dir = convert_dir = None
conversion_threshold_in_mb = 10
extension_list = ['.' + ext for ext in ['pdf','epub','djvu','azw','azw3']]
metadata_command =lambda x: ['fetch-ebook-metadata','--opf','--title', x]
configure_file_locations()