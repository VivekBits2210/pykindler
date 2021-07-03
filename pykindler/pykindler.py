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

def main(argv):
   inputfile = ''
   outputfile = ''
   usage = 'pykindler.py [-d <custom_download_folder>] [-e <kindle_email_id>] [-c Y (if you want a daily cron job setup)]'
   try:
      opts, args = getopt.getopt(argv,"hd:e:c:")
   except getopt.GetoptError:
      print(usage)
      sys.exit(2)
   dwd = email = None
   cron = False
   for opt, arg in opts:
      if opt == '-h':
         print(usage)
         sys.exit()
      elif opt == '-d':
         dwd = arg
      elif opt == '-e':
         email = arg
      elif opt == '-c' and arg=='Y':
         cron = True
   print(dwd,email,cron)
      
if __name__ == "__main__":
   main(sys.argv[1:])