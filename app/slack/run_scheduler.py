if __name__ == "__main__":
    from apscheduler.schedulers.background import BlockingScheduler
    from . import tasks

    scheduler = BlockingScheduler()

    scheduler.add_job(tasks.set_schedule, "cron", day_of_week="sun", hour="18")
    scheduler.add_job(tasks.remind, "cron", day_of_week="mon-sun", hour="5", kwargs={"tomorrow": False})
    scheduler.add_job(tasks.remind, "cron", day_of_week="mon-sun", hour="18", kwargs={"tomorrow": True})
    scheduler.start()
