#!/usr/bin/env python
# from subprocess import call
# call(['chmod','+x','cli.py'])
# TODO: Bash stuff to be written here
# from crontab import CronTab
# cron = CronTab(user=True)
# job = cron.new(command='echo hello_world >> /home/$USER/Desktop/cron_pushed_output.txt')
# job.hour.every(12)
# cron.write()
# [str(l) for l in cron.find_command('')]

import sys, getopt
from .utils import check_option_args_validity, setup_cron_job
from .constants import configure_file_locations, downloads_dir
from .convertor import process_and_convert_books
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
      configure_file_locations(custom_dir=dwd)
      if cron is True:
         setup_cron_job()
      file_list = listdir(downloads_dir) if file is None else [file]
      process_and_convert_books(file_list)
      print('Exiting...')
      sys.exit()
if __name__ == "__main__":
   main(sys.argv[1:])