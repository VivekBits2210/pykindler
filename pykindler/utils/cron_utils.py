# Clean out all previous pykinldler cron jobs?
def remove_pykindler_cron_jobs(cron):
    for job in cron:
        if "pykindler-run" in str(job):
            cron.remove(job)
            print(f"Removing existing pykindler-run job: {str(job)}")
    cron.write()


# Make new job
def create_pykindler_cron_job(cron, args):

    command = "pykindler-run"
    command = command + f" --folder {args.folder}" if args.folder is not None else ""
    command = command + f" --email {args.email}" if args.email is not None else ""
    command = command + f" --ext {args.ext}" if args.ext is not None else ""
    command = command + f" --email {args.email}" if args.email is not None else ""
    command = command + f" --kindle {args.kindle}" if args.kindle is not None else ""
    command = command + f" --force" if args.force else ""
    print(f"Creating scheduled job {command}...")
    job = cron.new(command=command)
    job.hour.every(12)
    cron.write()


# Create the job, plus housekeeping
def setup_cron_job(args):
    from crontab import CronTab

    cron = CronTab(user=True)
    remove_pykindler_cron_jobs(cron)
    create_pykindler_cron_job(cron, args)
    print("Scheduled job created!")
