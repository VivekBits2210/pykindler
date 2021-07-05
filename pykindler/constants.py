conversion_threshold_in_mb = 10
gmail_attachment_threshold_mb = 25
valid_extensions_for_conversion = ["pdf", "djvu", "azw3", "epub", "mobi"]
extension_list = ["." + ext for ext in ["pdf", "epub", "djvu", "azw", "azw3", "mobi"]]
metadata_command = lambda x: ["fetch-ebook-metadata", "--opf", "--title", x]
file_appended_hash = "30234f2413d43e5c"
