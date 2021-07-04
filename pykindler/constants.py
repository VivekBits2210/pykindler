conversion_threshold_in_mb = 10
valid_extensions_for_conversion = ["." + ext for ext in ["azw3", "epub", "mobi"]]
extension_list = ["." + ext for ext in ["pdf", "epub", "djvu", "azw", "azw3"]]
metadata_command = lambda x: ["fetch-ebook-metadata", "--opf", "--title", x]
