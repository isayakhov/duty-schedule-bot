import calendar
import logging
from datetime import datetime, timedelta
from typing import Optional

from app.config import DAYS_OF_DUTY

from . import exceptions
from .cache import cache
from .constants import EVENING_REMINDER, MORNING_REMINDER, PERSON_ADDED, PERSON_REMOVED, WEEK_SCHEDULE

logger = logging.getLogger(__name__)


def get_schedule(platform: str, chat_id: str) -> str:
    logger.info("Started to get schedule for chat_id: %s", chat_id)

    schedule = cache.get_schedule(platform, chat_id)
    if not schedule:
        raise exceptions.ScheduleNotFound

    logger.info("Finished to get schedule for chat_id: %s", chat_id)

    return "\n".join(f"{calendar.day_name[idx]}: {username}" for idx, username in enumerate(schedule))


def add_person(platform: str, chat_id: str, username: str) -> str:
    logger.info("Started to add username %s for chat_id: %s", username, chat_id)

    people = cache.get_people(platform, chat_id) or []

    if not username or not username.startswith("@"):
        raise exceptions.IncorrectUsername

    if username in people:
        raise exceptions.UserAlreadyExists

    people.append(username)
    cache.set_people(platform, chat_id, people)

    logger.info("Finished to remove username %s for chat_id: %s", username, chat_id)

    return PERSON_ADDED.format(username=username)


def remove_person(platform: str, chat_id: str, username: str) -> str:
    logger.info("Started to remove username %s for chat_id: %s", username, chat_id)

    people = cache.get_people(platform, chat_id) or []

    if not username or not username.startswith("@"):
        raise exceptions.IncorrectUsername

    if username not in people:
        raise exceptions.UserDoesNotExist

    people.remove(username)
    cache.set_people(platform, chat_id, people)

    logger.info("Finished to remove username %s for chat_id: %s", username, chat_id)

    return PERSON_REMOVED.format(username=username)


def _get_today() -> datetime:
    return datetime.today()


def set_schedule(platform: str, chat_id: str) -> Optional[str]:
    logger.info("Started to set up schedule for chat_id: %s", chat_id)

    users = cache.get_people(platform, chat_id)
    if not users:
        return None

    try:
        element_idx = users.index(cache.get_schedule(platform, chat_id)[-1]) + 1
    except (IndexError, ValueError):
        element_idx = 0

    schedule = []
    for _ in range(DAYS_OF_DUTY):
        if element_idx > len(users) - 1:
            element_idx = 0
        schedule.append(users[element_idx])
        element_idx += 1

    cache.set_schedule(platform, chat_id, schedule)

    logger.info("Finished to set up schedule: %s", chat_id)

    return WEEK_SCHEDULE.format(schedule=get_schedule(platform, chat_id))


def remind(platform: str, chat_id: str, tomorrow: bool) -> Optional[str]:
    logger.info("Started to remind schedule for chat_id: %s", chat_id)

    when_in_days = int(tomorrow)

    msg_map = {0: MORNING_REMINDER, 1: EVENING_REMINDER}

    idx = (_get_today() + timedelta(days=when_in_days)).weekday()
    if idx > DAYS_OF_DUTY - 1:
        return None

    schedule = cache.get_schedule(platform, chat_id)
    if idx > len(schedule) - 1:
        idx = 0

    logger.info("Finished to remind schedule for chat_id: %s", chat_id)

    return msg_map[when_in_days].format(username=schedule[idx])
