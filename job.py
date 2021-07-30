from apscheduler.schedulers.blocking import BlockingScheduler
from main import send


def mute():
    send(1)


def unmute():
    send(4)


scheduler = BlockingScheduler()
scheduler.add_job(unmute, 'cron', hour=8, minute=00)
scheduler.add_job(mute, 'cron', hour=9, minute=00)
scheduler.add_job(unmute, 'cron', hour=20, minute=00)
scheduler.add_job(mute, 'cron', hour=22, minute=00)
scheduler.start()
