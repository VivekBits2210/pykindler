# Check if word is english
def is_word_english(word):
    import enchant

    return enchant.Dict("en_US").check(word)


# Check if token is helpful to find metadatas
def is_token_good(token):
    bad_tokens = ["ltd", "libgen", "org", "www", "com", "co"]
    if len(token) <= 3 and not is_word_english(token):
        return False
    if len(token) <= 1:
        return False
    if token in bad_tokens:
        return False
    return True


# Clean file names to help find metadata better
def clean_file_name(filename):
    import re

    extension = filename[filename.rfind(".") + 1 :]
    clean_name = filename[: filename.rfind(".")]
    clean_name = re.sub(r"[^A-Za-z\' ]+", " ", clean_name)
    clean_name = re.sub(r" +", " ", clean_name)
    clean_name = clean_name.strip().lower()
    clean_name = " ".join([word for word in clean_name.split() if is_token_good(word)])
    return clean_name, extension
