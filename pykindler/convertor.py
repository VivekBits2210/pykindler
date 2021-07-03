from os import path, rename, remove
from subprocess import check_output, CalledProcessError, run
from .constants import *
from .utils import clean_file_name

def process_and_convert_books(file_list):
    for filename in file_list:
        absolute_file_path = path.join(downloads_dir, filename)

        # Move mobi files as is
        if filename.endswith('.mobi'):
            rename(absolute_file_path, path.join(convert_dir, filename))
            continue

        # Don't convert files which are too big
        file_size_in_mb = path.getsize(absolute_file_path)/1e6
        if file_size_in_mb > conversion_threshold_in_mb:
            continue

        if True in set(filename.endswith(extension) for extension in extension_list):
            cleaned_file_name, ext = clean_file_name(filename)

            # Don't convert one-word names, metadata search messes up these
            if len(cleaned_file_name.split()) <= 1:
                continue

            # Filter out non-books using calibre's metadata bash calls
            try:
                print(f"Looking at: {filename}")
                temp_metadata_storage = open(temp_metadata_file, "w")
                run(metadata_command(cleaned_file_name), stdout=temp_metadata_storage, check=True)

                #Move conversion to Converted and book to Processed
                print(f"Beginning conversion: {filename}")
                check_output(['ebook-convert',
                              absolute_file_path,
                              path.join(convert_dir, filename[:filename.rfind('.')]+'.mobi')
                             ])
                rename(absolute_file_path, path.join(processed_dir,filename))
                print(f"Completed Conversion: {filename}")
            except CalledProcessError: 
                #Does not have metadata, therefore not a book, continue to next
                continue

    # Cleanup
    if path.exists(temp_metadata_file):
        remove(temp_metadata_file)