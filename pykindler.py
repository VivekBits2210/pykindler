#!/usr/bin/env python
import sys, getopt
from pykindler.utils import check_option_args_validity, setup_cron_job
from pykindler.constants import *
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
      configure_file_locations(dwd)
      if cron is True:
         setup_cron_job()
      file_list = listdir(downloads_dir) if file is None else [file]
      process_and_convert_books(file_list)
      print('Exiting...')
      sys.exit()
if __name__ == "__main__":
   main(sys.argv[1:])