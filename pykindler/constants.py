from os import path
from .utils import get_downloads_folder_location
conversion_threshold_in_mb = 10,
extension_list = ['.' + ext for ext in ['pdf','epub','djvu','azw','azw3']]
metadata_command =lambda x: ['fetch-ebook-metadata','--opf','--title', x]
downloads_dir = get_downloads_folder_location()
temp_metadata_file =  path.join(downloads_dir,"temp_metadata_storage.opf")
processed_dir = path.join(downloads_dir,'Processed_Books')
converted_dir = path.join(downloads_dir,'Converted_Books')