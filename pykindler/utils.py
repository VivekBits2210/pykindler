from os import path, makedirs

def check_option_args_validity(dwd, email, file):
    import re
    is_dir = path.isdir(dwd) if dwd is not None else True
    is_email = False if email is not None and not re.match(r"^[a-z0-9](\.?[a-z0-9]){5,}@g(oogle)?mail\.com$",email) else True
    is_file = path.isfile(file) if file is not None else True

    if not is_dir:
        return f"Error: {dwd} is not an existing directory!"
    if not is_email:
        return f"Error: {email} is not a valid Kindle e-mail address!"
    if not is_file:
        return f"Error: {file} does not exist or is not a valid file!"

    return None
    
def setup_cron_job(dwd):
    print('Creating daily 12hr scheduled run for pykindler-run...')
    from crontab import CronTab
    cron = CronTab(user=True)

    # Clean if job exists
    for job in cron:
        if 'pykindler-run' in str(job):
            cron.remove(job)
            print(f'Cleaning out existing pykindler-run job: {str(job)}')

    # Make new job
    command = "pykindler-run" if dwd is None else f"pykindler-run -d {dwd}"
    job = cron.new(command=command)
    job.hour.every(12)
    cron.write()
    print('Scheduled job created!')


# Finds your downloads location
def get_downloads_folder_location():
    try: #GTK2
        import glib
        downloads_dir = glib.get_user_special_dir(glib.USER_DIRECTORY_DOWNLOAD)
    except (ModuleNotFoundError, AttributeError) as e: #GTK3
        try:
            from pgi.repository import GLib
            downloads_dir = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD)
        except (ModuleNotFoundError, AttributeError) as e: #GTK3
            downloads_dir = None
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

# Clean file names to help find metadata better
def clean_file_name(filename):
    import re
    extension = filename[filename.rfind('.')+1:]
    clean_name = filename[:filename.rfind('.')] 
    clean_name = re.sub(r'[^A-Za-z\' ]+', ' ',clean_name) 
    clean_name = re.sub(r' +', ' ', clean_name)
    clean_name = clean_name.strip().lower()
    clean_name = ' '.join([word for word in clean_name.split() if is_token_good(word)])
    return clean_name, extension

def make_required_directories(dir_list):
    for directory in dir_list:
        if not path.exists(directory):
            makedirs(directory)

def email_book(files, send_to):
    pass
    # TODO: Make this fn work
    # import smtplib
    # from pathlib import Path
    # from email.mime.multipart import MIMEMultipart
    # from email.mime.base import MIMEBase
    # from email.mime.text import MIMEText
    # from email.utils import COMMASPACE, formatdate
    # from email import encoders
    
    
    # send_from = 'pykindler-noreply@gmail.com'
    # server = "localhost"
    # subject = "Sending from pykindler"
    # message = f"Sending to your kindle ({send_to})"
    # port = 587
    # msg = MIMEMultipart()

    # msg['To'] = COMMASPACE.join(send_to)
    # msg['Date'] = formatdate(localtime=True)
    # msg['Subject'] = subject

    # msg.attach(MIMEText(message))

    # for file in files:    
    #     part = MIMEBase('application', "octet-stream")
    #     with open(path.join(converted_dir), 'rb') as file:
    #         part.set_payload(file.read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition',
    #                     'attachment; filename="{}"'.format(Path(path).name))
    #     msg.attach(part)

    # smtp = smtplib.SMTP(server, port)
    # smtp.login(username, password)
    # msg['From'] = send_from
    # smtp.sendmail(username, send_to, msg.as_string())
    # smtp.quit()