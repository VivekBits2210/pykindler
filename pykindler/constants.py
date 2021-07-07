argument_dict = {
    "folder": ("folder to run conversion on (defaults to downloads if not specified)",),
    "file": ("absolute file path for conversion, if you want a single file converted",),
    "kindle": ("your Kindle email-id, converted books are emailed to here",),
    "email": ("your personal email-id, converted books are emailed from here",),
    "ext": ("extension to convert to (defaults to mobi if not specified)",),
    "job": ("sets up a twice-a-day conversion job for specified folder", "store_true"),
    "force": ("only perform extensions check before converting", "store_true"),
    "askcred": ("re-enter your email password, override the stored one", "store_true"),
}
conversion_threshold_in_mb = 10
gmail_attachment_threshold_mb = 25
valid_extensions_for_conversion = ["pdf", "djvu", "azw3", "epub", "mobi"]
extension_list = ["." + ext for ext in ["pdf", "epub", "djvu", "azw", "azw3", "mobi"]]
metadata_command = lambda x: ["fetch-ebook-metadata", "--opf", "--title", x]
file_appended_hash = "30234f2413d43e5c"
