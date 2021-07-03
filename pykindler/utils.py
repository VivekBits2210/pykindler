from os import path, makedirs
# Finds your downloads location
def get_downloads_folder_location():
    try: #GTK2
        import glib
        downloads_dir = glib.get_user_special_dir(glib.USER_DIRECTORY_DOWNLOAD)
    except (ModuleNotFoundError, AttributeError) as e: #GTK3
        from gi.repository import GLib
        downloads_dir = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD)
    return downloads_dir

# Check if word is english
def is_word_english(word):
    import enchant
    return enchant.Dict("en_US").check(word)

# Check if token is helpful to find metadatas
def is_token_good(token):
    bad_tokens=['ltd','libgen','org','www','com','co']
    if len(token)<=3 and not is_word_english(token):
        return False
    if len(token)<=1:
        return False
    if token in bad_tokens:
        return False
    return True

#EMCODE: clean_name = re.sub(r'\b\w{1,2}\b', '', clean_name) #Remove small tokens
# Clean file names to help find metadata better
def clean_file_name(filename):
    import re
    extension = filename[filename.rfind('.')+1:]
    clean_name = filename[:filename.rfind('.')] #Extension removal
    clean_name = re.sub(r'[^A-Za-z\' ]+', ' ',clean_name) #Keep only letters and spaces
    clean_name = re.sub(r' +', ' ', clean_name) #Remove extra spaces
    clean_name = clean_name.strip().lower()
    clean_name = ' '.join([word for word in clean_name.split() if is_token_good(word)])
    return clean_name, extension

def make_required_directories(dir_list):
    for directory in dir_list:
        if not path.exists(directory):
            makedirs(directory)