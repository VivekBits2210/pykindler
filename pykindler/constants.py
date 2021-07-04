conversion_threshold_in_mb = 10
extension_list = ['.' + ext for ext in ['pdf','epub','djvu','azw','azw3']]
metadata_command =lambda x: ['fetch-ebook-metadata','--opf','--title', x]