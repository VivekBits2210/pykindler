#!/usr/bin/env python
import sys, getopt
from pykindler.utils import check_option_args_validity, setup_cron_job, get_downloads_folder_location
from pykindler.convertor import process_and_convert_books
from os import listdir
def main(argv):
   usage = 'pykindler.py [-d <custom_download_folder>] [-f <specific_absolute_path_to_convert>] [-e <kindle_email_id>] [-c Y (if you want a daily cron job setup, for the specified downloads folder)]'
   try:
      opts, args = getopt.getopt(argv,"hd:f:e:c:")
   except getopt.GetoptError:
      print(usage)
      sys.exit(2)
   dwd = email = file = None
   cron = False
   for opt, arg in opts:
      if opt == '-h':
         print(usage)
         sys.exit()
      if opt == '-f':
         file = arg
      elif opt == '-d':
         dwd = arg
      elif opt == '-e':
         email = arg
      elif opt == '-c' and arg=='Y':
         cron = True
   msg = check_option_args_validity(dwd,email,file)
   if msg is not None:
      print(msg)
      print(usage)
      sys.exit(2)
   else:
      if cron is True:
         setup_cron_job()
      download_dir = get_downloads_folder_location() if dwd is None else dwd
      file_list = listdir(download_dir) if file is None else [file]
      process_and_convert_books(file_list, download_dir)
      print('Exiting...')
      sys.exit()
if __name__ == "__main__":
   main(sys.argv[1:])