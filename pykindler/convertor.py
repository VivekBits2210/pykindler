from os import path, rename, remove
from subprocess import check_output, CalledProcessError, run
from .constants import *
from .utils import clean_file_name, make_required_directories

def process_and_convert_books(file_list,downloads_dir):
    not_books_file = path.join(downloads_dir, "not_books.txt")
    temp_metadata_file = path.join(downloads_dir,"temp_metadata_storage.opf")
    processed_dir = path.join(downloads_dir,'Processed_Books')
    convert_dir = path.join(downloads_dir,'Converted_Books')
    make_required_directories([convert_dir,processed_dir])

    print(f"Processing on folder: {downloads_dir}")

    # Fetch cache of items confirmed to not be books
    try:
        not_book_list = open(not_books_file, "r").read().splitlines()
    except FileNotFoundError:
        not_book_list = []
    not_book_writer = open(not_books_file, "a")

    for filename in file_list:
        absolute_file_path = path.join(downloads_dir, filename)
    
        # Move mobi files as is
        if filename.endswith('.mobi'):
            rename(absolute_file_path, path.join(convert_dir, filename))
            continue
            
        # If we looked at this file on last run, ignore
        if filename in not_book_list:
            continue

        # Ignore hidden files
        if filename.startswith('.'):
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
                print(f"Not a book: {filename}")
                #Does not have metadata, therefore not a book, cache name and continue to next
                not_book_writer.write(filename+'\n')
                continue

    # Cleanup
    if path.exists(temp_metadata_file):
        remove(temp_metadata_file)
    not_book_writer.close()

    print(f'Finished processing folder: {downloads_dir}')